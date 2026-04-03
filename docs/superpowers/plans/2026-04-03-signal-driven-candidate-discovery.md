# Signal-Driven Candidate Discovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a repeatable GitHub code-search workflow that discovers likely cmux integrations from env vars and other high-signal evidence, then ranks and filters repos for manual review.

**Architecture:** Build one Python CLI script that searches GitHub code for weighted cmux signals, dedupes and enriches repositories with metadata, scores confidence, and prints Markdown or JSON reports. Keep pure decision logic in small functions so unit tests cover parsing, scoring, filtering, and section suggestion without calling GitHub.

**Tech Stack:** Python 3 stdlib, `gh` CLI, GitHub GraphQL API, `unittest`

---

## Planned File Structure

- Create: `scripts/discover_candidates.py`
  - Single entrypoint for search execution, metadata enrichment, scoring, filtering, and report rendering.
- Create: `tests/test_discover_candidates.py`
  - Unit tests for pure logic and report-shaping helpers.
- Create: `docs/research/discover-candidates.md`
  - Maintainer guide for running and interpreting the discovery workflow.
- Modify: `CONTRIBUTING.md`
  - Add the discovery script as the preferred starting point for finding new repos.

### Task 1: Build the testable discovery core

**Files:**
- Create: `scripts/discover_candidates.py`
- Test: `tests/test_discover_candidates.py`

- [ ] **Step 1: Write the failing tests for parsing, scoring, status, and section hints**

```python
import importlib.util
import pathlib
import unittest


def load_module():
    path = pathlib.Path(__file__).resolve().parent.parent / "scripts" / "discover_candidates.py"
    spec = importlib.util.spec_from_file_location("discover_candidates", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


dc = load_module()


class DiscoveryCoreTests(unittest.TestCase):
    def test_extract_readme_repo_slugs_skips_deeper_paths(self):
        text = """
| [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | Source |
| [HazAT/pi-config](https://github.com/HazAT/pi-config) | Item |
- [llv22/cmux_forward](https://github.com/llv22/cmux_forward) — Fork
| [Nightly](https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg) | Download |
"""
        self.assertEqual(
            dc.extract_existing_repo_slugs(text),
            {"manaflow-ai/cmux", "HazAT/pi-config", "llv22/cmux_forward"},
        )

    def test_score_repo_evidence_prefers_env_var_hits(self):
        hits = [
            dc.EvidenceHit(signal="CMUX_WORKSPACE_ID", weight=5, path="src/cmux.ts"),
            dc.EvidenceHit(signal="CMUX_SURFACE_ID", weight=5, path="README.md"),
            dc.EvidenceHit(signal="cmux browser", weight=2, path=".claude/skills/cmux/SKILL.md"),
        ]
        score = dc.score_evidence(hits)
        self.assertGreaterEqual(score, 10)

    def test_status_candidate_requires_readme_and_not_archived(self):
        repo = dc.RepoCandidate(
            slug="example/repo",
            stars=12,
            language="TypeScript",
            updated="2026-04-03",
            description="desc",
            archived=False,
            has_readme=True,
            already_listed=False,
            evidence_hits=[],
            score=8,
            suggested_section="By Agent > Pi",
            status="",
            notes=[],
        )
        status = dc.classify_candidate(
            repo,
            excluded_slugs=set(),
            minimum_candidate_score=8,
        )
        self.assertEqual(status, "candidate")

    def test_status_review_when_score_is_weak(self):
        repo = dc.RepoCandidate(
            slug="example/repo",
            stars=1,
            language="Shell",
            updated="2026-04-03",
            description="desc",
            archived=False,
            has_readme=True,
            already_listed=False,
            evidence_hits=[],
            score=3,
            suggested_section="",
            status="",
            notes=[],
        )
        status = dc.classify_candidate(
            repo,
            excluded_slugs=set(),
            minimum_candidate_score=8,
        )
        self.assertEqual(status, "review")

    def test_status_excluded_without_readme(self):
        repo = dc.RepoCandidate(
            slug="example/repo",
            stars=1,
            language="Shell",
            updated="2026-04-03",
            description="desc",
            archived=False,
            has_readme=False,
            already_listed=False,
            evidence_hits=[],
            score=12,
            suggested_section="",
            status="",
            notes=[],
        )
        status = dc.classify_candidate(
            repo,
            excluded_slugs=set(),
            minimum_candidate_score=8,
        )
        self.assertEqual(status, "excluded")

    def test_suggest_section_for_pi_repo(self):
        section = dc.suggest_section(
            slug="sanurb/pi-cmux-browser",
            description="Browser automation for Pi + cmux.",
            evidence_hits=[],
        )
        self.assertEqual(section, "By Agent > Pi")

    def test_path_penalty_downgrades_generated_or_vendored_paths(self):
        penalty = dc.path_confidence_adjustment(".claude/skills/cmux/SKILL.md")
        self.assertLess(penalty, 0)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to verify they fail**

Run:

```bash
rtk python -m unittest tests/test_discover_candidates.py -v
```

Expected: FAIL with import or missing-attribute errors because `scripts/discover_candidates.py` does not exist yet.

- [ ] **Step 3: Create the minimal discovery module with importable data structures and pure helpers**

```python
#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass, field
import re


REPO_PATTERN = re.compile(r"github\\.com/([\\w.\\-]+/[\\w.\\-]+?)(?:\\)|\\s|/|$)")
ENTRY_PREFIXES = ("| [", "- [")


@dataclass(frozen=True)
class EvidenceHit:
    signal: str
    weight: int
    path: str


@dataclass
class RepoCandidate:
    slug: str
    stars: int
    language: str
    updated: str
    description: str
    archived: bool
    has_readme: bool
    already_listed: bool
    evidence_hits: list[EvidenceHit] = field(default_factory=list)
    score: int = 0
    suggested_section: str = ""
    status: str = ""
    notes: list[str] = field(default_factory=list)


def extract_existing_repo_slugs(text: str) -> set[str]:
    slugs: set[str] = set()
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith(ENTRY_PREFIXES):
            continue
        for match in REPO_PATTERN.finditer(line):
            slug = match.group(1)
            if slug.count("/") == 1:
                slugs.add(slug)
    return slugs


def path_confidence_adjustment(path: str) -> int:
    lowered = path.lower()
    noisy_parts = (
        ".claude/skills/",
        ".agents/skills/",
        "skills/cmux-browser/agents/openai.yaml",
        ".atlas-analysis.json",
        ".worktrees/",
    )
    return -2 if any(part in lowered for part in noisy_parts) else 0


def score_evidence(hits: list[EvidenceHit]) -> int:
    total = 0
    for hit in hits:
        total += hit.weight + path_confidence_adjustment(hit.path)
    return max(total, 0)


def suggest_section(slug: str, description: str, evidence_hits: list[EvidenceHit]) -> str:
    haystack = f"{slug} {description}".lower()
    if "pi" in haystack:
        return "By Agent > Pi"
    if "opencode" in haystack:
        return "By Agent > OpenCode"
    if "copilot" in haystack or "amp" in haystack:
        return "By Agent > Copilot & Amp"
    if "mcp" in haystack:
        return "By Use Case > MCP Servers"
    if "worktree" in haystack or "workspace provider" in haystack:
        return "By Use Case > Workspace & Worktrees"
    if any(term in haystack for term in ("restore", "resurrect", "remote", "companion", "context", "mirror")):
        return "By Use Case > Monitor & Restore Sessions"
    if any(term in haystack for term in ("browser", "preview", "diff", "hub")):
        return "By Use Case > Browser Pane"
    if "skill" in haystack or "claude" in haystack:
        return "By Agent > Claude Code"
    return ""


def classify_candidate(repo: RepoCandidate, excluded_slugs: set[str], minimum_candidate_score: int) -> str:
    if repo.slug in excluded_slugs:
        return "excluded"
    if repo.already_listed:
        return "listed"
    if repo.archived or not repo.has_readme:
        return "excluded"
    if repo.score >= minimum_candidate_score:
        return "candidate"
    return "review"
```

- [ ] **Step 4: Run the tests to verify the discovery core passes**

Run:

```bash
rtk python -m unittest tests/test_discover_candidates.py -v
```

Expected: PASS for all tests in `DiscoveryCoreTests`.

- [ ] **Step 5: Commit the tested core**

```bash
rtk git add scripts/discover_candidates.py tests/test_discover_candidates.py
rtk git commit -m "feat: add tested candidate discovery core"
```

### Task 2: Implement live GitHub search, enrichment, and report rendering

**Files:**
- Modify: `scripts/discover_candidates.py`
- Test: `tests/test_discover_candidates.py`

- [ ] **Step 1: Add failing tests for report rendering and sorting**

```python
    def test_render_markdown_orders_candidates_before_review(self):
        candidate = dc.RepoCandidate(
            slug="good/repo",
            stars=20,
            language="TypeScript",
            updated="2026-04-03",
            description="Strong hit",
            archived=False,
            has_readme=True,
            already_listed=False,
            evidence_hits=[dc.EvidenceHit(signal="CMUX_WORKSPACE_ID", weight=5, path="src/cmux.ts")],
            score=10,
            suggested_section="By Agent > Pi",
            status="candidate",
            notes=[],
        )
        review = dc.RepoCandidate(
            slug="maybe/repo",
            stars=5,
            language="Shell",
            updated="2026-04-03",
            description="Weak hit",
            archived=False,
            has_readme=True,
            already_listed=False,
            evidence_hits=[dc.EvidenceHit(signal="cmux notify", weight=2, path=".claude/skills/cmux/SKILL.md")],
            score=2,
            suggested_section="",
            status="review",
            notes=[],
        )
        output = dc.render_markdown([review, candidate], include_listed=False, include_excluded=False)
        self.assertLess(output.index("good/repo"), output.index("maybe/repo"))
        self.assertIn("| good/repo | candidate | 10 |", output)
```

- [ ] **Step 2: Run the tests to verify the new rendering test fails**

Run:

```bash
rtk python -m unittest tests/test_discover_candidates.py -v
```

Expected: FAIL because `render_markdown` does not exist yet.

- [ ] **Step 3: Expand the script into a complete CLI**

Add the following code to `scripts/discover_candidates.py` after the pure helpers:

```python
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path


README = Path(__file__).resolve().parent.parent / "README.md"
SIGNALS = (
    {"query": "CMUX_WORKSPACE_ID", "weight": 5},
    {"query": "CMUX_SURFACE_ID", "weight": 5},
    {"query": "CMUX_SOCKET_PATH", "weight": 5},
    {"query": '"github.com/manaflow-ai/cmux"', "weight": 3},
    {"query": '"cmux.dev"', "weight": 3},
    {"query": '"cmux browser"', "weight": 2},
    {"query": '"cmux notify"', "weight": 2},
)
EXCLUDED_SLUGS = {
    "manaflow-ai/cmux",
    "manaflow-ai/manaflow",
    "yigitkonur/awesome-cmux",
}


def run_json_command(args: list[str]) -> list[dict] | dict:
    result = subprocess.run(args, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "command failed")
    return json.loads(result.stdout)


def search_signal(query: str, weight: int, limit: int) -> dict[str, list[EvidenceHit]]:
    results = run_json_command(
        [
            "gh", "search", "code", query,
            "--match", "file",
            "--limit", str(limit),
            "--json", "repository,path",
        ]
    )
    grouped: dict[str, list[EvidenceHit]] = {}
    for item in results:
        slug = item["repository"]["nameWithOwner"]
        grouped.setdefault(slug, []).append(
            EvidenceHit(signal=query, weight=weight, path=item["path"])
        )
    return grouped


def gh_graphql(query: str) -> dict:
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={query}"],
        capture_output=True,
        text=True,
        timeout=60,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "graphql failed")
    return json.loads(result.stdout)


def fetch_repo_metadata(slugs: list[str]) -> dict[str, dict]:
    metadata: dict[str, dict] = {}
    for batch_start in range(0, len(slugs), 25):
        batch = slugs[batch_start:batch_start + 25]
        parts = []
        for index, slug in enumerate(batch):
            owner, name = slug.split("/", 1)
            parts.append(
                f'r{index}: repository(owner: "{owner}", name: "{name}") '
                "{ nameWithOwner description stargazerCount pushedAt isArchived primaryLanguage { name } object(expression: \"HEAD:README.md\") { ... on Blob { text } } }"
            )
        response = gh_graphql("{ " + " ".join(parts) + " }")
        for index, slug in enumerate(batch):
            repo = response["data"].get(f"r{index}")
            if not repo:
                continue
            metadata[slug] = {
                "description": repo.get("description") or "",
                "stars": repo.get("stargazerCount") or 0,
                "updated": (repo.get("pushedAt") or "")[:10],
                "archived": bool(repo.get("isArchived")),
                "language": ((repo.get("primaryLanguage") or {}).get("name")) or "?",
                "has_readme": bool(repo.get("object")),
            }
        time.sleep(1)
    return metadata


def build_candidates(limit_per_signal: int, minimum_candidate_score: int) -> list[RepoCandidate]:
    existing = extract_existing_repo_slugs(README.read_text())
    evidence_by_slug: dict[str, list[EvidenceHit]] = {}
    for signal in SIGNALS:
        grouped = search_signal(signal["query"], signal["weight"], limit_per_signal)
        for slug, hits in grouped.items():
            evidence_by_slug.setdefault(slug, []).extend(hits)
    metadata = fetch_repo_metadata(sorted(evidence_by_slug))
    candidates: list[RepoCandidate] = []
    for slug, hits in evidence_by_slug.items():
        info = metadata.get(slug, {})
        repo = RepoCandidate(
            slug=slug,
            stars=info.get("stars", 0),
            language=info.get("language", "?"),
            updated=info.get("updated", ""),
            description=info.get("description", ""),
            archived=info.get("archived", False),
            has_readme=info.get("has_readme", False),
            already_listed=slug in existing,
            evidence_hits=hits,
        )
        repo.score = score_evidence(hits)
        repo.suggested_section = suggest_section(repo.slug, repo.description, repo.evidence_hits)
        repo.status = classify_candidate(repo, EXCLUDED_SLUGS, minimum_candidate_score)
        candidates.append(repo)
    return sorted(candidates, key=lambda repo: (repo.status != "candidate", -repo.score, -repo.stars, repo.slug.lower()))


def render_markdown(candidates: list[RepoCandidate], include_listed: bool, include_excluded: bool) -> str:
    visible = []
    for repo in candidates:
        if repo.status == "listed" and not include_listed:
            continue
        if repo.status == "excluded" and not include_excluded:
            continue
        visible.append(repo)
    lines = [
        "| Repo | Status | Score | Stars | Lang | Updated | Suggested Section | Evidence |",
        "|------|--------|-------|-------|------|---------|-------------------|----------|",
    ]
    for repo in visible:
        evidence = ", ".join(sorted({hit.signal for hit in repo.evidence_hits}))
        lines.append(
            f"| {repo.slug} | {repo.status} | {repo.score} | {repo.stars} | {repo.language} | {repo.updated} | {repo.suggested_section or '—'} | {evidence} |"
        )
    return "\\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit-per-signal", type=int, default=20)
    parser.add_argument("--minimum-candidate-score", type=int, default=8)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--include-listed", action="store_true")
    parser.add_argument("--include-excluded", action="store_true")
    args = parser.parse_args()

    candidates = build_candidates(args.limit_per_signal, args.minimum_candidate_score)
    if args.format == "json":
        print(json.dumps([repo.__dict__ | {"evidence_hits": [hit.__dict__ for hit in repo.evidence_hits]} for repo in candidates], indent=2))
    else:
        print(render_markdown(candidates, args.include_listed, args.include_excluded))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Re-run the tests to verify the rendering test passes**

Run:

```bash
rtk python -m unittest tests/test_discover_candidates.py -v
```

Expected: PASS.

- [ ] **Step 5: Run the live discovery command against GitHub**

Run:

```bash
rtk python scripts/discover_candidates.py --limit-per-signal 10 --format markdown
```

Expected:
- command exits with code `0`
- output contains the markdown header row
- output includes at least some already-known cmux repos such as `espennilsen/pi`, `HazAT/pi-config`, or `AtAFork/ghostty-claude-code-session-restore`
- output marks already-listed repos as `listed` unless filtered out

- [ ] **Step 6: Commit the full discovery workflow**

```bash
rtk git add scripts/discover_candidates.py tests/test_discover_candidates.py
rtk git commit -m "feat: add live cmux candidate discovery workflow"
```

### Task 3: Document maintainer usage and connect it to contribution flow

**Files:**
- Create: `docs/research/discover-candidates.md`
- Modify: `CONTRIBUTING.md`

- [ ] **Step 1: Write the failing docs expectation as a content checklist**

Create `docs/research/discover-candidates.md` with the following required sections:

```md
# Discover Candidates

## Why this exists
- direct repo search misses integrations that only expose `CMUX_*` env vars or cmux hooks in code

## Run the tool
- include the command `rtk python scripts/discover_candidates.py --limit-per-signal 20 --format markdown`

## How to read the output
- `candidate` means strong evidence plus basic inclusion checks passed
- `review` means inspect manually before adding
- `listed` means already in README
- `excluded` means filtered out

## Review checklist
- public repo
- root README exists
- actually uses a cmux API or env var
- section placement still needs a human decision
```

- [ ] **Step 2: Add the maintainer guide**

```md
# Discover Candidates

## Why this exists

Some valid cmux integrations never advertise themselves in the repository name or description. They show up only through code-level evidence such as `CMUX_WORKSPACE_ID`, `CMUX_SURFACE_ID`, `CMUX_SOCKET_PATH`, or links back to the upstream cmux docs. This workflow searches for those signals directly so candidate discovery is repeatable instead of ad hoc.

## Run the tool

Run `rtk python scripts/discover_candidates.py --limit-per-signal 20 --format markdown`.

For a fuller audit view:

Run `rtk python scripts/discover_candidates.py --limit-per-signal 20 --format json --include-listed --include-excluded`.

## How to read the output

- `candidate`: strong enough evidence and basic inclusion checks passed
- `review`: likely interesting, but signals are weak or noisy
- `listed`: already present in `README.md`
- `excluded`: filtered out because it is archived, missing a README, or explicitly out of scope

The score is directional, not authoritative. Treat it as ranking help, not permission to skip review.

## Review checklist

Before adding a repo to the awesome list, still verify:

1. the repo is public and has a usable root README
2. it genuinely uses a cmux API, env var, CLI command, or socket integration
3. the suggested section is actually correct
4. the description you write follows `CONTRIBUTING.md`
```

- [ ] **Step 3: Add a discovery hint to `CONTRIBUTING.md`**

Insert this section before `## Pull request checklist`:

```md
## Discovery workflow

To find new candidates, start with:

`rtk python scripts/discover_candidates.py --limit-per-signal 20 --format markdown`

This searches for cmux-specific evidence inside repository contents, including `CMUX_WORKSPACE_ID`, `CMUX_SURFACE_ID`, and `CMUX_SOCKET_PATH`, then ranks repos for manual review. It is a discovery aid, not an auto-merge tool: still verify README presence, actual cmux usage, and final section placement before editing `README.md`.
```

- [ ] **Step 4: Verify the docs files read clearly in the terminal**

Run:

```bash
rtk sed -n '1,220p' docs/research/discover-candidates.md
rtk sed -n '1,240p' CONTRIBUTING.md
```

Expected:
- both files render valid Markdown in plain text
- commands are prefixed with `rtk`
- wording matches the repo's neutral maintainer tone

- [ ] **Step 5: Commit the documentation update**

```bash
rtk git add docs/research/discover-candidates.md CONTRIBUTING.md
rtk git commit -m "docs: document signal-driven candidate discovery"
```

### Task 4: Full verification

**Files:**
- Verify: `scripts/discover_candidates.py`
- Verify: `tests/test_discover_candidates.py`
- Verify: `docs/research/discover-candidates.md`
- Verify: `CONTRIBUTING.md`

- [ ] **Step 1: Run the unit test suite**

```bash
rtk python -m unittest tests/test_discover_candidates.py -v
```

Expected: PASS with zero failures.

- [ ] **Step 2: Run the live discovery command in maintainer mode**

```bash
rtk python scripts/discover_candidates.py --limit-per-signal 10 --format markdown
```

Expected:
- command exits with code `0`
- report includes visible candidate rows
- report includes evidence sourced from `CMUX_*` hits

- [ ] **Step 3: Run the machine-readable output mode**

```bash
rtk python scripts/discover_candidates.py --limit-per-signal 5 --format json --include-listed --include-excluded > /tmp/cmux-candidates.json
rtk sed -n '1,120p' /tmp/cmux-candidates.json
```

Expected:
- JSON file is created
- objects include `slug`, `status`, `score`, `suggested_section`, and `evidence_hits`

- [ ] **Step 4: Run git diff hygiene checks**

```bash
rtk git diff --check
rtk git status --short
```

Expected:
- `rtk git diff --check` exits with code `0`
- only the intended files are modified

- [ ] **Step 5: Commit the final verification state if needed**

```bash
rtk git add scripts/discover_candidates.py tests/test_discover_candidates.py docs/research/discover-candidates.md CONTRIBUTING.md
rtk git commit -m "chore: finalize candidate discovery verification"
```

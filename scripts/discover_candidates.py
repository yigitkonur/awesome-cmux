#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit


README = Path(__file__).resolve().parent.parent / "README.md"
REPO_URL_PATTERN = re.compile(r"https?://github\.com/[^\s<>\]\)]+")
EXPLICIT_EXCLUDED_SLUGS = {
    "yigitkonur/awesome-cmux",
    "manaflow-ai/cmux",
    "ghostty-org/ghostty",
    "vercel-labs/agent-browser",
}
HIGH_CONFIDENCE_SIGNALS = {
    "CMUX_WORKSPACE_ID",
    "CMUX_SURFACE_ID",
    "CMUX_SOCKET_PATH",
}
STATUS_ORDER = {
    "candidate": 0,
    "review": 1,
    "listed": 2,
    "excluded": 3,
}
DEFAULT_INCLUDED_STATUSES = ("candidate", "review")
DEFAULT_SIGNAL_LIMIT = 15
DEFAULT_CANDIDATE_SCORE = 8
DEFAULT_METADATA_BATCH_SIZE = 25


@dataclass(frozen=True)
class SignalSpec:
    name: str
    query: str
    weight: int
    limit: int = DEFAULT_SIGNAL_LIMIT


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
    metadata_loaded: bool = False
    evidence_hits: list[EvidenceHit] = field(default_factory=list)
    score: int = 0
    suggested_section: str = ""
    status: str = ""
    notes: list[str] = field(default_factory=list)


SIGNALS: tuple[SignalSpec, ...] = (
    SignalSpec("CMUX_WORKSPACE_ID", "CMUX_WORKSPACE_ID", 10, 12),
    SignalSpec("CMUX_SURFACE_ID", "CMUX_SURFACE_ID", 10, 12),
    SignalSpec("CMUX_SOCKET_PATH", "CMUX_SOCKET_PATH", 10, 12),
    SignalSpec("CMUX_CLI_PATH", "CMUX_CLI_PATH", 7, 10),
    SignalSpec("cmux.dev", "cmux.dev", 4, 8),
    SignalSpec("github.com/manaflow-ai/cmux", "github.com/manaflow-ai/cmux", 4, 8),
    SignalSpec("cmux browser", '"cmux browser"', 2, 10),
    SignalSpec("cmux notify", '"cmux notify"', 2, 10),
    SignalSpec("read-screen", '"read-screen"', 2, 10),
    SignalSpec("cmux new-workspace", '"cmux new-workspace"', 2, 10),
)

NOISY_PATH_PATTERNS: tuple[tuple[str, int], ...] = (
    ("/.claude/skills/", -6),
    ("/.agents/skills/", -6),
    ("skills/", -5),
    ("references/", -5),
    ("reference/", -5),
    ("docs/", -4),
    ("readme.md", -4),
    ("claude.md", -4),
    ("agents.md", -4),
    ("todo.md", -4),
    (".github/", -3),
    ("vendor/", -3),
    ("vendored/", -3),
    ("node_modules/", -3),
    ("dist/", -3),
    ("build/", -3),
    (".generated.", -3),
    (".git", -3),
)


def _slug_from_github_url(url: str) -> str | None:
    cleaned = url.rstrip(".,;:!?")
    parsed = urlsplit(cleaned)
    if parsed.netloc.lower() != "github.com":
        return None
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) != 2:
        return None
    owner, repo = parts
    return f"{owner}/{repo}"


def extract_existing_repo_slugs(text: str) -> set[str]:
    slugs: set[str] = set()
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith(("| [", "- [")):
            continue
        for match in REPO_URL_PATTERN.finditer(line):
            slug = _slug_from_github_url(match.group(0))
            if slug:
                slugs.add(slug)
    return slugs


def load_listed_repo_slugs() -> set[str]:
    try:
        return extract_existing_repo_slugs(README.read_text())
    except OSError:
        return set()


def path_confidence_adjustment(path: str) -> int:
    lowered = path.lower()
    for pattern, penalty in NOISY_PATH_PATTERNS:
        if pattern in lowered:
            return penalty
    if lowered.endswith(".min.js") or lowered.endswith(".min.ts"):
        return -1
    if any(part.startswith(".") for part in lowered.split("/") if part):
        return -3
    return 0


def score_evidence(hits: list[EvidenceHit]) -> int:
    total = 0
    for hit in hits:
        total += hit.weight + path_confidence_adjustment(hit.path)
    return max(total, 0)


def has_high_confidence_evidence(hits: list[EvidenceHit]) -> bool:
    return any(hit.signal in HIGH_CONFIDENCE_SIGNALS for hit in hits)


def suggest_section(slug: str, description: str, evidence_hits: list[EvidenceHit]) -> str:
    haystack = " ".join(
        [
            slug,
            description,
            " ".join(hit.signal for hit in evidence_hits),
            " ".join(hit.path for hit in evidence_hits),
        ]
    ).lower()

    if any(term in haystack for term in ("pi-cmux", " pi ", "pi/")):
        return "By Agent > Pi"
    if "opencode" in haystack:
        return "By Agent > OpenCode"
    if "copilot" in haystack or "amp" in haystack:
        return "By Agent > Copilot & Amp"
    if "skill" in haystack and "claude" in haystack:
        return "By Agent > Claude Code > Skills"
    if "mcp" in haystack:
        return "By Use Case > MCP Servers"
    if "worktree" in haystack or "workspace provider" in haystack:
        return "By Use Case > Workspace & Worktrees"
    if any(term in haystack for term in ("restore", "resurrect", "remote", "companion", "context", "mirror")):
        return "By Use Case > Monitor & Restore Sessions"
    if any(term in haystack for term in ("browser", "preview", "diff", "hub")):
        return "By Use Case > Browser Pane"
    return ""


def classify_candidate(repo: RepoCandidate, excluded_slugs: set[str], minimum_candidate_score: int) -> str:
    if repo.slug in excluded_slugs:
        return "excluded"
    if repo.already_listed:
        return "listed"
    if repo.archived:
        return "excluded"
    if not repo.metadata_loaded:
        return "review"
    if not repo.has_readme:
        return "excluded"
    if repo.score >= minimum_candidate_score and has_high_confidence_evidence(repo.evidence_hits):
        return "candidate"
    return "review"


def _run_gh(args: list[str], *, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["gh", *args],
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def ensure_gh_auth() -> None:
    result = _run_gh(["auth", "status", "-h", "github.com"], timeout=20)
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or "gh auth status failed"
        raise RuntimeError(
            "GitHub CLI authentication is required. Run `gh auth login` or fix the existing auth session.\n"
            f"{message}"
        )


def search_code_for_signal(signal: SignalSpec) -> list[dict]:
    result = _run_gh(
        [
            "search",
            "code",
            signal.query,
            "--match",
            "file",
            "--json",
            "path,repository,textMatches,url",
            "--limit",
            str(signal.limit),
        ],
        timeout=90,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or f"gh search code failed for {signal.name}"
        raise RuntimeError(message)
    if not result.stdout.strip():
        return []
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Could not parse gh search code JSON for {signal.name}: {exc}") from exc
    if not isinstance(payload, list):
        raise RuntimeError(f"Unexpected gh search code response for {signal.name}: {type(payload).__name__}")
    return payload


def parse_repository_slug(item: dict) -> str | None:
    repository = item.get("repository")
    if isinstance(repository, dict):
        slug = repository.get("nameWithOwner")
        if isinstance(slug, str) and slug.count("/") == 1:
            return slug
    if isinstance(repository, str) and repository.count("/") == 1:
        return repository
    return None


def aggregate_search_hits(signals: tuple[SignalSpec, ...]) -> tuple[dict[str, RepoCandidate], list[str]]:
    repositories: dict[str, RepoCandidate] = {}
    warnings: list[str] = []
    seen_hits: set[tuple[str, str, str]] = set()

    for signal in signals:
        try:
            results = search_code_for_signal(signal)
        except RuntimeError as exc:
            warnings.append(f"{signal.name}: {exc}")
            continue

        for item in results:
            slug = parse_repository_slug(item)
            path = item.get("path")
            if not slug or not isinstance(path, str):
                continue

            hit_key = (slug, path, signal.name)
            if hit_key in seen_hits:
                continue
            seen_hits.add(hit_key)

            candidate = repositories.get(slug)
            if candidate is None:
                candidate = RepoCandidate(
                    slug=slug,
                    stars=0,
                    language="",
                    updated="",
                    description="",
                    archived=False,
                    has_readme=False,
                    already_listed=False,
                )
                repositories[slug] = candidate

            candidate.evidence_hits.append(EvidenceHit(signal=signal.name, weight=signal.weight, path=path))

    return repositories, warnings


def _graphql_batch_query(slugs: list[str]) -> str:
    parts: list[str] = []
    for index, slug in enumerate(slugs):
        owner, name = slug.split("/", 1)
        parts.append(
            f'''r{index}: repository(owner: "{owner}", name: "{name}") {{
  nameWithOwner
  description
  stargazerCount
  pushedAt
  isArchived
  primaryLanguage {{ name }}
  object(expression: "HEAD:README.md") {{
    __typename
    ... on Blob {{ byteSize }}
  }}
}}'''
        )
    return "query { " + " ".join(parts) + " }"


def _graphql_single_query(slug: str) -> str:
    owner, name = slug.split("/", 1)
    return f'''query {{
  repo: repository(owner: "{owner}", name: "{name}") {{
    nameWithOwner
    description
    stargazerCount
    pushedAt
    isArchived
    primaryLanguage {{ name }}
    object(expression: "HEAD:README.md") {{
      __typename
      ... on Blob {{ byteSize }}
    }}
  }}
}}'''


def _run_graphql(query: str, *, timeout: int = 60) -> dict:
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={query}"],
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or "gh api graphql failed"
        return {"errors": [message]}
    if not result.stdout.strip():
        return {"data": {}}
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        return {"errors": [f"Could not parse GraphQL JSON: {exc}"]}
    if not isinstance(payload, dict):
        return {"errors": [f"Unexpected GraphQL response: {type(payload).__name__}"]}
    return payload


def _metadata_from_repo_node(slug: str, node: dict) -> dict:
    primary_language = node.get("primaryLanguage") or {}
    readme = node.get("object") or {}
    return {
        "slug": node.get("nameWithOwner") or slug,
        "stars": int(node.get("stargazerCount") or 0),
        "language": primary_language.get("name") or "",
        "updated": str(node.get("pushedAt") or "")[:10],
        "description": node.get("description") or "",
        "archived": bool(node.get("isArchived")),
        "has_readme": readme.get("__typename") == "Blob" and readme.get("byteSize") is not None,
        "metadata_loaded": True,
    }


def fetch_repository_metadata(slugs: list[str], *, batch_size: int = DEFAULT_METADATA_BATCH_SIZE) -> tuple[dict[str, dict], list[str]]:
    metadata: dict[str, dict] = {}
    warnings: list[str] = []

    for start in range(0, len(slugs), batch_size):
        batch = slugs[start : start + batch_size]
        if not batch:
            continue

        payload = _run_graphql(_graphql_batch_query(batch), timeout=90)
        data = payload.get("data") or {}
        errors = payload.get("errors") or []

        missing: list[str] = []
        for index, slug in enumerate(batch):
            node = data.get(f"r{index}")
            if isinstance(node, dict):
                metadata[slug] = _metadata_from_repo_node(slug, node)
            else:
                missing.append(slug)

        if missing and (errors or not data):
            for slug in missing:
                single_payload = _run_graphql(_graphql_single_query(slug), timeout=60)
                single_data = (single_payload.get("data") or {}).get("repo")
                if isinstance(single_data, dict):
                    metadata[slug] = _metadata_from_repo_node(slug, single_data)
                else:
                    single_errors = single_payload.get("errors") or []
                    if single_errors:
                        warnings.append(f"{slug}: {single_errors[0]}")
                    else:
                        warnings.append(f"{slug}: metadata unavailable")
        elif missing:
            warnings.append(f"{len(missing)} repos missing GraphQL metadata in batch")

        if errors and not data:
            warnings.append(f"GraphQL batch failed for {len(batch)} repos")

    return metadata, warnings


def populate_metadata(candidates: dict[str, RepoCandidate], metadata: dict[str, dict]) -> None:
    for slug, candidate in candidates.items():
        repo_metadata = metadata.get(slug)
        if repo_metadata is None:
            candidate.notes.append("metadata unavailable")
            candidate.metadata_loaded = False
            candidate.suggested_section = suggest_section(candidate.slug, candidate.description, candidate.evidence_hits)
            candidate.score = score_evidence(candidate.evidence_hits)
            continue

        candidate.slug = repo_metadata["slug"]
        candidate.stars = repo_metadata["stars"]
        candidate.language = repo_metadata["language"]
        candidate.updated = repo_metadata["updated"]
        candidate.description = repo_metadata["description"]
        candidate.archived = repo_metadata["archived"]
        candidate.has_readme = repo_metadata["has_readme"]
        candidate.metadata_loaded = repo_metadata["metadata_loaded"]
        candidate.score = score_evidence(candidate.evidence_hits)
        candidate.suggested_section = suggest_section(candidate.slug, candidate.description, candidate.evidence_hits)


def mark_listed_candidates(candidates: dict[str, RepoCandidate], listed_slugs: set[str]) -> None:
    for slug, candidate in candidates.items():
        candidate.already_listed = slug in listed_slugs


def build_candidates(
    signals: tuple[SignalSpec, ...] = SIGNALS,
    *,
    candidate_score: int = DEFAULT_CANDIDATE_SCORE,
    metadata_batch_size: int = DEFAULT_METADATA_BATCH_SIZE,
) -> tuple[list[RepoCandidate], list[str]]:
    discovered, warnings = aggregate_search_hits(signals)
    slugs = sorted(discovered)
    mark_listed_candidates(discovered, load_listed_repo_slugs())
    metadata, metadata_warnings = fetch_repository_metadata(slugs, batch_size=metadata_batch_size)
    warnings.extend(metadata_warnings)
    populate_metadata(discovered, metadata)

    for candidate in discovered.values():
        candidate.status = classify_candidate(candidate, EXPLICIT_EXCLUDED_SLUGS, candidate_score)

    ordered = sorted(
        discovered.values(),
        key=lambda candidate: (
            STATUS_ORDER.get(candidate.status, 99),
            -candidate.score,
            -candidate.stars,
            _updated_sort_key(candidate.updated),
            candidate.slug,
        ),
    )
    return ordered, warnings


def _updated_sort_key(updated: str) -> tuple[int, int, int]:
    parts = updated.split("-")
    if len(parts) == 3 and all(part.isdigit() for part in parts):
        year, month, day = (int(part) for part in parts)
        return (-year, -month, -day)
    return (9999, 99, 99)


def _escape_markdown_cell(value: object) -> str:
    text = str(value).replace("\n", " ")
    return text.replace("|", "\\|")


def _format_repo_link(slug: str) -> str:
    return f"[{slug}](https://github.com/{slug})"


def evidence_summary(repo: RepoCandidate, max_items: int = 3) -> str:
    parts: list[str] = []
    for hit in repo.evidence_hits[:max_items]:
        parts.append(f"{hit.signal} @ {hit.path}")
    if len(repo.evidence_hits) > max_items:
        parts.append(f"+{len(repo.evidence_hits) - max_items} more")
    return "; ".join(parts)


def selected_candidates(candidates: list[RepoCandidate], included_statuses: set[str]) -> list[RepoCandidate]:
    return [candidate for candidate in candidates if candidate.status in included_statuses]


def render_markdown_report(candidates: list[RepoCandidate], included_statuses: set[str]) -> str:
    selected = selected_candidates(candidates, included_statuses)
    lines = [
        f"# Signal-driven candidate discovery",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"Showing statuses: {', '.join(sorted(included_statuses))}",
        "",
        "| repo | status | score | stars | language | updated | suggested section | evidence |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    for candidate in selected:
        lines.append(
            "| "
            + " | ".join(
                [
                    _escape_markdown_cell(_format_repo_link(candidate.slug)),
                    _escape_markdown_cell(candidate.status),
                    _escape_markdown_cell(candidate.score),
                    _escape_markdown_cell(candidate.stars),
                    _escape_markdown_cell(candidate.language or "—"),
                    _escape_markdown_cell(candidate.updated or "—"),
                    _escape_markdown_cell(candidate.suggested_section or "—"),
                    _escape_markdown_cell(evidence_summary(candidate) or "—"),
                ]
            )
            + " |"
        )

    if not selected:
        lines.append("")
        lines.append("_No repositories matched the selected statuses._")

    return "\n".join(lines)


def render_json_report(candidates: list[RepoCandidate], included_statuses: set[str], warnings: list[str] | None = None) -> str:
    selected = selected_candidates(candidates, included_statuses)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "statuses": sorted(included_statuses),
        "warnings": warnings or [],
        "results": [
            {
                "slug": candidate.slug,
                "status": candidate.status,
                "score": candidate.score,
                "stars": candidate.stars,
                "language": candidate.language,
                "updated": candidate.updated,
                "description": candidate.description,
                "archived": candidate.archived,
                "has_readme": candidate.has_readme,
                "metadata_loaded": candidate.metadata_loaded,
                "already_listed": candidate.already_listed,
                "suggested_section": candidate.suggested_section,
                "evidence": [asdict(hit) for hit in candidate.evidence_hits],
                "notes": candidate.notes,
            }
            for candidate in selected
        ],
    }
    return json.dumps(payload, indent=2, sort_keys=True)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Discover candidate repositories from live GitHub code search.")
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format.",
    )
    parser.add_argument(
        "--limit-per-signal",
        type=int,
        default=DEFAULT_SIGNAL_LIMIT,
        help="Maximum code-search results per signal.",
    )
    parser.add_argument(
        "--minimum-candidate-score",
        type=int,
        default=DEFAULT_CANDIDATE_SCORE,
        help="Minimum score for candidate classification when high-confidence evidence is present.",
    )
    parser.add_argument(
        "--metadata-batch-size",
        type=int,
        default=DEFAULT_METADATA_BATCH_SIZE,
        help="GraphQL batch size for repo metadata lookups.",
    )
    parser.add_argument(
        "--include-listed",
        action="store_true",
        help="Include already-listed repositories in the report.",
    )
    parser.add_argument(
        "--include-excluded",
        action="store_true",
        help="Include excluded repositories in the report.",
    )
    return parser.parse_args(argv)


def _configured_signals(signal_limit: int) -> tuple[SignalSpec, ...]:
    configured: list[SignalSpec] = []
    for signal in SIGNALS:
        configured.append(
            SignalSpec(
                name=signal.name,
                query=signal.query,
                weight=signal.weight,
                limit=min(signal.limit, signal_limit),
            )
        )
    return tuple(configured)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        ensure_gh_auth()
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return 1

    included_statuses = set(DEFAULT_INCLUDED_STATUSES)
    if args.include_listed:
        included_statuses.add("listed")
    if args.include_excluded:
        included_statuses.add("excluded")

    signals = _configured_signals(args.limit_per_signal)
    candidates, warnings = build_candidates(
        signals,
        candidate_score=args.minimum_candidate_score,
        metadata_batch_size=args.metadata_batch_size,
    )

    if args.format == "json":
        print(render_json_report(candidates, included_statuses, warnings))
    else:
        report = render_markdown_report(candidates, included_statuses)
        print(report)
        if warnings:
            print()
            print("Warnings:")
            for warning in warnings:
                print(f"- {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass, field
import re
from urllib.parse import urlsplit


README_GITHUB_URL_PATTERN = re.compile(r"https?://github\.com/[^\s<>\]\)]+")
NOISY_PATH_PATTERNS = (
    ".claude/skills/",
    ".agents/skills/",
    ".worktrees/",
    "vendor/",
    "vendored/",
    "node_modules/",
    "/dist/",
    "/build/",
    ".generated.",
)


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
        for match in README_GITHUB_URL_PATTERN.finditer(line):
            slug = _slug_from_github_url(match.group(0))
            if slug:
                slugs.add(slug)
    return slugs


def path_confidence_adjustment(path: str) -> int:
    lowered = path.lower()
    if any(pattern in lowered for pattern in NOISY_PATH_PATTERNS):
        return -2
    if lowered.endswith(".min.js") or lowered.endswith(".min.ts"):
        return -1
    return 0


def score_evidence(hits: list[EvidenceHit]) -> int:
    total = 0
    for hit in hits:
        total += hit.weight + path_confidence_adjustment(hit.path)
    return max(total, 0)


def has_high_confidence_evidence(hits: list[EvidenceHit]) -> bool:
    return any(hit.signal.upper().startswith("CMUX_") for hit in hits)


def suggest_section(slug: str, description: str, evidence_hits: list[EvidenceHit]) -> str:
    haystack = " ".join(
        [slug, description, " ".join(hit.signal for hit in evidence_hits), " ".join(hit.path for hit in evidence_hits)]
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
    if repo.archived or not repo.has_readme:
        return "excluded"
    if repo.score >= minimum_candidate_score and has_high_confidence_evidence(repo.evidence_hits):
        return "candidate"
    return "review"

#!/usr/bin/env python3
"""Update star counts and last-commit dates in README.md from the GitHub API."""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

STAR_THRESHOLD = 5
README = Path(__file__).resolve().parent.parent / "README.md"
REPO_PATTERN = re.compile(r"github\.com/([\w.\-]+/[\w.\-]+)")
STAR_PATTERN = re.compile(r" · ★\d+")


def gh_graphql(query: str) -> dict:
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={query}"],
        capture_output=True, text=True, timeout=30,
    )
    if result.returncode != 0:
        print(f"GraphQL error: {result.stderr}", file=sys.stderr)
        return {}
    return json.loads(result.stdout)


def fetch_repo_meta(slugs: list[str]) -> dict[str, dict]:
    """Fetch stars + pushedAt for up to 100 repos via a single GraphQL query."""
    meta = {}
    # GitHub GraphQL max aliases ~100; batch if needed
    for batch_start in range(0, len(slugs), 80):
        batch = slugs[batch_start:batch_start + 80]
        fragments = []
        for i, slug in enumerate(batch):
            owner, name = slug.split("/", 1)
            alias = f"r{i}"
            fragments.append(
                f'{alias}: repository(owner: "{owner}", name: "{name}") {{'
                f" stargazerCount pushedAt isArchived }}"
            )
        query = "{ " + " ".join(fragments) + " }"
        data = gh_graphql(query).get("data", {})
        for i, slug in enumerate(batch):
            info = data.get(f"r{i}")
            if info:
                meta[slug] = {
                    "stars": info["stargazerCount"],
                    "pushed": info["pushedAt"],
                    "archived": info["isArchived"],
                }
    return meta


def age_label(iso_date: str) -> str:
    pushed = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
    delta = datetime.now(timezone.utc) - pushed
    days = delta.days
    if days <= 7:
        return ""
    if days <= 30:
        return f"{days}d ago"
    months = days // 30
    if months < 12:
        return f"{months}mo ago"
    return f"{days // 365}y ago"


def main():
    text = README.read_text()
    lines = text.split("\n")

    # Collect all repo slugs
    slugs = set()
    for line in lines:
        m = REPO_PATTERN.search(line)
        if m:
            slug = m.group(1).rstrip(")")
            if slug.count("/") == 1:
                slugs.add(slug)

    print(f"Found {len(slugs)} repo slugs")
    meta = fetch_repo_meta(sorted(slugs))
    print(f"Fetched metadata for {len(meta)} repos")

    updated = 0
    new_lines = []
    for line in lines:
        m = REPO_PATTERN.search(line)
        if m:
            slug = m.group(1).rstrip(")")
            info = meta.get(slug)
            if info:
                stars = info["stars"]
                # Remove existing star annotation
                line = STAR_PATTERN.sub("", line)
                # Add star count if >= threshold
                if stars >= STAR_THRESHOLD:
                    # Find the end of the line to append
                    line = line.rstrip()
                    # Remove trailing pipe cell for table rows
                    if line.endswith("|"):
                        # Table row — insert before last |
                        line = line.rstrip("|").rstrip() + f" · ★{stars} |"
                    else:
                        line = line + f" · ★{stars}"
                    updated += 1
        new_lines.append(line)

    new_text = "\n".join(new_lines)
    if new_text != text:
        README.write_text(new_text)
        print(f"Updated {updated} star counts")
    else:
        print("No changes needed")


if __name__ == "__main__":
    main()

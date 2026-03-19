#!/usr/bin/env python3
"""Update star counts in README.md from the GitHub API."""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

STAR_THRESHOLD = 5
README = Path(__file__).resolve().parent.parent / "README.md"
# Match github.com/owner/repo but NOT deeper paths like /releases, /discussions, etc.
REPO_PATTERN = re.compile(r"github\.com/([\w.\-]+/[\w.\-]+?)(?:\)|\s|/|$)")
STAR_SUFFIX = re.compile(r" · ★\d+")

# Known non-repo paths to skip
SKIP_SLUGS = {
    "ghostty-org/ghostty",  # upstream, not in our list format
    "orgs", "topics", "settings",
}


def gh_graphql(query: str) -> dict:
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={query}"],
        capture_output=True, text=True, timeout=30,
    )
    if result.returncode != 0:
        return {"errors": result.stderr}
    return json.loads(result.stdout)


def fetch_batch(slugs: list[str]) -> dict[str, dict]:
    """Fetch stars for a batch. On failure, retry one-by-one."""
    fragments = []
    for i, slug in enumerate(slugs):
        owner, name = slug.split("/", 1)
        fragments.append(
            f'r{i}: repository(owner: "{owner}", name: "{name}") '
            f"{{ stargazerCount pushedAt isArchived }}"
        )
    query = "{ " + " ".join(fragments) + " }"
    resp = gh_graphql(query)

    if "errors" in resp and "data" not in resp:
        # Batch failed — retry individually
        print(f"  Batch of {len(slugs)} failed, retrying individually...")
        results = {}
        for slug in slugs:
            owner, name = slug.split("/", 1)
            q = f'{{ repo: repository(owner: "{owner}", name: "{name}") {{ stargazerCount pushedAt isArchived }} }}'
            r = gh_graphql(q)
            info = (r.get("data") or {}).get("repo")
            if info:
                results[slug] = {
                    "stars": info["stargazerCount"],
                    "pushed": info["pushedAt"],
                    "archived": info["isArchived"],
                }
            else:
                print(f"  Skipping {slug}: not found or API error")
        return results

    data = resp.get("data", {})
    results = {}
    for i, slug in enumerate(slugs):
        info = data.get(f"r{i}")
        if info:
            results[slug] = {
                "stars": info["stargazerCount"],
                "pushed": info["pushedAt"],
                "archived": info["isArchived"],
            }
    return results


def main():
    text = README.read_text()
    lines = text.split("\n")

    # Collect all unique repo slugs from entry lines (lines starting with | [ or - [)
    slugs = set()
    for line in lines:
        if not (line.strip().startswith("| [") or line.strip().startswith("- [")):
            continue
        for m in REPO_PATTERN.finditer(line):
            slug = m.group(1)
            if slug.count("/") == 1 and slug not in SKIP_SLUGS:
                slugs.add(slug)

    slug_list = sorted(slugs)
    print(f"Found {len(slug_list)} repo slugs")

    # Fetch in batches of 50 (conservative to avoid GraphQL limits)
    meta = {}
    for i in range(0, len(slug_list), 50):
        batch = slug_list[i:i + 50]
        print(f"  Fetching batch {i // 50 + 1} ({len(batch)} repos)...")
        meta.update(fetch_batch(batch))

    print(f"Fetched metadata for {len(meta)} repos")

    # Update star counts in README
    updated = 0
    new_lines = []
    for line in lines:
        if line.strip().startswith("| [") or line.strip().startswith("- ["):
            for m in REPO_PATTERN.finditer(line):
                slug = m.group(1)
                info = meta.get(slug)
                if info:
                    stars = info["stars"]
                    # Remove existing star annotation
                    line = STAR_SUFFIX.sub("", line)
                    if stars >= STAR_THRESHOLD:
                        line = line.rstrip()
                        # For table rows ending with |
                        if line.endswith("|"):
                            # Insert before the last |
                            line = line[:-1].rstrip() + f" · ★{stars} |"
                        else:
                            line = line + f" · ★{stars}"
                        updated += 1
                    break  # Only process first repo link per line
        new_lines.append(line)

    new_text = "\n".join(new_lines)
    if new_text != text:
        README.write_text(new_text)
        print(f"Updated {updated} star counts in README.md")
    else:
        print("No changes needed")


if __name__ == "__main__":
    main()

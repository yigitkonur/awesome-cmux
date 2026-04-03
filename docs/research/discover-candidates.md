# Discover Candidates

## Why this exists

Direct repo search misses some valid cmux integrations. Many projects only expose `CMUX_WORKSPACE_ID`, `CMUX_SURFACE_ID`, `CMUX_SOCKET_PATH`, or related hooks inside code and repo files, so they never show up in a name- or description-based search.

This script is a discovery aid, not an auto-add tool. It helps maintainers find repos worth reviewing, then leaves the final inclusion decision to a human.

## How to run it

Use `python3` in this environment:

```bash
rtk python3 scripts/discover_candidates.py --limit-per-signal 20 --minimum-candidate-score 8 --format markdown
```

Useful flags:

- `--limit-per-signal` controls how many code-search hits each signal may return.
- `--minimum-candidate-score` raises or lowers the threshold for `candidate` status.
- `--include-listed` keeps repos already in `README.md` in the report.
- `--include-excluded` keeps archived or explicitly excluded repos in the report.
- `--format json` returns machine-readable output instead of the Markdown table.

## How to read the output

Each row includes a status, score, stars, language, last update, suggested section, and evidence summary.

- `candidate` means the repo has strong evidence and passed the basic inclusion checks.
- `review` means the repo is interesting, but the evidence is weaker or noisier and needs manual inspection.
- `listed` means the repo is already present in `README.md`.
- `excluded` means the repo was filtered out because it is archived, missing a root README, or explicitly out of scope.

The score is only a ranking signal. Treat it as triage, not permission to add an entry.

`suggested section` is advisory. Use it as a starting point, then confirm the final section against the existing layout rules in `CONTRIBUTING.md`.

## What still needs human review

Before editing `README.md`, verify all of the following:

1. The repo is public and has a usable root README.
2. It genuinely uses a cmux API, env var, CLI command, or socket integration.
3. The repo is not already listed.
4. The proposed section is correct.
5. The one-line description follows the table format and tone in `CONTRIBUTING.md`.

If a repo only reaches `review`, inspect it manually before deciding whether it belongs in the list.

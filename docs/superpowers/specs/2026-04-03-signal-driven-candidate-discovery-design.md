# Signal-Driven Candidate Discovery Design

## Context

`awesome-cmux` already has a strong inclusion rule in [CONTRIBUTING.md](../../../CONTRIBUTING.md): valid entries must use a cmux API such as `CMUX_SOCKET_PATH`, `CMUX_WORKSPACE_ID`, `CMUX_SURFACE_ID`, the `cmux` CLI, or the socket protocol. The repo also already automates star-count refreshes with [`scripts/update_stars.py`](../../../scripts/update_stars.py), but candidate discovery itself is still manual and search-query-driven.

That creates a predictable blind spot: many valid repos do not advertise themselves with `cmux` in the repository name or description. They surface only in code, AGENTS/CLAUDE docs, plugin files, or README snippets through cmux-specific env vars and integration hooks. Direct repo search is still useful, but it is not sufficient on its own.

The goal of this design is to make candidate research reproducible, evidence-based, and faster to review without weakening the curated quality bar.

## Goals

- Discover likely cmux integrations by searching for cmux-specific evidence inside repository contents, not just repository metadata.
- Produce a ranked shortlist that separates likely candidates from noise, duplicates, and invalid repos.
- Reuse the repo's existing inclusion rules as machine-checkable filters where possible.
- Keep the workflow lightweight: local script, no third-party Python dependencies, compatible with existing `gh`-based maintenance.
- Preserve human review as the final gate before anything is added to the README.

## Non-Goals

- No fully automatic README mutation from discovery results.
- No scheduled candidate-addition bot.
- No attempt to perfectly classify every repo without review.
- No broad refactor of the existing star-update script or CI unless required by the implementation.

## Autonomous Five-Perspective Review

### 1. Maintainer perspective

The maintainer problem is operational, not theoretical: "show me net-new repos worth checking." The tool therefore must understand the current README, flag already-listed repos, and emit a shortlist that is easy to scan and manually validate.

### 2. Search-quality perspective

The strongest signals are the cmux env vars because they are specific to the target project and appear in real integrations even when the repo branding does not. Repo-name search should remain a complement, but signal-driven code search should become the backbone.

### 3. False-positive perspective

Not every hit is good evidence. Vendored skills, copied docs, generated artifacts, empty repos, archived repos, and unrelated `cmux` uses all create noise. The design needs confidence weights, exclusion rules, and explicit candidate statuses instead of pretending every search hit is equal.

### 4. Tooling perspective

The repo is intentionally small and already uses Python plus `gh`. The new workflow should follow that precedent: one focused Python script, stdlib only, shell-friendly output, and tests around pure logic.

### 5. Quality-control perspective

The tool must not merely "find repos." It must explain why each repo appeared. That means storing evidence hits, sample paths, and a deterministic score so reviewers can audit the shortlist instead of trusting a black box.

## Options Considered

### Option A: Document-only research playbook

Write a maintainer guide that says "search these env vars manually, then inspect the repos."

Pros:
- Fastest to ship
- No code to maintain

Cons:
- Still manual, inconsistent, and easy to drift
- No dedupe, scoring, or already-listed detection
- Does not materially improve repeatability

### Option B: Local signal-driven discovery script

Add a Python script that runs GitHub code searches for cmux-specific signals, dedupes repos, enriches them with metadata, scores confidence, and emits a candidate report.

Pros:
- Repeatable and auditable
- Fits current repo tooling
- Strongly improves recall while keeping human review

Cons:
- Requires some heuristic tuning
- Needs tests and maintenance

### Option C: Scheduled candidate-research pipeline

Build Option B plus a GitHub Actions workflow that periodically generates candidate reports or issues.

Pros:
- Maximum automation
- Good for ongoing discovery

Cons:
- Higher maintenance and noise risk
- Premature before the discovery heuristics are proven

## Recommendation

Adopt **Option B** now. It delivers the main value with low operational risk and leaves room to add scheduled automation later if the signal quality holds up in practice.

## Chosen Design

### Overview

Add a new script, `scripts/discover_candidates.py`, that searches GitHub code for cmux-specific evidence signals, aggregates repositories across those searches, enriches each repository with metadata, evaluates each repository against basic inclusion checks, and prints a ranked shortlist for manual review.

The tool is intentionally assistive, not authoritative. It narrows the research surface area and shows its work.

### Inputs

- The current `README.md`, used to mark repos already present in the awesome list.
- A built-in set of evidence signals and weights.
- `gh` authentication from the current shell environment.

### Evidence Signals

Signals are grouped by confidence:

- **High-confidence env vars**
  - `CMUX_WORKSPACE_ID`
  - `CMUX_SURFACE_ID`
  - `CMUX_SOCKET_PATH`
- **Medium-confidence upstream references**
  - `github.com/manaflow-ai/cmux`
  - `cmux.dev`
- **Lower-confidence CLI phrases**
  - `cmux browser`
  - `cmux notify`
  - `cmux read-screen`
  - `cmux new-workspace`

The first implementation should prioritize env vars and upstream references. CLI phrases are useful, but noisier, so they should carry less weight and never outrank env-var hits on their own.

### Search Strategy

For each signal, run `gh search code` with `--match file` and a configurable per-signal limit. Capture:

- repository name
- matching path
- signal responsible for the hit

Then:

- dedupe by repository
- count matched signals
- retain a bounded list of sample paths per repository
- compute an evidence score from weighted signal hits

The tool should stop at deterministic ceilings rather than open-ended crawling. The goal is shortlist quality, not exhaustive indexing.

### Metadata Enrichment

After dedupe, fetch repository metadata in batches using the GitHub GraphQL API:

- description
- primary language
- stargazer count
- last pushed date
- archived state

Also check whether the repository has a root README, because README presence is a hard inclusion rule for this list.

### Candidate Status Model

Each discovered repo should be assigned one status:

- `listed` — already present in `README.md`
- `candidate` — new repo, has README, not archived, no exclusion triggered
- `review` — new repo but needs manual inspection because signals are weak or noisy
- `excluded` — empty, no README, archived, or matched an explicit exclusion rule

The first version should be conservative: uncertain repos go to `review`, not `candidate`.

### Exclusions and Noise Controls

The tool should support deterministic exclusions for:

- the awesome repo itself
- upstream repos that are sources or references rather than candidate entries
- explicit unrelated slugs already known to be outside scope
- generated or clearly vendored paths that should reduce confidence

Path patterns should not blindly discard a repo, but they can lower confidence. For example, a hit only inside copied skill assets is weaker than a hit in active source or README files.

### Suggested Section Heuristics

The tool should emit a `suggested_section` hint for manual use. This is advisory only.

Initial heuristics can map obvious patterns:

- `pi` / `pi-cmux` -> `By Agent > Pi`
- `opencode` -> `By Agent > OpenCode`
- `copilot` / `amp` -> `By Agent > Copilot & Amp`
- `mcp` -> `By Use Case > MCP Servers`
- `worktree` / `workspace provider` -> `By Use Case > Workspace & Worktrees`
- `restore`, `resurrect`, `remote`, `companion`, `context`, `mirror` -> `By Use Case > Monitor & Restore Sessions` or `Remote & Mobile`
- `browser`, `preview`, `diff`, `hub` -> `By Use Case > Browser Pane`
- `skill` plus Claude-oriented evidence -> `By Agent > Claude Code > Skills`

If no heuristic is strong enough, the field should be blank rather than guessed.

### Outputs

The tool should support:

- **Markdown table output** for maintainers to scan quickly
- **JSON output** for deeper inspection or later automation

Each row should include:

- repo
- status
- score
- stars
- language
- updated date
- suggested section
- evidence summary

The default console view should prioritize net-new `candidate` and `review` repos, with `listed` and `excluded` repos available on demand.

## Error Handling

- Missing `gh` auth should fail fast with a clear message.
- Individual search or metadata failures should be recorded per signal or per repo without crashing the whole run when possible.
- Empty results for one signal are not fatal.
- Rate limiting should be handled pragmatically: bounded query counts, batched metadata fetches, and small sleeps only if necessary.

## Testing Strategy

Add unit tests for pure logic:

- parsing existing README slugs
- evidence scoring
- status classification
- section suggestion heuristics
- path-based confidence adjustments

Subprocess boundaries should be isolated behind helper functions so tests can inject fixtures without calling GitHub.

## Documentation

Add a maintainer-facing workflow document describing:

- why env-var discovery exists
- how to run the tool
- how to read the output
- what still requires manual review before README changes

`CONTRIBUTING.md` should point maintainers to the discovery tool as the preferred starting point for finding new candidates.

## Verification

The implementation will be considered correct when:

- the tool runs successfully against authenticated GitHub search
- it surfaces repos already known to be valid cmux integrations from env-var evidence
- it clearly marks already-listed repos versus net-new repos
- it excludes or downgrades obviously invalid results such as empty repos or non-candidate references
- unit tests cover the pure decision logic

## Implementation Boundary

This design intentionally stops short of automatic README edits or scheduled candidate ingestion. If the discovery results prove high-signal over time, a later design can add a manual GitHub Actions report workflow on top of the same core logic.

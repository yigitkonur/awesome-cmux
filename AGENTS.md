# AGENTS.md

Instructions for AI agents working on this repository. Read this file completely before making any changes.

## What This Repo Is

A curated, opinionated awesome-list for the cmux ecosystem (manaflow-ai/cmux) — the Ghostty-based macOS terminal for AI coding agents. 120+ community projects, organized by feature dimensions with matrix/tag-based cross-referencing.

## Repository Structure

```
README.md                             # The awesome-list (primary deliverable)
AGENTS.md                             # This file — agent instructions
CONTRIBUTING.md                       # Human contributor guidelines
LICENSE                               # MIT
docs/
  sidebar-integration-api.md          # Full sidebar protocol reference (V1 text + V2 JSON-RPC)
  applescript/                        # 10-part AppleScript automation guide
scripts/
  update_stars.py                     # GitHub Actions star-count updater
.github/workflows/
  update-stars.yml                    # Daily star-count CI
```

## README Design Decisions

These decisions are final. Do not deviate without explicit user approval.

### Audience
- **Primary**: End users who installed cmux and want to find plugins for their agent
- **Secondary**: Plugin developers who want to build new integrations

### Tone
- Opinionated guide — editorial intros, recommended picks, not a flat dump
- Each feature section opens with 2-3 sentences explaining what the feature is and why it matters
- "Recommended" picks called out with `>` blockquotes where appropriate

### Structure (Approach B — Feature Dimensions)
```
Hero section (what is cmux, ecosystem stats)
Quick Start (brew install, resource links)
"I want to..." navigator table (14 goals)
Feature Dimensions (PRIMARY navigation):
  1. Sidebar & Status Pills
  2. Progress Bars & Estimation
  3. Sidebar Logs & Activity Feed
  4. Desktop Notifications
  5. Multi-Agent Orchestration
  6. Browser Automation
  7. Worktrees & Workspace Management
  8. Monitoring & Session Restore
  9. Remote & Mobile Access
  10. Themes, Layouts & Config
By Agent (SECONDARY navigation):
  - Claude Code (Hooks/Sidebar, Skills, Orchestration/Worktrees, Session Restore, Layout/Config)
  - Pi
  - OpenCode
  - Copilot & Amp
  - Multi-Agent / Agnostic
Cross-Platform Ports (Windows, Linux)
Alternatives (tmux-based, other terminals, forks)
Build Your Own Plugin (links to sidebar-integration-api.md)
Reference (Build & Distribution, Upstream, Ghostty Config, Automation Docs, Community, Articles)
Archived
Contributing
License
```

### Matrix/Tag System
- Repos appear in **every feature dimension section** they're relevant to
- A repo touching sidebar + notifications + progress appears in all three sections
- This duplication is intentional — browse by the feature you need, not by where someone filed it
- The "By Agent" section is a secondary cross-reference, not the primary navigation

### Within Each Feature Section
- Repos are **clustered by agent**: Claude Code first, then Pi, OpenCode, Copilot, Amp, Multi/Other
- Bold separator rows mark each cluster: `| **Claude Code** | | | |`
- Within each agent cluster, repos **sort by star count descending** (★477 → ★228 → unstarred)
- Within same star tier, sort by feature richness

### Description Standards
- **30-50 words** per description, no more, no less
- **Start with a verb** (Wire, Push, Deliver, Bridge, Teach, Expose, Fire, etc.)
- **Highlight differentiators** between similar plugins targeting the same agent:
  - Use contrast phrases: "unlike X which...", "focuses specifically on...", "adds Y on top of..."
  - If 6 Pi notification plugins exist, each description must explain what makes THAT one unique
- **No superlatives** (best, most, pioneering, first)
- **No marketing language** — neutral, technical tone
- Consistent sentence structure across all entries

### Table Formats

Feature dimension sections:
```
| Repo | Agent | Description | Lang |
```

By Agent sections:
```
| Repo | Tags | Description | Lang |
```

Tags use inline code: `` `sidebar` `notify` `progress` ``

Star counts: `★N` suffix in Lang column for repos with 5+ stars.

### What NOT to Do
- Do not flatten back to a by-agent-only structure
- Do not remove the matrix/tag duplication — it's the core design
- Do not add repos without placing them in every relevant feature section
- Do not write descriptions longer than 50 words or shorter than 30
- Do not skip the editorial intro at the top of each feature section
- Do not add internal/private docs to the `docs/` directory (the superpowers/ incident)
- Do not change the Ghostty config block — it stays inline in a `<details>` at the bottom

## Research Workflow — Finding New Repos

When tasked with discovering new repos to add, follow this process:

### Step 1: Search Sources
Use multiple search vectors in parallel:
- `gh api search/repositories` with keywords: `cmux`, `cmux plugin`, `cmux sidebar`, `cmux-claude`, `pi-cmux`, `opencode-cmux`
- Web search: `"CMUX_SOCKET_PATH" site:github.com`, `"CMUX_WORKSPACE_ID" site:github.com`
- Reddit: search r/ClaudeCode, r/ClaudeAI for "cmux" mentions
- Check GitHub topics: `cmux`, `claude-code`, `ai-terminal`
- Monitor the awesome-cmux discussions/issues for community submissions

### Step 2: Evaluate Each Candidate
For each repo found:
1. Fetch the README: `gh api repos/OWNER/REPO/readme --jq '.content' | base64 -d`
2. Check stars and language: `gh api repos/OWNER/REPO --jq '.stargazers_count, .language'`
3. Verify it uses a cmux API (`CMUX_SOCKET_PATH`, `CMUX_WORKSPACE_ID`, `cmux` CLI, or socket protocol)
4. Reject if: empty README, no cmux integration, pure fork with no unique value, deleted/archived

### Step 3: Classify
Determine for each repo:
- **Agent**: Claude Code / Pi / OpenCode / Copilot / Amp / Multi / None
- **Tags**: from the approved set: `sidebar`, `progress`, `logs`, `notify`, `orchestrate`, `browser`, `worktree`, `monitor`, `layout`, `skill`, `mcp`, `config`, `port`
- **Feature sections**: which of the 10 dimensions it belongs in (can be multiple)

### Step 4: Write the Description
- Read the README thoroughly (first 100 lines minimum)
- Write a 30-50 word description starting with a verb
- Compare against existing repos in the same agent cluster — explicitly differentiate
- If the repo is similar to an existing one, the description MUST explain what makes it unique

### Step 5: Place in README
- Add to every relevant feature dimension section (1-10)
- Add to the correct By Agent section
- Insert in the right position within its agent cluster (by star count)
- Add bold agent separator row if starting a new cluster

### Step 6: Batch Approach
When processing many repos at once:
- Split into batches of ~20
- Spawn parallel agents, each batch fetching READMEs and producing standardized summaries
- Merge results and cross-reference for completeness
- Verify every repo appears in at least one feature section AND its agent section

## Editing the README

### Adding a Single Repo
1. Read the repo's README
2. Write the standardized description
3. Insert into each relevant feature section at the correct position
4. Insert into the By Agent section
5. Commit with message: `docs: add OWNER/REPO to awesome-cmux`

### Updating Descriptions
If rewriting descriptions across the board:
1. Spawn parallel agents — one per feature section
2. Each agent clusters by agent, sorts by stars, rewrites descriptions
3. Each agent returns its optimized section
4. Assemble the full README from header + optimized sections + footer
5. Commit with descriptive message

### Removing a Repo
1. Remove from ALL feature sections and the By Agent section
2. If deleted/archived, move to the Archived section at the bottom
3. Commit with message: `docs: remove OWNER/REPO (reason)`

## Tag Vocabulary

Only use these tags. Do not invent new ones.

| Tag | Meaning |
|-----|---------|
| `sidebar` | Updates cmux sidebar status pills, metadata, or visual elements |
| `progress` | Implements or controls progress bars in the sidebar |
| `logs` | Writes to the sidebar log/activity feed |
| `notify` | Sends desktop notifications via `cmux notify`, OSC 777, or JSON-RPC |
| `orchestrate` | Spawns, monitors, or coordinates multiple agents |
| `browser` | Controls cmux's embedded WebKit browser pane |
| `worktree` | Manages git worktrees with cmux workspace integration |
| `monitor` | Observes agent state across workspaces (dashboards, restore, snapshots) |
| `layout` | Creates or manages pane splits, workspace arrangements, or project launchers |
| `skill` | A reference/skill document that teaches an agent how to use cmux |
| `mcp` | Exposes cmux functionality as MCP tools |
| `config` | Themes, dotfiles, Ghostty config, Homebrew taps, or development conventions |
| `port` | Windows or Linux port of the cmux application |

## Sidebar Integration API Doc

The `docs/sidebar-integration-api.md` file is a comprehensive protocol reference derived from reverse-engineering 12 production integrations. It covers:
- V1 text protocol (status pills, progress, logs, metadata, agent PID)
- V2 JSON-RPC protocol (notifications, browser, workspace queries)
- 5 progress estimation algorithms with code
- Status priority system
- State management patterns
- Complete working examples (shell + TypeScript)

When updating this doc, verify claims against actual plugin source code — do not guess at protocol details.

## CI / Automation

- `scripts/update_stars.py` + `.github/workflows/update-stars.yml` update star counts daily
- Star counts in the README use `★N` format, only shown for repos with 5+ stars
- The CI reads repo URLs from the README, fetches current counts, and commits updates

## Never

- Never add internal planning docs, specs, or brainstorming artifacts to this repo
- Never change the README structure without explicit user approval
- Never write descriptions that don't start with a verb
- Never add a repo without verifying it actually uses a cmux API
- Never skip the matrix placement — every repo goes in feature sections AND agent section
- Never use emojis in section headers (tasteful inline use in descriptions is OK)
- Never commit secrets, API keys, or personal data

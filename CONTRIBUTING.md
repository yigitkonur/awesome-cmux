# Contributing to Awesome cmux

## Inclusion Criteria

Before opening a PR, verify your entry meets **all three**:

1. **Public repo** with a README
2. **Uses a cmux API** — `CMUX_SOCKET_PATH`, `CMUX_WORKSPACE_ID`, `CMUX_SURFACE_ID`, the `cmux` CLI, or the Unix socket protocol
3. **Themes/configs** must include at least one cmux-specific feature (not just a generic Ghostty config)

## Exclusion Criteria

- Unrelated `cmux` projects (e.g., the Go connection multiplexer by soheilhy)
- Empty repos, abandoned forks with no unique value, or spam
- Repos that mention cmux only in comments or acknowledgments

## Entry Format

Feature dimension sections use:

```md
| [owner/repo](url) | Agent | Description starting with a verb, 30-50 words | Lang · ★N |
```

By Agent sections use:

```md
| [owner/repo](url) | `tag1` `tag2` | Description starting with a verb, 30-50 words | Lang · ★N |
```

## Description Rules

| Rule | Detail |
|------|--------|
| Length | 30-50 words. No exceptions. |
| Start with a verb | Wire, Push, Deliver, Teach, Expose, Bridge, Fire, etc. |
| Differentiate | If similar plugins exist for the same agent, explain what makes yours unique |
| No superlatives | No "best", "most complete", "pioneering", "first" |
| Stars 5+ only | Format: `★N` in the Lang column. Omit for repos under 5 stars. Updated daily by CI. |
| No API enumerations | Don't list `execFileSync`, `surface.send_text` — that belongs in the linked repo |
| No nationality labels | Use "Docs in Korean" if language matters, never "Korean-authored" |

## Tags

Use 1-4 tags from this approved set:

`sidebar` `progress` `logs` `notify` `orchestrate` `browser` `worktree` `monitor` `layout` `skill` `mcp` `config` `port`

See [AGENTS.md](./AGENTS.md) for full tag definitions.

## Section Placement

The README uses a **matrix/tag system** — repos appear in every section they're relevant to. You must place your entry in:

1. **Every relevant feature dimension section** (1-10)
2. **The correct By Agent section**

### Feature Dimensions

| # | Section | What belongs here |
|---|---------|------------------|
| 1 | Sidebar & Status Pills | Anything that writes to the cmux sidebar (status pills, metadata, visual elements) |
| 2 | Progress Bars & Estimation | Anything that drives the sidebar progress bar |
| 3 | Sidebar Logs & Activity Feed | Anything that writes log entries to the sidebar feed |
| 4 | Desktop Notifications | Anything that fires `cmux notify`, OSC 777, or JSON-RPC notifications |
| 5 | Multi-Agent Orchestration | Frameworks, MCP servers, and skills for running multiple agents |
| 6 | Browser Automation | Anything controlling cmux's embedded WebKit browser pane |
| 7 | Worktrees & Workspace Management | Git worktree integration, workspace creation, project launchers |
| 8 | Monitoring & Session Restore | Dashboards, session snapshots, restore tools, status scrapers |
| 9 | Remote & Mobile Access | PWA bridges, mobile apps, SSH mirroring, remote terminal tools |
| 10 | Themes, Layouts & Config | Pane layouts, themes, dotfiles, Homebrew taps, Raycast extensions |

### By Agent Sections

| Agent | Section |
|-------|---------|
| Claude Code | By Agent > Claude Code (subsections: Hooks & Sidebar, Skills, Orchestration & Worktrees, Session Restore, Layout & Config) |
| Pi | By Agent > Pi |
| OpenCode | By Agent > OpenCode |
| Copilot / Amp | By Agent > Copilot & Amp |
| Multi-agent or agnostic | By Agent > Multi-Agent / Agnostic |

### Ordering Within Sections

1. Repos are **grouped by agent** (Claude Code, Pi, OpenCode, Copilot, Amp, Multi/Other)
2. Bold separator rows mark each group: `| **Claude Code** | | | |`
3. Within each group, **sort by star count descending**
4. Within same star tier, sort by feature richness

### Other Sections

| Type | Section |
|------|---------|
| Windows/Linux port of cmux | Cross-Platform Ports |
| tmux-based wrapper | Alternatives > tmux-Based |
| Other terminal emulator | Alternatives > Other Terminals & Workspaces |
| Fork of cmux | Alternatives > Forks |
| Deleted/inaccessible repo | Archived |
| Build tools, proxies, Homebrew taps | Reference > Build & Distribution |

## Pull Request Checklist

- [ ] Link opens successfully and repo has a README
- [ ] Repo actually uses a cmux API (not just mentioning cmux)
- [ ] Description is 30-50 words, starts with a verb, no superlatives
- [ ] If similar repos exist for same agent, description highlights what makes this one unique
- [ ] Entry placed in every relevant feature dimension section (1-10)
- [ ] Entry placed in the correct By Agent section
- [ ] Correctly positioned within its agent cluster (sorted by star count)
- [ ] Tags are from the approved vocabulary (1-4 tags)
- [ ] Star count included if 5+ (CI will keep it updated after merge)
- [ ] No duplicate of an existing entry

## Star Counts

Star counts (`★N`) are updated daily by [GitHub Actions](.github/workflows/update-stars.yml). Include the current count when adding a new entry if 5+. CI keeps it current after merge.

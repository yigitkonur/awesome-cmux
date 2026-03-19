# Contributing to Awesome cmux

Thanks for helping improve this list.

## Inclusion criteria

A repo must meet **all three**:

1. **Public** with a README.
2. **Meaningfully uses a cmux API** — `CMUX_SOCKET_PATH`, `CMUX_WORKSPACE_ID`, `CMUX_SURFACE_ID`, the `cmux` CLI, or the Unix socket protocol.
3. Themes and configs must include at least one **cmux-specific feature** (not just a generic Ghostty config).

## Exclusion criteria

- Unrelated `cmux` projects (e.g., the Go connection multiplexer by soheilhy).
- Empty repos, abandoned forks with no unique value, or AI-generated spam.
- Dead links or repos that mention cmux only in passing (acknowledgments, comments).

## Entry format

Every entry follows this template:

```md
- [owner/repo](https://github.com/owner/repo) — [cmux verb] to [user value]. [One differentiating detail]. Lang · ★N
```

**Rules:**

| Rule | Example |
|------|---------|
| Lead with a cmux verb | "Opens a browser split via…", "Hooks into lifecycle events to push…", "Spawns agents via `cmux new-split`…" |
| Max 2 sentences | One for what it does with cmux, one for a differentiating detail |
| Stars shown only for ≥5 stars | `TypeScript · ★155` — omit stars below 5 |
| Language tag at end | `TypeScript`, `Rust`, `Shell`, `Python`, etc. |
| No API call enumerations | Don't list `execFileSync`, `surface.send_text`, etc. — those belong in the linked repo's README |
| No nationality labels | Use "Docs in Korean" if the documentation language matters, never "Korean-authored" |
| No issue links in tables | Bug references go in the linked repo, not this list |

## Skills table

Skills (SKILL.md files for Claude Code) use a table format with focus tags:

```md
| Repo | Focus | What it teaches Claude | ★ |
|------|-------|----------------------|---|
| [owner/repo](url) | `browser` | One-line description | ★4 |
```

**Focus tags:** `browser`, `cli-ref`, `orchestration`, `workflow`, `layout`, `hooks`, `compat`

Sort rows by focus tag to group similar skills together.

## Section placement

| Type | Section |
|------|---------|
| Claude Code plugin/skill | Agent Plugins > Claude Code |
| Pi extension | Agent Plugins > Pi |
| OpenCode plugin | Agent Plugins > OpenCode |
| Copilot/Amp plugin | Agent Plugins > Copilot & Amp |
| Standalone tool/library | Tools > appropriate subsection |
| Windows/Linux port | Ports |
| tmux wrapper or alternative terminal | Alternatives |
| Theme, config, dotfile | Setup > Themes & Layouts |
| Homebrew tap, CI, proxy | Setup > Build & Distribution |

## Visual style

- `---` horizontal rules only between major groupings (after Agent Plugins, after Tools, after Ports, after Alternatives).
- No `---` between every subsection.
- Descriptions use plain text — no bold, no inline code for tool names (except cmux commands like `cmux new-split`).

## Pull request checklist

- [ ] Link opens successfully.
- [ ] Description follows the entry format above.
- [ ] Placed in the correct section.
- [ ] No duplicate of an existing entry.
- [ ] Stars count is current (if ≥5).
- [ ] Focus tag is correct (for skills table entries).

# Contributing to Awesome cmux

## Inclusion criteria

Before opening a PR, verify your entry meets **all three**:

1. **Public repo** with a README
2. **Uses a cmux API** — `CMUX_SOCKET_PATH`, `CMUX_WORKSPACE_ID`, `CMUX_SURFACE_ID`, the `cmux` CLI, or the Unix socket protocol
3. **Themes/configs** must include at least one cmux-specific feature (not just a generic Ghostty config)

## Exclusion criteria

- Unrelated `cmux` projects (e.g., the Go connection multiplexer by soheilhy)
- Empty repos, abandoned forks with no unique value, or spam
- Repos that mention cmux only in comments or acknowledgments

## Entry format

All entries use table format:

```md
| [owner/repo](url) | `tag` | One sentence, neutral, no superlatives | Lang · ★N |
```

**Rules:**

| Rule | Detail |
|------|--------|
| One sentence max | Describe what the tool does with cmux — not how great it is |
| No superlatives | No "best", "most complete", "pioneering", "first" |
| Stars ≥ 5 only | Format: `★N`. Omit for repos under 5 stars. Updated daily by CI |
| Tags | 1–2 from: `sidebar` `browser` `notify` `orchestrate` `worktree` `layout` `mcp` `monitor` `compat` |
| Language at end | `TypeScript`, `Rust`, `Shell`, etc. |
| No API enumerations | Don't list `execFileSync`, `surface.send_text` — that belongs in the linked repo |
| No nationality labels | Use "Docs in Korean" if language matters, never "Korean-authored" |

## Skill entries

Skills (SKILL.md files) use the skill table:

```md
| [owner/repo](url) | `focus-tag` | One-line: what it teaches Claude |
```

Focus tags: `browser`, `cli-ref`, `orchestration`, `workflow`, `layout`, `hooks`, `compat`

## Section placement

| Type | Section |
|------|---------|
| Claude Code plugin/skill | By Agent > Claude Code |
| Pi extension | By Agent > Pi |
| OpenCode plugin | By Agent > OpenCode |
| Copilot/Amp plugin | By Agent > Copilot & Amp |
| Standalone orchestration tool | By Use Case > Orchestrate Multiple Agents |
| MCP server | By Use Case > MCP Servers |
| Browser pane tool | By Use Case > Browser Pane |
| Worktree/workspace manager | By Use Case > Workspace & Worktrees |
| Session/monitoring tool | By Use Case > Monitor & Restore Sessions |
| Windows/Linux port | Ports |
| tmux wrapper or alternative | Alternatives |
| Theme, config, dotfile | Setup & Config > Themes & Layouts |
| Homebrew tap, CI, proxy | Setup & Config > Build & Distribution |

## Visual style

- `---` horizontal rules only between major groups (By Agent, By Use Case, Ports, Alternatives, Setup, Reference)
- All groups of 3+ entries use table format, not bullet lists
- No bold in table cells except section headers

## Star counts

Star counts (`★N`) are updated daily by [GitHub Actions](.github/workflows/update-stars.yml). When adding a new entry, include the current count if ≥ 5. CI will keep it current.

## Pull request checklist

- [ ] Link opens successfully
- [ ] Description follows the table format above
- [ ] Placed in the correct section
- [ ] No duplicate of an existing entry
- [ ] Tags are from the approved vocabulary
- [ ] No superlatives or marketing language

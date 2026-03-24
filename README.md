# Awesome cmux [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Last updated](https://img.shields.io/github/last-commit/yigitkonur/awesome-cmux?label=last%20updated)

> A curated list of resources for **[cmux](https://github.com/manaflow-ai/cmux)** — the Ghostty-based macOS terminal for coding agents. This list is for `manaflow-ai/cmux` only — for the Go connection multiplexer by soheilhy, see that repo directly. 100+ public repos use cmux's primitives: `CMUX_WORKSPACE_ID`, `CMUX_SURFACE_ID`, and `CMUX_SOCKET_PATH`.

| I want to... | Go to |
|---|---|
| Install cmux | [Getting Started](#getting-started) |
| Add cmux support to **Claude Code** | [Claude Code](#claude-code) |
| Add cmux support to **Pi / OpenCode / Copilot** | [Pi](#pi) · [OpenCode](#opencode) · [Copilot & Amp](#copilot--amp) |
| Orchestrate multiple agents | [Orchestration](#orchestrate-multiple-agents) |
| Run cmux on **Windows or Linux** | [Ports](#ports) |
| Browse tmux-based alternatives | [Alternatives](#alternatives) |

## Contents

- [Getting Started](#getting-started)
- [By Agent](#by-agent)
- [By Use Case](#by-use-case)
- [Ports](#ports)
- [Alternatives](#alternatives)
- [Setup & Config](#setup--config)
- [Reference](#reference)

## Getting Started

```sh
brew install --cask cmux          # stable
brew install --cask cmux-nightly  # nightly
```

| Resource | Link |
|----------|------|
| Website | [cmux.dev](https://www.cmux.dev/) |
| Source | [github.com/manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) |
| Downloads | [Stable DMG](https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg) · [Nightly DMG](https://github.com/manaflow-ai/cmux/releases/download/nightly/cmux-nightly-macos.dmg) |
| Docs | [Getting Started](https://www.cmux.dev/docs/getting-started) · [Concepts](https://www.cmux.dev/docs/concepts) · [Configuration](https://www.cmux.dev/docs/configuration) · [Shortcuts](https://www.cmux.dev/docs/keyboard-shortcuts) |
| API | [Reference](https://www.cmux.dev/docs/api) · [Browser](https://www.cmux.dev/docs/browser-automation) · [Notifications](https://www.cmux.dev/docs/notifications) |
| Blog | [Introducing cmux](https://www.cmux.dev/blog/introducing-cmux) · [Show HN](https://www.cmux.dev/blog/show-hn-launch) · [Zen of cmux](https://www.cmux.dev/blog/zen-of-cmux) |

---

## By Agent

### Claude Code

**Sidebar & Lifecycle Hooks**

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [HazAT/pi-config](https://github.com/HazAT/pi-config) | `sidebar` `notify` | Pushes agent status, model, tokens, and active tool to cmux sidebar on every lifecycle event | TypeScript · ★186 |
| [tslateman/cmux-claude-code](https://github.com/tslateman/cmux-claude-code) | `sidebar` `notify` | 6-hook plugin: emoji tool names, logarithmic progress bar, desktop notification on completion | Shell |
| [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) | `sidebar` `notify` | Auto-renames workspace tab to git repo name, notifies on completion, includes restraint rules | Shell |
| [blueraai/bluera-base](https://github.com/blueraai/bluera-base) | `hooks` | Skill package with 5 reference docs and benchmark evaluations for cmux task performance | — |
| [claude-studio/claude-studio](https://github.com/claude-studio/claude-studio) | `hooks` | Ships two cmux CLI reference docs as CLAUDE.md tool context for workspace and browser control | — |

**Skills**

| Repo | Focus | What it teaches Claude |
|------|-------|----------------------|
| [darkspock/cmux-skill](https://github.com/darkspock/cmux-skill) | `browser` | Full `cmux browser` surface: DOM, JS eval, cookies, tabs, dialogs, frames · ★5 |
| [hashangit/cmux-skill](https://github.com/hashangit/cmux-skill) | `browser` | Element refs via `snapshot --interactive`, notify decision matrix, auto-wired hooks |
| [hoonkim/cmux-skills-plugin](https://github.com/hoonkim/cmux-skills-plugin) | `browser` | Browser automation + pane control via `cmux tree`/`read-screen`/`send`. Docs in Korean |
| [Stealinglight/cmux-claude-code-skill](https://github.com/Stealinglight/cmux-claude-code-skill) | `cli-ref` | Three deep references (CLI, browser, shortcuts) with Python socket API examples |
| [mikecfisher/cmux-skill](https://github.com/mikecfisher/cmux-skill) | `cli-ref` | Full CLI taxonomy, documents `capture-pane` tmux alias and `CMUX_SOCKET_PASSWORD` |
| [mangledmonkey/cmux-skills](https://github.com/mangledmonkey/cmux-skills) | `cli-ref` | Auto-syncing 4-skill bundle from upstream via weekly GitHub Actions |
| [bocktae80/cmux-pilot](https://github.com/bocktae80/cmux-pilot) | `layout` | `/cmux-ws` commands to save/restore workspace layouts with cron autosave. Docs in Korean |
| [jhta/cmux-skill](https://github.com/jhta/cmux-skill) | `workflow` | Neovim + git diff patterns: open files, delta diffs, run tests in adjacent panes |
| [halindrome/cmux-tmux-mapping-for-cc](https://github.com/halindrome/cmux-tmux-mapping-for-cc) | `compat` | tmux abstraction layer routing to cmux or tmux by environment. WIP |

### Pi

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [espennilsen/pi](https://github.com/espennilsen/pi) | `sidebar` `browser` | Built-in `@e9n/pi-cmux`: socket JSON-RPC, 7 LLM tools for workspace and browser | TypeScript · ★57 |
| [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) | `sidebar` `notify` | Persistent socket client, 4 live sidebar pills (model, state, thinking, tokens) | TypeScript · ★13 |
| [javiermolinar/pi-cmux](https://github.com/javiermolinar/pi-cmux) | `layout` `notify` | 12+ slash commands: splits, zoxide jumps, worktree handoffs, PR review panes | TypeScript · ★5 |
| [joelhooks/pi-cmux](https://github.com/joelhooks/pi-cmux) | `sidebar` `notify` | 3s sidebar heartbeat, AI session naming via Haiku, worker mode for subagents | TypeScript · ★7 |
| [simonjohansson/pi-cmux](https://github.com/simonjohansson/pi-cmux) | `sidebar` | Single `cmux_cli` tool passing any argv to cmux. Configurable via `CMUX_CLI_PATH` | TypeScript |
| [storelayer/pi-cmux-browser](https://github.com/storelayer/pi-cmux-browser) | `browser` | Full `cmux browser` CLI (36+ actions) with persistent surface tracking | JavaScript |

### OpenCode

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [kdcokenny/ocx](https://github.com/kdcokenny/ocx) | `sidebar` `notify` | Pushes status, progress, logs, flash triggers on every OpenCode lifecycle event | TypeScript · ★448 |
| [kdcokenny/opencode-notify](https://github.com/kdcokenny/opencode-notify) | `notify` | Routes OS notifications through `cmux notify` when workspace ID is set | TypeScript · ★109 |
| [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) | `sidebar` `notify` | Status pills, todo-driven progress, timeline logs, unread marks — scoped per workspace | TypeScript · ★19 |
| [Attamusc/opencode-cmux](https://github.com/Attamusc/opencode-cmux) | `sidebar` | Socket JSON-RPC (~1-2ms), render throttling, log rate limiting, subagent detection | TypeScript |
| [Joehoel/opencode-cmux](https://github.com/Joehoel/opencode-cmux) | `sidebar` `notify` | OpenCode plugin + Zsh integration polling Azure DevOps and Jira as sidebar pills | Shell |

### Copilot & Amp

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [Attamusc/copilot-cmux](https://github.com/Attamusc/copilot-cmux) | `sidebar` `notify` | Copilot CLI hooks to sidebar status/progress/notifications via socket JSON-RPC | TypeScript |
| [tadashi-aikawa/copilot-plugin-notify](https://github.com/tadashi-aikawa/copilot-plugin-notify) | `notify` | OSC 777 escape sequences from Copilot hooks — works with any OSC 777 terminal | Shell |
| [block/cmux-amp](https://github.com/block/cmux-amp) | `sidebar` | Official Block plugin: Amp events to sidebar pills with SF Symbol icons | TypeScript |

---

## By Use Case

### Orchestrate Multiple Agents

**Frameworks**

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [aannoo/hcom](https://github.com/aannoo/hcom) | `orchestrate` | Spawns workspaces via `cmux new-workspace`, one of 24 terminal backends | Rust · ★158 |
| [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) | `orchestrate` | Splits panes, relays tasks, polls `read-screen` for completion. cmux/tmux/zellij | TypeScript · ★108 |
| [dagster-io/erk](https://github.com/dagster-io/erk) | `orchestrate` `worktree` | Opens PRs in dedicated cmux workspaces via `cmux checkout`/`cmux teleport` | Python · ★76 |
| [burggraf/pi-teams](https://github.com/burggraf/pi-teams) | `orchestrate` | cmux `TerminalAdapter`: splits, liveness checks, workspace isolation | TypeScript · ★45 |
| [bjacobso/pimux](https://github.com/bjacobso/pimux) | `orchestrate` | cmux-mandatory Effect service: per-task workspaces, sidebar status state machine | TypeScript |
| [eduwass/cru](https://github.com/eduwass/cru) | `orchestrate` `sidebar` | 447-line cmux module, lifecycle phases with SF Symbols, progress-watcher. E2E tests | TypeScript |
| [rjwittams/flotilla](https://github.com/rjwittams/flotilla) | `orchestrate` `layout` | `CmuxWorkspaceManager` Rust trait: multi-pane YAML templates across all windows | Rust |

**Orchestration Skills**

| Repo | What it teaches Claude |
|------|----------------------|
| [ygrec-app/supreme-leader-skill](https://github.com/ygrec-app/supreme-leader-skill) | Splits a 2–8 worker grid, dispatches tasks, monitors via `read-screen` polling — never codes |
| [umitaltintas/cmux-agent-toolkit](https://github.com/umitaltintas/cmux-agent-toolkit) | Fan-out: spawn agents, synchronize via `wait-for`/`wait-for --signal` |
| [hummer98/cmux-team](https://github.com/hummer98/cmux-team) | Typed team slash commands (Researchers, Design, Impl, Test) as dedicated workspaces |
| [baixianger/claude-orchestration-in-cmux](https://github.com/baixianger/claude-orchestration-in-cmux) | Pane delegation via `cmux send`/`read-screen`, coordinated through worktrees |
| [Th3Sp3ct3R/cmux-claude-agents](https://github.com/Th3Sp3ct3R/cmux-claude-agents) | `PreToolUse` hook redirecting Agent calls to visible cmux panes |
| [ygrec-app/offload-task-skill](https://github.com/ygrec-app/offload-task-skill) | Split pane, launch `claude --dangerously-skip-permissions`, return to main session |

### MCP Servers

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) | `mcp` `orchestrate` | 81 tools: full hierarchy, agent grid launchers, bulk dispatch, session recovery | TypeScript |
| [EtanHey/cmuxlayer](https://github.com/EtanHey/cmuxlayer) | `mcp` | 20 tools via socket (~0.1ms) or CLI fallback. Agent lifecycle engine | TypeScript |
| [jasonraz/cmux-browser-mcp](https://github.com/jasonraz/cmux-browser-mcp) | `mcp` `browser` | 31 browser-only tools. Auto-tracks last-opened surface | JavaScript · ★5 |

### Browser Pane

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [azu/cmux-hub](https://github.com/azu/cmux-hub) | `browser` `sidebar` | Diff viewer in browser split, sends review comments back via cmux socket | TypeScript · ★13 |
| [gonzaloserrano/streamdeck-cmux](https://github.com/gonzaloserrano/streamdeck-cmux) | `sidebar` | Reads socket for live workspace status on Stream Deck buttons | TypeScript · ★6 |
| [monzou/mo-cmux](https://github.com/monzou/mo-cmux) | `browser` | Live-reload Markdown server in cmux browser split | Shell |
| [doublezz10/figure-viewer](https://github.com/doublezz10/figure-viewer) | `browser` | HTML figure gallery in cmux pane, auto-refreshes on new images | JavaScript |
| [RyoHirota68/cmux-pencil-preview](https://github.com/RyoHirota68/cmux-pencil-preview) | `browser` | `PostToolUse` hook: export PDF, reload cmux browser pane per design iteration | Shell |

### Workspace & Worktrees

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [kdcokenny/opencode-worktree](https://github.com/kdcokenny/opencode-worktree) | `worktree` | New cmux workspace per git worktree, detected via env vars | TypeScript · ★339 |
| [aschreifels/cwt](https://github.com/aschreifels/cwt) | `worktree` `sidebar` | Worktrees in cmux workspaces with splits, badges, bundled agent skills | Go |
| [bhandeland/fleet](https://github.com/bhandeland/fleet) | `worktree` `orchestrate` | Workspace per branch, sidebar badges, multi-agent team splits. Degrades without cmux | Shell |
| [tasuku43/kra](https://github.com/tasuku43/kra) | `worktree` | Persistent ticket → filesystem → cmux workspace mapping with auto-reconciliation | Go |
| [wwaIII/proj](https://github.com/wwaIII/proj) | `layout` | TUI project launcher opening named cmux workspaces with `[CC]` activity badges | Rust |

### Monitor & Restore Sessions

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [AtAFork/ghostty-claude-code-session-restore](https://github.com/AtAFork/ghostty-claude-code-session-restore) | `monitor` | Snapshots sessions every 2s, restores into correct cmux surfaces on relaunch | Python · ★21 |
| [owizdom/context-brdige-for-cmux](https://github.com/owizdom/context-brdige-for-cmux) | `monitor` | Polls socket, reads scrollback, stores in SQLite, auto-injects context handoff prompts | Go |
| [alaasdk/cmux-ctl](https://github.com/alaasdk/cmux-ctl) | `monitor` | Real-time TUI dashboard of all workspaces with agent send/stop shortcuts | Python |
| [taichiiwamoto-s/cmux-context](https://github.com/taichiiwamoto-s/cmux-context) | `monitor` | Scrapes Claude status bar from every workspace, renders context-fill dashboard | Shell |
| [ensarkovankaya/cmux-mirror](https://github.com/ensarkovankaya/cmux-mirror) | `monitor` | Mirrors remote cmux layout to local instance over SSH | Python |

### Launchers

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [stevenocchipinti/raycast-cmux](https://github.com/stevenocchipinti/raycast-cmux) | `layout` | Raycast commands for workspace switching, surface search, notification jump | TypeScript |

---

## Ports

### Windows

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [mkurman/cmux-windows](https://github.com/mkurman/cmux-windows) | — | WPF/ConPTY: sidebar, splits, OSC notifications, WebView2 browser, CLI. 5 releases | C# · ★24 |
| [TRINITXX/cmux-windows](https://github.com/TRINITXX/cmux-windows) | — | Fork of mkurman + Claude Code hooks, Zen mode, Dracula/One Dark themes | C# |
| [aasm3535/wmux](https://github.com/aasm3535/wmux) | — | WinUI 3 + xterm.js: sidebar, splits, OSC notifications, native Mica backdrop | C# |
| [shogotomita/cmux-win](https://github.com/shogotomita/cmux-win) | — | WPF/ConPTY under active development. 24 test files. Missing browser/persistence | C# |

### Linux

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [asermax/seemux](https://github.com/asermax/seemux) | — | Rust/GTK4, 30+ releases: tab groups, splits, Claude hooks, quake mode, plugin marketplace | Rust |
| [nice-bills/lmux](https://github.com/nice-bills/lmux) | — | Pure C, GTK4/VTE/WebKitGTK: browser split, D-Bus notifications, socket API | C |
| [anurag-arjun/cove](https://github.com/anurag-arjun/cove) | — | Ghostty GTK fork with vertical workspace sidebar, notification badges | Zig |

---

## Alternatives

### tmux-Based

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [craigsc/cmux](https://github.com/craigsc/cmux) | `worktree` | `cmux new <branch>` for isolated worktrees. Tab completion, merge/teardown | Shell · ★430 |
| [maedana/crmux](https://github.com/maedana/crmux) | `monitor` | Rust tmux sidebar: live status, model, context usage, permission alerts | Rust · ★19 |
| [wolffiex/cmux](https://github.com/wolffiex/cmux) | `layout` | Bun tmux manager (~22ms): popup carousel, 10 preset layouts, AI summaries | TypeScript |
| [theforager/cmux](https://github.com/theforager/cmux) | `monitor` | Interactive session selector with live status. Optimized for mobile SSH | Shell |
| [jeremyeder/sisi-cmux](https://github.com/jeremyeder/sisi-cmux) | `layout` | Auto-discovers projects, builds tmux workspace per project with Claude keybindings | TypeScript |

### Other

| Repo | Description | Lang |
|------|-------------|------|
| [danneu/danterm](https://github.com/danneu/danterm) | macOS terminal on libghostty: vertical tabs, tab groups, Claude hooks, Nix module | Swift |
| [Pollux-Studio/maxc](https://github.com/Pollux-Studio/maxc) | Tauri workspace: terminals + browser + agent orchestration via CLI and socket RPC | Rust |
| [Kaldy14/clui](https://github.com/Kaldy14/clui) | Electron: project-scoped Claude threads with xterm.js, git, LRU hibernation | TypeScript |
| [wrock/wezterm-agent-cards](https://github.com/wrock/wezterm-agent-cards) | WezTerm sidebar replicating cmux's status-card UX via curses and Claude hooks | Python |
| [davis7dotsh/my-term](https://github.com/davis7dotsh/my-term) | Native macOS prototype with Arc-style persistent sidebar, SwiftTerm | Swift |
| [ipdelete/cmux](https://github.com/ipdelete/cmux) | Electron workspace using Copilot CLI/SDK, Monaco editor, PTY terminals | TypeScript |

### Forks

- [llv22/cmux_forward](https://github.com/llv22/cmux_forward) — Adds working-directory restore for Bash sessions. One patch over upstream. Swift

<details>
<summary>Archived</summary>

- [adhyaay-karnwal/cmux](https://github.com/adhyaay-karnwal/cmux) — Abandoned fork with Docker isolation and multi-CLI support. TypeScript

</details>

---

## Setup & Config

### Themes & Layouts

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [jacobtellep/cmux-setup](https://github.com/jacobtellep/cmux-setup) | `layout` | 3-pane Conductor layout (Claude + lazygit + dev server) with dark-teal theme | Shell |
| [budah1987/cmux-script](https://github.com/budah1987/cmux-script) | `layout` | Interactive project picker: 3-pane layout with yazi + lazygit, auto-starts dev servers | Shell |
| [ctaho19/cmux-cursor-work-style](https://github.com/ctaho19/cmux-cursor-work-style) | `layout` | Cursor aesthetic: charcoal/blue theme, Berkeley Mono, sidebar tint, Claude status line | Shell |
| [rappdw/zen-term](https://github.com/rappdw/zen-term) | `layout` | MacBook-to-DGX via Mosh: three Zellij layouts, auto-starts Claude + `nvidia-smi` | Shell |
| [chrisliu298/ghostty-config](https://github.com/chrisliu298/ghostty-config) | — | GitHub Dark, Berkeley Mono 18pt, 128 MiB scrollback, cmux-ready keybinds | — |
| [jcyamacho/zdotfiles](https://github.com/jcyamacho/zdotfiles) | — | `cmux.zsh` plugin: Homebrew install, PATH symlink, `cmux-inside`/`cmux-ping` helpers | Zsh |
| [karlorz/dev-docs-cmux](https://github.com/karlorz/dev-docs-cmux) | — | LLM-optimized docs for cmux's tech stack from context7.com | Shell |

### Build & Distribution

| Repo | Description | Lang |
|------|-------------|------|
| [manaflow-ai/manaflow](https://github.com/manaflow-ai/manaflow) | Primary monorepo. Contains `cmux-proxy` and `cmux-env` Rust crates | TypeScript · ★974 |
| [webkaz/cmux-intel-builds](https://github.com/webkaz/cmux-intel-builds) | Builds unsigned Intel Mac x86_64 DMGs by polling releases every 6h | — |
| [lawrencecchen/cmux-proxy](https://github.com/lawrencecchen/cmux-proxy) | Reverse proxy routing to per-workspace loopback IPs. Optional LD_PRELOAD shim | Rust |
| [lawrencecchen/cmux-env](https://github.com/lawrencecchen/cmux-env) | Daemon sharing env vars across shells/projects. Bash/zsh/fish hooks, dotenv | Rust |
| [budah1987/homebrew-tools](https://github.com/budah1987/homebrew-tools) | Homebrew formula wrapping cmux + yazi + lazygit into a `workspace` command | Ruby |
| [anhoder/homebrew-repo](https://github.com/anhoder/homebrew-repo) | Personal tap with `cmux-nightly` cask via Sparkle/appcast | Ruby |

### Upstream

- [Ghostty](https://ghostty.org/) ([docs](https://ghostty.org/docs) · [config](https://ghostty.org/docs/config) · [source](https://github.com/ghostty-org/ghostty)) — the terminal engine under cmux.
- [agent-browser](https://github.com/vercel-labs/agent-browser) — Vercel's browser automation, ported into cmux. · ★24503

---

## Reference

### Ghostty Config

cmux reads `~/.config/ghostty/config` automatically. Below is a production config optimized for multi-agent workflows.

<details>
<summary><strong>Full config (click to expand)</strong></summary>

```ini
# NOTE: macos-option-as-alt breaks Option+key chars on non-US keyboards (e.g. @ on Turkish layout)
theme = Catppuccin Mocha
background = 1e1e2e
foreground = cdd6f4
cursor-color = f5e0dc
cursor-text = 1e1e2e
cursor-style = block
cursor-style-blink = false
cursor-opacity = 0.9
selection-background = 585b70
selection-foreground = cdd6f4
font-family = JetBrainsMono Nerd Font
font-family-bold = JetBrainsMono Nerd Font
font-family-italic = JetBrainsMono Nerd Font
font-family-bold-italic = JetBrainsMono Nerd Font
font-size = 16
font-thicken = true
font-thicken-strength = 64
font-feature = calt
font-feature = liga
font-codepoint-map = U+2500-U+259F=Menlo
background-opacity = 0.95
background-blur = macos-glass-regular
window-padding-x = 16
window-padding-y = 12
window-padding-balance = true
window-padding-color = extend
window-height = 35
window-width = 120
macos-titlebar-style = transparent
window-decoration = auto
window-theme = dark
window-colorspace = display-p3
window-save-state = always
window-show-tab-bar = never
unfocused-split-opacity = 0.65
unfocused-split-fill = 181825
split-divider-color = 45475a
split-inherit-working-directory = true
tab-inherit-working-directory = true
window-inherit-working-directory = true
window-inherit-font-size = true
scrollback-limit = 50000
clipboard-read = allow
clipboard-write = allow
clipboard-trim-trailing-spaces = true
clipboard-paste-protection = true
clipboard-paste-bracketed-safe = true
copy-on-select = clipboard
shell-integration = zsh
shell-integration-features = no-cursor
term = xterm-256color
confirm-close-surface = false
macos-option-as-alt = true
macos-non-native-fullscreen = true
focus-follows-mouse = false
resize-overlay = after-first
resize-overlay-position = bottom-right
resize-overlay-duration = 500ms
cursor-click-to-move = true
scroll-to-bottom = keystroke, no-output
keybind = alt+left=esc:b
keybind = alt+right=esc:f
keybind = cmd+left=text:\x01
keybind = cmd+right=text:\x05
keybind = alt+backspace=text:\x17
keybind = cmd+k=clear_screen
keybind = cmd+d=new_split:right
keybind = cmd+shift+d=new_split:down
keybind = cmd+alt+left=goto_split:left
keybind = cmd+alt+right=goto_split:right
keybind = cmd+alt+up=goto_split:top
keybind = cmd+alt+down=goto_split:bottom
keybind = cmd+ctrl+left=resize_split:left,20
keybind = cmd+ctrl+right=resize_split:right,20
keybind = cmd+ctrl+up=resize_split:up,10
keybind = cmd+ctrl+down=resize_split:down,10
keybind = cmd+shift+e=equalize_splits
keybind = cmd+shift+z=toggle_split_zoom
keybind = cmd+equal=increase_font_size:2
keybind = cmd+minus=decrease_font_size:2
keybind = cmd+0=reset_font_size
keybind = cmd+shift+comma=reload_config
keybind = cmd+enter=toggle_fullscreen
palette = 0=#45475a
palette = 8=#585b70
palette = 1=#f38ba8
palette = 9=#f38ba8
palette = 2=#a6e3a1
palette = 10=#a6e3a1
palette = 3=#f9e2af
palette = 11=#f9e2af
palette = 4=#89b4fa
palette = 12=#89b4fa
palette = 5=#f5c2e7
palette = 13=#f5c2e7
palette = 6=#94e2d5
palette = 14=#94e2d5
palette = 7=#bac2de
palette = 15=#a6adc8
```

</details>

| Setting | Why |
|---------|-----|
| `window-show-tab-bar = never` | cmux has its own vertical tabs |
| `unfocused-split-opacity = 0.65` | see which agent pane is active |
| `background-opacity = 0.95` | frosted glass without hurting readability |
| `scrollback-limit = 50000` | agent output is verbose |

### Automation Docs

- [How to Scriptize cmux: CLI, AppleScript, Raw Sockets](https://notes.yigitkonur.com/j7ohBAkoc651DC)

<details>
<summary><strong>10-part guide from the cmux source (click to expand)</strong></summary>

| # | Topic |
|---|-------|
| 00 | [Index](./docs/applescript/README.md) |
| 01 | [Overview](./docs/applescript/01-overview.md) |
| 02 | [Setup & Permissions](./docs/applescript/02-setup-permissions-and-verification.md) |
| 03 | [AppleScript Wrapper Pattern](./docs/applescript/03-applescript-cli-wrapper-pattern.md) |
| 04 | [Command Catalog](./docs/applescript/04-command-catalog-practical-index.md) |
| 05 | [Browser Command Surface](./docs/applescript/05-browser-command-surface.md) |
| 06 | [Socket v2 Protocol](./docs/applescript/06-socket-v2-protocol.md) |
| 07 | [v2 Method Inventory](./docs/applescript/07-runtime-v2-method-inventory.md) |
| 08 | [CLI to v2 Mapping](./docs/applescript/08-cli-to-v2-mapping.md) |
| 09 | [Automation Recipes](./docs/applescript/09-automation-recipe-playbook.md) |
| 10 | [Errors & Diagnostics](./docs/applescript/10-errors-diagnostics-triage.md) |

</details>

### Community

| Channel | Link |
|---------|------|
| Discussions | [github.com/…/discussions](https://github.com/manaflow-ai/cmux/discussions) |
| Issues | [github.com/…/issues](https://github.com/manaflow-ai/cmux/issues) |
| Discord | [invite](https://discord.gg/xsgFEVrWCZ) |
| X | [@manaflowai](https://x.com/manaflowai) |
| YouTube | [channel](https://www.youtube.com/channel/UCAa89_j-TWkrXfk9A3CbASw) |

[Show HN](https://news.ycombinator.com/item?id=47079718) · [r/ClaudeCode intro](https://www.reddit.com/r/ClaudeCode/comments/1r43cdr/introducing_cmux_tmux_for_claude_code/) · [r/ClaudeCode vertical tabs](https://www.reddit.com/r/ClaudeCode/comments/1r9g45u/i_made_a_ghosttybased_terminal_with_vertical_tabs/)

### Articles & Coverage

- [Official Demo Video](https://www.youtube.com/watch?v=i-WxO5YUTOs) · [Product Hunt](https://www.producthunt.com/products/cmux) · [YC (Manaflow)](https://www.ycombinator.com/companies/manaflow) · [UBOS](https://ubos.tech/news/introducing-cmux-a-ghostty%E2%80%91based-macos-terminal-with-vertical-tabs-and-ai%E2%80%91agent-notifications/) · [Digg](https://digg.com/technology/QjlMUZ5/cmux-the-terminal-for-multitasking) · [Microlaunch](https://microlaunch.net/p/cmux)

## Contributing

Before opening a PR, verify your entry:

1. **Public repo** with a README
2. **Uses a cmux API** — `CMUX_SOCKET_PATH`, `cmux` CLI, socket protocol, or cmux env vars
3. **Themes/configs** must include at least one cmux-specific feature
4. **Description** — one sentence, neutral tone, no superlatives
5. **Format** — `[owner/repo](url) | \`tag\` | description | Lang · ★N`

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full style guide.

## License

MIT — see [LICENSE](./LICENSE).

# Awesome cmux [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of resources for **[cmux](https://github.com/manaflow-ai/cmux)** — the Ghostty-based macOS terminal for coding agents. This list is for `manaflow-ai/cmux` only — for the Go connection multiplexer by soheilhy, see that repo directly. The ecosystem spans 100+ public repos using cmux's three primitives: `CMUX_WORKSPACE_ID`, `CMUX_SURFACE_ID`, and `CMUX_SOCKET_PATH`.

## Contents

- [Getting Started](#getting-started)
- [Ghostty Config](#ghostty-config)
- [Automation Docs](#automation-docs)
- [Agent Plugins](#agent-plugins)
- [Tools](#tools)
- [Ports](#ports)
- [Alternatives](#alternatives)
- [Setup](#setup)

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
| Changelog | [changelog](https://www.cmux.dev/docs/changelog) |

## Ghostty Config

cmux reads `~/.config/ghostty/config` automatically. Below is a production config optimized for multi-agent workflows.

<details>
<summary><strong>Full config (click to expand)</strong></summary>

```ini
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
| `unfocused-split-opacity = 0.65` | instantly see which agent pane is active |
| `background-opacity = 0.95` | frosted glass without hurting readability |
| `font-size = 16` + `font-thicken` | legible through blur on retina |
| `scrollback-limit = 50000` | agent output is verbose |
| `macos-option-as-alt = true` | word-jump keybindings |

> **Caveat:** `macos-option-as-alt` breaks `Option`+key character input on non-US keyboards (e.g., `@` on Turkish layout).

## Automation Docs

- [How to Scriptize cmux: CLI, AppleScript, Raw Sockets](https://notes.yigitkonur.com/j7ohBAkoc651DC) — deep dive into every automation method.

Rewritten automation docs from the cmux source, organized as a 10-part guide:

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

---

## Agent Plugins

### Claude Code

**Sidebar & Lifecycle Hooks**

- [HazAT/pi-config](https://github.com/HazAT/pi-config) — Hooks into Pi lifecycle events to push agent status, model, token count, and active tool to the cmux sidebar via `set-status`/`notify`, guarded by `CMUX_SOCKET_PATH`. Bundles a SKILL.md reference card. TypeScript · ★155
- [tslateman/cmux-claude-code](https://github.com/tslateman/cmux-claude-code) — Drives the cmux sidebar through 6 Claude Code hooks: "Thinking" on prompt submit, emoji-labeled tool names with a logarithmic progress bar, "Done" + desktop notification on completion. No-op outside cmux. Shell
- [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) — Renames the cmux workspace tab to the git repo name on session start, fires `cmux notify` on completion. Includes restraint rules for when to use browser/progress/notifications. Shell
- [blueraai/bluera-base](https://github.com/blueraai/bluera-base) — Houses a cmux skill package with SKILL.md + five reference docs, plus benchmark evaluations measuring agent performance on cmux tasks with and without the skill.
- [claude-studio/claude-studio](https://github.com/claude-studio/claude-studio) — Ships two cmux CLI reference documents as CLAUDE.md tool context, enabling agents to orchestrate splits and automate the browser from within cmux.

**Skills**

| Repo | Focus | What it teaches Claude | ★ |
|------|-------|----------------------|---|
| [darkspock/cmux-skill](https://github.com/darkspock/cmux-skill) | `browser` | Every `cmux browser` subcommand — DOM, JS eval, cookies, tabs, dialogs, frames — plus workspace/notification commands | ★4 |
| [hashangit/cmux-skill](https://github.com/hashangit/cmux-skill) | `browser` | Browser automation via `snapshot --interactive` element refs, notify decision matrix (`cmux notify` vs `osascript`), auto-wired hooks | |
| [hoonkim/cmux-skills-plugin](https://github.com/hoonkim/cmux-skills-plugin) | `browser` | Dual-skill: browser automation + pane control via `cmux tree`/`read-screen`/`send`. Docs in Korean | |
| [Stealinglight/cmux-claude-code-skill](https://github.com/Stealinglight/cmux-claude-code-skill) | `cli-ref` | Core SKILL.md + three references (CLI, browser, shortcuts) with Python socket API examples | |
| [mikecfisher/cmux-skill](https://github.com/mikecfisher/cmux-skill) | `cli-ref` | Most thorough CLI taxonomy: every command category. Documents `capture-pane` tmux alias and `CMUX_SOCKET_PASSWORD` | |
| [mangledmonkey/cmux-skills](https://github.com/mangledmonkey/cmux-skills) | `cli-ref` | Auto-syncing 4-skill bundle (topology, browser, markdown viewer, debug) via weekly GitHub Actions sync from upstream | |
| [bocktae80/cmux-pilot](https://github.com/bocktae80/cmux-pilot) | `layout` | `/cmux-ws` slash commands to save/restore named workspace layouts (panels, colors, browser URLs) with cron autosave. Docs in Korean | |
| [jhta/cmux-skill](https://github.com/jhta/cmux-skill) | `workflow` | Neovim + git diff split-pane patterns: open files, view diffs with delta, run tests in adjacent panes | |
| [halindrome/cmux-tmux-mapping-for-cc](https://github.com/halindrome/cmux-tmux-mapping-for-cc) | `compat` | tmux abstraction layer routing to cmux or tmux by environment. Auto-creates/cleans up agent panels via hooks. WIP | |

### Pi

- [espennilsen/pi](https://github.com/espennilsen/pi) — Speaks cmux's Unix socket JSON-RPC directly via the built-in `@e9n/pi-cmux` extension: sidebar status, debounced notifications, 7 LLM tools for workspace and browser control. TypeScript · ★27
- [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) — Connects to the cmux socket with a persistent client to fire context-aware notifications summarizing Pi's actions and maintain 4 live sidebar pills (model, state, thinking, tokens). TypeScript · ★13
- [javiermolinar/pi-cmux](https://github.com/javiermolinar/pi-cmux) — Uses `cmux new-split` and `cmux respawn-pane` to power 12+ slash commands: splits, zoxide jumps, worktree handoffs, PR review panes, smart notifications. Published to npm. TypeScript
- [joelhooks/pi-cmux](https://github.com/joelhooks/pi-cmux) — Drives the cmux sidebar via CLI with a 3-second heartbeat (tool + elapsed time), AI session naming via Haiku, worker mode for subagents, peon-ping alerts. TypeScript
- [simonjohansson/pi-cmux](https://github.com/simonjohansson/pi-cmux) — Exposes the full cmux surface through a single `cmux_cli` tool that passes any argv to the binary. Configurable via `CMUX_CLI_PATH`. TypeScript
- [storelayer/pi-cmux-browser](https://github.com/storelayer/pi-cmux-browser) — Wraps the entire `cmux browser` CLI (36+ actions) with persistent surface tracking so the LLM maintains browser state across multi-step web tasks. JavaScript

### OpenCode

- [kdcokenny/ocx](https://github.com/kdcokenny/ocx) — Pushes session status, progress bars, sidebar logs, notifications, and flash triggers to cmux on every OpenCode lifecycle event via its bundled KDCO workspace component. TypeScript · ★418
- [kdcokenny/opencode-notify](https://github.com/kdcokenny/opencode-notify) — Routes native OS notifications through `cmux notify` when `CMUX_WORKSPACE_ID` is set, with automatic fallback to desktop notifications. TypeScript · ★100
- [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) — Bridges the full OpenCode session lifecycle into cmux: status pills, todo-driven progress bars, timeline logs, unread marks, flash triggers — scoped per workspace. TypeScript · ★16
- [Attamusc/opencode-cmux](https://github.com/Attamusc/opencode-cmux) — Connects to cmux via Unix socket JSON-RPC for ~1-2ms latency, with render throttling, log rate limiting, and primary/subagent session distinction. TypeScript
- [Joehoel/opencode-cmux](https://github.com/Joehoel/opencode-cmux) — Two-in-one: an OpenCode plugin pushing status to cmux, plus a Zsh integration polling Azure DevOps and Jira via async workers and displaying results as sidebar pills. Shell

### Copilot & Amp

- [Attamusc/copilot-cmux](https://github.com/Attamusc/copilot-cmux) — Hooks into Copilot CLI lifecycle events and translates them into cmux sidebar status, progress bars, and notifications via Unix socket JSON-RPC with CLI fallback. TypeScript
- [tadashi-aikawa/copilot-plugin-notify](https://github.com/tadashi-aikawa/copilot-plugin-notify) — Emits OSC 777 escape sequences from Copilot CLI hooks, triggering cmux notifications via the standard terminal multiplexer protocol. Configurable allow/deny rules. Shell
- [block/cmux-amp](https://github.com/block/cmux-amp) — Official plugin from Block. Maps Amp agent lifecycle events to cmux sidebar status pills with tool-specific SF Symbol icons and colors. TypeScript

---

## Tools

### Orchestration

**Frameworks**

- [aannoo/hcom](https://github.com/aannoo/hcom) — Spawns agent workspaces via `cmux new-workspace` and tracks them through `CMUX_WORKSPACE_ID`. Supports cmux as one of 24 terminal backends. Rust · ★147
- [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) — Spawns subagents as visible cmux split panes via `cmux new-split`, relays tasks via `cmux send`, polls completion via `cmux read-screen`, cleans up with `cmux close-surface`. Multi-backend (cmux/tmux/zellij). TypeScript · ★76
- [dagster-io/erk](https://github.com/dagster-io/erk) — Opens PRs in dedicated cmux workspaces via `cmux new-workspace`/`cmux rename-workspace`/`cmux select-workspace` through its `cmux checkout` and `cmux teleport` gateway. Python · ★76
- [burggraf/pi-teams](https://github.com/burggraf/pi-teams) — Implements a cmux `TerminalAdapter` for Pi agent teams: spawns splits, checks liveness via `cmux list-pane-surfaces`, manages workspace-level isolation. TypeScript · ★37
- [bjacobso/pimux](https://github.com/bjacobso/pimux) — Uses cmux as its mandatory runtime via a full `CmuxClient` Effect service: per-task workspaces, splits, sidebar status/progress through a task state machine. TypeScript
- [eduwass/cru](https://github.com/eduwass/cru) — Drives cmux splits and sidebar lifecycle phases (SF Symbol icons) through a 447-line TypeScript module, with a detached progress-watcher tracking `~/.claude/tasks/`. Includes E2E tests. TypeScript
- [rjwittams/flotilla](https://github.com/rjwittams/flotilla) — Implements a `CmuxWorkspaceManager` Rust trait that enumerates workspaces across all cmux windows and creates multi-pane layouts from YAML templates. Auto-detects via `CMUX_SOCKET_PATH`. Rust

**Skills**

| Repo | What it teaches Claude |
|------|----------------------|
| [ygrec-app/supreme-leader-skill](https://github.com/ygrec-app/supreme-leader-skill) | "Supreme leader" pattern: splits a 2–8 worker grid via cmux, dispatches tasks, monitors via `read-screen` polling, reviews deliverables — never writes code itself |
| [umitaltintas/cmux-agent-toolkit](https://github.com/umitaltintas/cmux-agent-toolkit) | Parallel fan-out: spawn agents via cmux, synchronize via `wait-for`/`wait-for --signal`. Topology management + tmux compat refs |
| [hummer98/cmux-team](https://github.com/hummer98/cmux-team) | Slash commands spawning typed teams (Researchers, Design, Impl, Test) as dedicated cmux workspaces |
| [baixianger/claude-orchestration-in-cmux](https://github.com/baixianger/claude-orchestration-in-cmux) | Pane-level delegation to parallel Claude sessions via `cmux send`/`read-screen`, coordinated through worktrees |
| [Th3Sp3ct3R/cmux-claude-agents](https://github.com/Th3Sp3ct3R/cmux-claude-agents) | `PreToolUse` hook redirecting Agent tool calls to visible cmux panes via `cmux new-pane`/`cmux send` |
| [ygrec-app/offload-task-skill](https://github.com/ygrec-app/offload-task-skill) | Single-purpose: split a pane, launch `claude --dangerously-skip-permissions`, return to main conversation |

### MCP Servers

- [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) — Exposes 81 tools covering the full cmux hierarchy (windows, workspaces, panes, surfaces) plus agent grid launchers, bulk orchestration, session save/recover, and 12 browser tools. Published to npm. TypeScript
- [EtanHey/cmuxlayer](https://github.com/EtanHey/cmuxlayer) — Provides 20 tools via a dual transport: persistent Unix socket V2 JSON-RPC (~0.1ms latency) with CLI fallback. Includes an agent lifecycle engine to spawn, monitor, and kill coding agents in cmux panes. TypeScript
- [jasonraz/cmux-browser-mcp](https://github.com/jasonraz/cmux-browser-mcp) — Exposes 31 browser-only tools via `cmux browser` subprocess calls. Auto-tracks the last-opened surface so refs are optional on most calls. JavaScript

### Browser Pane

- [azu/cmux-hub](https://github.com/azu/cmux-hub) — Opens a browser split via `cmux browser open-split` to display syntax-highlighted diffs alongside your terminal, sending review comments back through the cmux socket. Self-terminates when the pane closes. Bun binary with marketplace plugin. TypeScript · ★9
- [gonzaloserrano/streamdeck-cmux](https://github.com/gonzaloserrano/streamdeck-cmux) — Reads workspace state from cmux's Unix socket to render live status on Stream Deck buttons — switch workspaces or launch agents with a physical keypress. TypeScript · ★6
- [monzou/mo-cmux](https://github.com/monzou/mo-cmux) — Serves Markdown through a live-reload server in a cmux browser split, auto-closing when the pane is dismissed. Shell
- [doublezz10/figure-viewer](https://github.com/doublezz10/figure-viewer) — Opens an interactive HTML figure gallery in a cmux browser pane, auto-refreshing as new images appear. Falls back to system browser outside cmux. JavaScript
- [RyoHirota68/cmux-pencil-preview](https://github.com/RyoHirota68/cmux-pencil-preview) — Wires a `PostToolUse` hook to the Pencil MCP: exports updated designs as PDFs and reloads the cmux browser pane after every iteration. Shell

### Workspace & Worktree Managers

- [kdcokenny/opencode-worktree](https://github.com/kdcokenny/opencode-worktree) — Opens a new cmux workspace per git worktree when `CMUX_WORKSPACE_ID` or `CMUX_SOCKET_PATH` is detected, keeping each worktree isolated. TypeScript · ★318
- [aschreifels/cwt](https://github.com/aschreifels/cwt) — Creates git worktrees inside new cmux workspaces with configurable splits, sidebar badges, and prompt injection. Ships skills teaching agents to use `set-status`/`log`/`notify`. Go
- [bhandeland/fleet](https://github.com/bhandeland/fleet) — Creates a named cmux workspace per branch with sidebar badges and multi-agent team splits. Degrades gracefully without cmux. Shell
- [tasuku43/kra](https://github.com/tasuku43/kra) — Maintains a persistent 1:1:1 mapping from ticket IDs to filesystem workspaces to cmux workspaces, with capability-gated fallback and stale-mapping reconciliation. Go
- [wwaIII/proj](https://github.com/wwaIII/proj) — Opens projects in new named cmux workspaces with live `[CC]` badges on projects where Claude Code is active. Rust

### Monitoring & Sessions

- [AtAFork/ghostty-claude-code-session-restore](https://github.com/AtAFork/ghostty-claude-code-session-restore) — Snapshots running `claude`/`codex` sessions every 2s and restores them into the correct cmux surfaces via `cmux send` on next launch. Python · ★21
- [owizdom/context-brdige-for-cmux](https://github.com/owizdom/context-brdige-for-cmux) — Polls cmux's socket every 5s, reads scrollback to detect agent sessions, stores in SQLite, and auto-injects context handoff prompts into new sessions in the same directory. Go
- [alaasdk/cmux-ctl](https://github.com/alaasdk/cmux-ctl) — Presents a real-time grid dashboard of all cmux workspaces via `cmux tree`/`sidebar-state`/`read-screen`, with shortcuts to launch, stop, and message agents. Python
- [taichiiwamoto-s/cmux-context](https://github.com/taichiiwamoto-s/cmux-context) — Scrapes the Claude Code status bar from every cmux workspace via `cmux read-screen`, rendering a color-coded context-fill dashboard. Shell
- [ensarkovankaya/cmux-mirror](https://github.com/ensarkovankaya/cmux-mirror) — Mirrors a remote machine's entire cmux layout to the local instance over SSH, connecting each pane to its remote tmux session. Python

### Hardware & Launchers

- [stevenocchipinti/raycast-cmux](https://github.com/stevenocchipinti/raycast-cmux) — Wraps `cmux list-workspaces`/`select-workspace`/`tree`/`new-workspace` into Raycast commands for keyboard-driven workspace switching. TypeScript

---

## Ports

### Windows

- [mkurman/cmux-windows](https://github.com/mkurman/cmux-windows) — WPF/ConPTY port with workspaces, sidebar, splits, OSC notifications, WebView2 browser, session persistence, and CLI. 5 releases. C# · ★16
- [TRINITXX/cmux-windows](https://github.com/TRINITXX/cmux-windows) — Fork of mkurman adding Claude Code hooks (status detection, session resume, Haiku tab titling), Zen mode, and Dracula/One Dark themes. C#
- [aasm3535/wmux](https://github.com/aasm3535/wmux) — WinUI 3 port with xterm.js, sidebar, splits, OSC notifications, WebView2, native Mica backdrop. C#
- [shogotomita/cmux-win](https://github.com/shogotomita/cmux-win) — WPF/ConPTY port under active development. Workspaces, panes, sidebar, CLI, 24 test files. Missing browser and persistence. C#

### Linux

- [asermax/seemux](https://github.com/asermax/seemux) — Rust/GTK4 port with 30+ releases: collapsible tab groups, splits, Claude Code hooks, quake mode, Agent Teams via tmux shim, plugin marketplace. Rust
- [nice-bills/lmux](https://github.com/nice-bills/lmux) — Pure C port using GTK4/VTE/WebKitGTK: workspaces, browser split, D-Bus notifications with rings, session persistence, Unix socket API. C
- [anurag-arjun/cove](https://github.com/anurag-arjun/cove) — Ghostty GTK fork adding a vertical workspace sidebar with notification badges and git branch/PWD display. Zig

---

## Alternatives

### tmux-Based

- [craigsc/cmux](https://github.com/craigsc/cmux) — Pure-bash worktree manager: `cmux new <branch>` spins up isolated worktrees for parallel Claude agents. Tab completion, setup hooks, merge/teardown. Shell · ★367
- [maedana/crmux](https://github.com/maedana/crmux) — Rust tmux sidebar aggregating all Claude sessions with live status, model, context usage, and permission alerts. Inspired by cmux's notification UX. Rust · ★18
- [wolffiex/cmux](https://github.com/wolffiex/cmux) — Fast (~22ms) Bun tmux layout manager with popup carousel, 10 preset layouts, git naming, AI window summaries via Anthropic API. TypeScript
- [theforager/cmux](https://github.com/theforager/cmux) — Bash tmux session manager with interactive selector, live status indicators, `/cmux_name` slash command. Optimized for mobile SSH. Shell
- [jeremyeder/sisi-cmux](https://github.com/jeremyeder/sisi-cmux) — Auto-discovers projects and builds a tmux workspace per project with Claude keybindings and per-type `dev/test/build` commands. TypeScript

### Other

- [davis7dotsh/my-term](https://github.com/davis7dotsh/my-term) — Early-stage native macOS terminal prototype with Arc-style persistent sidebar and SwiftTerm. Swift
- [Kaldy14/clui](https://github.com/Kaldy14/clui) — Electron app organizing Claude Code sessions into project-scoped threads with xterm.js, git integration, and LRU hibernation. TypeScript
- [Pollux-Studio/maxc](https://github.com/Pollux-Studio/maxc) — Tauri-based programmable workspace unifying terminals, browser, and agent orchestration via CLI and socket RPC. Rust
- [wrock/wezterm-agent-cards](https://github.com/wrock/wezterm-agent-cards) — WezTerm plugin replicating cmux's status-card UX: curses Python sidebar with per-session cards driven by Claude hooks. Python
- [danneu/danterm](https://github.com/danneu/danterm) — macOS terminal on libghostty (same engine as cmux) with vertical tabs, tab groups, splits, Claude notification hooks, Nix module. Swift
- [ipdelete/cmux](https://github.com/ipdelete/cmux) — Electron workspace using GitHub Copilot CLI/SDK with Monaco editor and PTY terminals. TypeScript

### Forks

- [llv22/cmux_forward](https://github.com/llv22/cmux_forward) — Adds working-directory restore for Bash sessions. One patch over upstream. Swift

<details>
<summary><strong>Archived</strong></summary>

- [adhyaay-karnwal/cmux](https://github.com/adhyaay-karnwal/cmux) — Abandoned fork extended with Docker isolation (OpenVSCode containers) and multi-CLI support. TypeScript

</details>

---

## Setup

### Themes & Layouts

- [jacobtellep/cmux-setup](https://github.com/jacobtellep/cmux-setup) — Creates a 3-pane Conductor layout in cmux (Claude left, lazygit top-right, dev server bottom-right) with a dark-teal Ghostty theme and git-delta. Shell
- [budah1987/cmux-script](https://github.com/budah1987/cmux-script) — Interactive project picker that creates a 3-pane layout (Claude + yazi file tree + lazygit) using the cmux CLI, auto-starts npm dev servers. Shell
- [rappdw/zen-term](https://github.com/rappdw/zen-term) — Bridges a MacBook (cmux/Ghostty) to an NVIDIA DGX Spark via Mosh with three Zellij layouts. Default auto-starts Claude + live `nvidia-smi`. Shell
- [ctaho19/cmux-cursor-work-style](https://github.com/ctaho19/cmux-cursor-work-style) — Cursor CLI aesthetic: charcoal/blue Ghostty theme, Berkeley Mono 15pt, cmux sidebar tint controls, Claude status line. Shell
- [chrisliu298/ghostty-config](https://github.com/chrisliu298/ghostty-config) — GitHub Dark theme, Berkeley Mono 18pt, 128 MiB scrollback, cmux-ready split keybinds.
- [jcyamacho/zdotfiles](https://github.com/jcyamacho/zdotfiles) — Zsh framework with `cmux.zsh` plugin: install/uninstall via Homebrew tap, `cmux-setup-cli` PATH symlink, `cmux-inside`/`cmux-ping` helpers.
- [karlorz/dev-docs-cmux](https://github.com/karlorz/dev-docs-cmux) — LLM-optimized docs for cmux's own tech stack (Convex, Hono, TanStack, etc.) from context7.com. Shell

### Build & Distribution

- [manaflow-ai/manaflow](https://github.com/manaflow-ai/manaflow) — Primary monorepo for the Manaflow/cmux platform. Contains `cmux-proxy` and `cmux-env` Rust crates as internal subpackages. TypeScript · ★933
- [webkaz/cmux-intel-builds](https://github.com/webkaz/cmux-intel-builds) — Builds unsigned Intel Mac (x86_64) DMGs by polling releases every 6 hours via GitHub Actions.
- [lawrencecchen/cmux-proxy](https://github.com/lawrencecchen/cmux-proxy) — Rust reverse proxy routing to per-workspace loopback IPs (`127.18.x.y`). Optional LD_PRELOAD shim for transparent socket redirection. Rust
- [lawrencecchen/cmux-env](https://github.com/lawrencecchen/cmux-env) — Rust daemon sharing env vars across shells/projects within cmux workspaces. Bash/zsh/fish hooks, dotenv, base64 secrets. Rust
- [budah1987/homebrew-tools](https://github.com/budah1987/homebrew-tools) — Homebrew formula wrapping cmux + yazi + lazygit into a `workspace` launcher command. Ruby
- [anhoder/homebrew-repo](https://github.com/anhoder/homebrew-repo) — Personal tap with `cmux-nightly` cask via Sparkle/appcast. Ruby

### Upstream

- [Ghostty](https://ghostty.org/) ([docs](https://ghostty.org/docs) · [config](https://ghostty.org/docs/config) · [source](https://github.com/ghostty-org/ghostty)) — the terminal engine under cmux.
- [agent-browser](https://github.com/vercel-labs/agent-browser) — Vercel's browser automation, ported into cmux.

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

- [Official Demo Video](https://www.youtube.com/watch?v=i-WxO5YUTOs)
- [Product Hunt](https://www.producthunt.com/products/cmux)
- [YC Company Page (Manaflow)](https://www.ycombinator.com/companies/manaflow)
- [UBOS: Introducing cmux](https://ubos.tech/news/introducing-cmux-a-ghostty%E2%80%91based-macos-terminal-with-vertical-tabs-and-ai%E2%80%91agent-notifications/)
- [Digg: cmux — The Terminal for Multitasking](https://digg.com/technology/QjlMUZ5/cmux-the-terminal-for-multitasking)
- [Microlaunch](https://microlaunch.net/p/cmux)

## Contributing

To add an entry, the repo must be **public**, have a **README**, and **meaningfully use a cmux API** (`CMUX_SOCKET_PATH`, `cmux` CLI, or socket protocol). Themes and configs must include at least one cmux-specific feature.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full style guide and PR checklist.

## License

MIT — see [LICENSE](./LICENSE).

# Awesome cmux [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of resources for **[cmux](https://github.com/manaflow-ai/cmux)** — the Ghostty-based macOS terminal built for coding agents.
> [!IMPORTANT]
> This list is for **`manaflow-ai/cmux`** only. Not the Go connection multiplexer by soheilhy.

## Contents

- [Getting Started](#getting-started)
- [Ghostty Config](#ghostty-config)
- [Automation Docs](#automation-docs)
- [Ecosystem at a Glance](#ecosystem-at-a-glance)
- [Claude Code Extensions](#claude-code-extensions)
  - [Sidebar & Lifecycle Hooks](#sidebar--lifecycle-hooks)
  - [Browser Automation Skills](#browser-automation-skills)
  - [CLI Reference Skills](#cli-reference-skills)
  - [Workspace & Layout Skills](#workspace--layout-skills)
  - [Orchestration Skills](#orchestration-skills)
  - [Developer Workflow Skills](#developer-workflow-skills)
  - [Compatibility Layers](#compatibility-layers)
- [Pi Extensions](#pi-extensions)
- [OpenCode Plugins](#opencode-plugins)
- [Copilot & Amp Plugins](#copilot--amp-plugins)
- [Orchestration Frameworks](#orchestration-frameworks)
- [MCP Servers](#mcp-servers)
- [Browser Pane Tools](#browser-pane-tools)
- [Workspace & Worktree Managers](#workspace--worktree-managers)
- [Monitoring & Session Tools](#monitoring--session-tools)
- [Hardware & Launchers](#hardware--launchers)
- [Windows Ports](#windows-ports)
- [Linux Ports](#linux-ports)
- [tmux-Based Alternatives](#tmux-based-alternatives)
- [Other Alternatives](#other-alternatives)
- [Direct Forks](#direct-forks)
- [Themes, Layouts & Dotfiles](#themes-layouts--dotfiles)
- [Build & Distribution](#build--distribution)
- [Upstream](#upstream)
- [Community](#community)
- [Articles & Coverage](#articles--coverage)

---

## Getting Started

```sh
brew install --cask cmux          # stable
brew install --cask cmux-nightly  # nightly
```

Or grab the DMG: [stable](https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg) | [nightly](https://github.com/manaflow-ai/cmux/releases/download/nightly/cmux-nightly-macos.dmg)

| Resource | Link |
|----------|------|
| Website | [cmux.dev](https://www.cmux.dev/) |
| Source | [github.com/manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) |
| Docs | [Getting Started](https://www.cmux.dev/docs/getting-started) · [Concepts](https://www.cmux.dev/docs/concepts) · [Configuration](https://www.cmux.dev/docs/configuration) · [Keyboard Shortcuts](https://www.cmux.dev/docs/keyboard-shortcuts) |
| API | [Reference](https://www.cmux.dev/docs/api) · [Browser](https://www.cmux.dev/docs/browser-automation) · [Notifications](https://www.cmux.dev/docs/notifications) |
| Blog | [Introducing cmux](https://www.cmux.dev/blog/introducing-cmux) · [Show HN](https://www.cmux.dev/blog/show-hn-launch) · [Zen of cmux](https://www.cmux.dev/blog/zen-of-cmux) |

---

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
| `macos-option-as-alt = true` | word-jump keybindings — [breaks @ on turkish keyboards](https://github.com/manaflow-ai/cmux/issues/1653) |

---

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

## Ecosystem at a Glance

100+ public repos discovered via GitHub code search for cmux primitives.

| Primitive | Repos | Purpose |
|-----------|-------|---------|
| `CMUX_WORKSPACE_ID` | 99 | Identifies the workspace (group of tabs/surfaces) |
| `CMUX_SURFACE_ID` | 69 | Identifies a specific terminal surface |
| `CMUX_SOCKET_PATH` | 64 | Path to the cmux Unix domain socket |

---

## Claude Code Extensions

### Sidebar & Lifecycle Hooks

Plugins that push live agent state into the cmux sidebar and fire notifications.

- [HazAT/pi-config](https://github.com/HazAT/pi-config) — Pi config with a TypeScript cmux extension hooking `session_start`, `agent_start/end`, `turn_end`, `tool_execution_start/end` to push agent status, model, token count, cost, and active tool to the sidebar via `set-status`/`notify` guarded by `CMUX_SOCKET_PATH`. Also bundles a SKILL.md reference card. TypeScript · 155 stars
- [tslateman/cmux-claude-code](https://github.com/tslateman/cmux-claude-code) — 6-hook plugin: shows "Thinking" on prompt submit, updates with emoji-labeled tool names (⚡ Bash, 📖 Read, 🔌 MCP) and a logarithmic progress bar, shows "Done" + desktop notification on completion. No-op outside cmux. Shell
- [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) — Auto-renames workspace tab to git repo name on session start, fires `cmux notify` on completion via hooks, includes best-practice SKILL.md with restraint rules for when to use browser/progress/notifications. Shell
- [blueraai/bluera-base](https://github.com/blueraai/bluera-base) — Production `cmux` skill package with SKILL.md + five reference docs, plus two iterations of benchmark evaluations measuring agent performance on cmux tasks with and without the skill.
- [claude-studio/claude-studio](https://github.com/claude-studio/claude-studio) — Electron Claude Code dashboard shipping two cmux CLI reference documents as CLAUDE.md tool context for workspace/pane control and browser automation.

### Browser Automation Skills

Skills teaching Claude to drive cmux's embedded browser pane.

- [darkspock/cmux-skill](https://github.com/darkspock/cmux-skill) — The most complete browser-automation SKILL.md: covers every `cmux browser` subcommand — DOM interaction, JS eval, cookies, tabs, dialogs, frames — plus workspace/notification commands. 4 stars
- [hoonkim/cmux-skills-plugin](https://github.com/hoonkim/cmux-skills-plugin) — Korean-authored dual-skill plugin with distinct browser automation (`cmux-browser`) and pane control (`cmux-pane-control`) skills using `cmux tree`, `cmux read-screen`, `cmux send`.
- [hashangit/cmux-skill](https://github.com/hashangit/cmux-skill) — Browser skill using element refs from `snapshot --interactive`, plus a notify decision matrix (`cmux notify` vs `osascript`) and `install.sh` that wires hooks automatically. Shell

### CLI Reference Skills

Comprehensive cmux command references for agents.

- [Stealinglight/cmux-claude-code-skill](https://github.com/Stealinglight/cmux-claude-code-skill) — Core SKILL.md plus three deep-dive references (full CLI, browser automation, keyboard shortcuts) with Python socket API examples.
- [mikecfisher/cmux-skill](https://github.com/mikecfisher/cmux-skill) — Most thorough CLI taxonomy: every command category (connection, windows, workspaces, panes, surfaces, I/O, browser, sidebar, notifications). Documents `capture-pane` as a tmux alias and `CMUX_SOCKET_PASSWORD`.
- [mangledmonkey/cmux-skills](https://github.com/mangledmonkey/cmux-skills) — Auto-syncing 4-skill bundle (topology, browser, markdown viewer via `cmux markdown open`, debug-window capture) kept current via weekly GitHub Actions sync from `manaflow-ai/cmux`. Shell

### Workspace & Layout Skills

Skills for saving, restoring, and managing cmux workspace layouts.

- [bocktae80/cmux-pilot](https://github.com/bocktae80/cmux-pilot) — Korean-authored plugin adding `/cmux-ws` slash commands to save/restore named workspace layouts (panel configs, colors, browser URLs, session IDs) to JSON, with 15-minute cron autosave. Shell

### Orchestration Skills

Skills that teach Claude to spawn and coordinate other agents in cmux panes.

- [ygrec-app/supreme-leader-skill](https://github.com/ygrec-app/supreme-leader-skill) — "Supreme leader" pattern: Claude creates a team workspace, splits a 2–8 worker grid via `cmux new-split`, dispatches tasks via `cmux send`, monitors via `cmux read-screen` polling, reviews deliverables, issues fix cycles — never writes code itself.
- [umitaltintas/cmux-agent-toolkit](https://github.com/umitaltintas/cmux-agent-toolkit) — Parallel fan-out patterns: spawn agents via `cmux new-pane`, collect with `cmux read-screen`, synchronize via `cmux wait-for`/`cmux wait-for --signal`. Includes topology management and tmux compatibility refs.
- [hummer98/cmux-team](https://github.com/hummer98/cmux-team) — Slash commands that spawn typed teams (Researchers, Design, Implementation, Test) as dedicated cmux workspaces, relay tasks via `cmux send`, poll progress with `cmux read-screen`, update sidebar with `cmux set-status`. Shell
- [baixianger/claude-orchestration-in-cmux](https://github.com/baixianger/claude-orchestration-in-cmux) — Pane-level orchestrator using `cmux list-panes`/`cmux send`/`cmux read-screen` to delegate to parallel Claude sessions in sibling panes, coordinating through git worktrees and `/tmp` handoff files.
- [Th3Sp3ct3R/cmux-claude-agents](https://github.com/Th3Sp3ct3R/cmux-claude-agents) — `PreToolUse` hook intercepting the built-in Agent tool when `CMUX_SOCKET_PATH` is set, redirecting execution agents to visible cmux panes via `cmux new-pane`/`cmux send`. Shell
- [ygrec-app/offload-task-skill](https://github.com/ygrec-app/offload-task-skill) — Single-purpose: split pane with `cmux new-split`, launch `claude --dangerously-skip-permissions` via `cmux send`, return to main conversation.

### Developer Workflow Skills

Skills for code editing, diffing, and testing workflows.

- [jhta/cmux-skill](https://github.com/jhta/cmux-skill) — Neovim + git diff split-pane patterns: `cmux new-split`/`cmux send`/`cmux read-screen` to open files, view diffs with delta, run tests in adjacent panes. Includes `cmux-helpers.sh` wrapper and socket API ref. Shell

### Compatibility Layers

- [halindrome/cmux-tmux-mapping-for-cc](https://github.com/halindrome/cmux-tmux-mapping-for-cc) — Under-development tmux abstraction layer (`mux_create_panel`/`mux_send`/`mux_destroy_panel`) routing to cmux or tmux based on environment. Auto-creates/cleanup agent panels via hooks. Shell

---

## Pi Extensions

Extensions for the [Pi](https://github.com/microsoft/pi) coding agent. Two camps: **socket-based** (espennilsen, sasha) using Unix socket JSON-RPC, and **CLI-based** (javiermolinar, joelhooks, simonjohansson, storelayer).

- [espennilsen/pi](https://github.com/espennilsen/pi) — Official Pi framework with built-in `@e9n/pi-cmux` extension speaking cmux's Unix socket JSON-RPC directly. Pushes sidebar status, debounced surface-targeted notifications, and 7 LLM tools for workspace management and browser automation. TypeScript · 27 stars
- [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) — Pioneering independent extension using persistent Unix socket. Context-aware notifications summarizing actual Pi actions ("Updated auth.ts", "bash failed"). Maintains 4 sidebar pills: model, state, thinking level, tokens. TypeScript · 13 stars
- [javiermolinar/pi-cmux](https://github.com/javiermolinar/pi-cmux) — Comprehensive workflow toolkit (`npm: pi-cmux`): 12+ slash commands for splits, zoxide jumps, git-worktree handoffs, PR review splits, configurable smart notifications. TypeScript · 3 stars
- [joelhooks/pi-cmux](https://github.com/joelhooks/pi-cmux) — Polished CLI-driven extension with 3s sidebar heartbeat (tool + elapsed time), AI session naming via `claude-haiku-4-5`, worker mode for subagents, peon-ping sound alerts. TypeScript · 1 star
- [simonjohansson/pi-cmux](https://github.com/simonjohansson/pi-cmux) — Minimalist: single `cmux_cli` tool passing any argv to cmux, exposing the full command surface through one interface. Configurable via `CMUX_CLI_PATH`. TypeScript
- [storelayer/pi-cmux-browser](https://github.com/storelayer/pi-cmux-browser) — Browser-specialized: wraps the entire `cmux browser` surface (36+ actions) with persistent surface tracking across multi-step web tasks. JavaScript

---

## OpenCode Plugins

- [kdcokenny/ocx](https://github.com/kdcokenny/ocx) — "shadcn for OpenCode config" — CLI/registry for profiles and plugins. Bundled KDCO workspace component pushes session status, progress bars, sidebar logs, notifications, workspace-action marks, and flash triggers on every lifecycle event. TypeScript · 418 stars
- [kdcokenny/opencode-notify](https://github.com/kdcokenny/opencode-notify) — Native OS notifications on task complete/error/input-needed, with `cmux notify` routing when `CMUX_WORKSPACE_ID` is set. Automatic fallback to desktop notifications. TypeScript · 100 stars
- [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) — Full lifecycle bridge (`npm: opencode-cmux`): sidebar status pills, todo-driven progress bars, timeline logs, unread marks, flash triggers — scoped per workspace ID. TypeScript · 16 stars
- [Attamusc/opencode-cmux](https://github.com/Attamusc/opencode-cmux) — Production-grade: Unix socket JSON-RPC (~1-2ms), render throttling (200ms), log rate limiting (5/s), primary/subagent session distinction. TypeScript
- [Joehoel/opencode-cmux](https://github.com/Joehoel/opencode-cmux) — Two-in-one: OpenCode plugin + Zsh shell integration polling Azure DevOps PRs/pipelines and Jira tickets via async workers, displaying as sidebar pills. Shell

---

## Copilot & Amp Plugins

- [Attamusc/copilot-cmux](https://github.com/Attamusc/copilot-cmux) — GitHub Copilot CLI hooks (`sessionStart`→`errorOccurred`) translated to sidebar status/progress/notifications. Unix socket JSON-RPC primary, CLI fallback. TypeScript
- [tadashi-aikawa/copilot-plugin-notify](https://github.com/tadashi-aikawa/copilot-plugin-notify) — Copilot CLI hooks emitting OSC 777 escape sequences (`\e]777;notify;…\a`) — works with any OSC 777-aware terminal. Configurable tool/path/URL allow/deny rules. Shell
- [block/cmux-amp](https://github.com/block/cmux-amp) — Official Amp plugin from Block (Square). Maps agent lifecycle events to sidebar status pills with tool-specific SF Symbol icons and colors. TypeScript

---

## Orchestration Frameworks

Libraries and tools (not skills) for coordinating multiple agents across cmux panes.

- [aannoo/hcom](https://github.com/aannoo/hcom) — Multi-AI-agent orchestrator supporting cmux as one of 24 terminal backends. Spawns via `cmux new-workspace`, tracks via `CMUX_WORKSPACE_ID`. Rust · 147 stars
- [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) — Multi-backend pane abstraction (cmux/tmux/zellij). Spawns subagents via `cmux new-split`, relays via `cmux send`, polls completion via `cmux read-screen`, cleans up with `cmux close-surface`. TypeScript · 76 stars
- [dagster-io/erk](https://github.com/dagster-io/erk) — GitHub PR and Graphite stack TUI with cmux gateway: `cmux checkout`/`cmux teleport` open PRs in dedicated named workspaces. Python · 76 stars
- [burggraf/pi-teams](https://github.com/burggraf/pi-teams) — Multi-backend `TerminalAdapter` for Pi agent teams. cmux adapter: `new-split`, `list-pane-surfaces` liveness checks, workspace-level isolation. TypeScript · 37 stars
- [bjacobso/pimux](https://github.com/bjacobso/pimux) — Bun/Effect agent orchestrator using cmux as mandatory runtime. Full `CmuxClient` Effect service: per-task workspaces, splits, sidebar status/progress/notifications through a task state machine. TypeScript
- [eduwass/cru](https://github.com/eduwass/cru) — Agent team layout tool with cmux as first-class backend (447-line module). Drives splits, lifecycle phases (SF Symbol icons), detached progress-watcher tracking `~/.claude/tasks/`. E2E test suite. TypeScript
- [rjwittams/flotilla](https://github.com/rjwittams/flotilla) — Rust fleet management TUI. `CmuxWorkspaceManager` trait: enumerates across all windows, creates multi-pane layouts from YAML templates, auto-detects via `CMUX_SOCKET_PATH`. Rust

---

## MCP Servers

- [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) — 81 tools (`npm: cmux-agent-mcp`). Full hierarchy (windows/workspaces/panes/surfaces) via `execFileSync`. Agent grid launchers, `cmux_orchestrate` bulk dispatch, session save/recover, 12 browser tools. TypeScript
- [EtanHey/cmuxlayer](https://github.com/EtanHey/cmuxlayer) — 20 tools. Dual transport: persistent Unix socket V2 JSON-RPC (~0.1ms) with CLI fallback. Agent lifecycle engine (spawn/monitor/kill claude/codex/gemini/kiro/cursor). TypeScript
- [jasonraz/cmux-browser-mcp](https://github.com/jasonraz/cmux-browser-mcp) — 31 browser-only tools via `cmux browser …` subprocess. Navigation, DOM snapshots, interaction, JS eval, tabs, cookies/storage. Auto-tracks last-opened surface. JavaScript · 3 stars

---

## Browser Pane Tools

Tools using cmux's embedded browser split for rendering content.

- [azu/cmux-hub](https://github.com/azu/cmux-hub) — Diff and code-review tool. Reads `CMUX_SURFACE_ID`, opens via `cmux browser open-split`, self-terminates via `cmux surface-health`. Sends review comments to terminal via `surface.send_text` JSON-RPC over `/tmp/cmux.sock`. Shiki syntax highlighting, commit history, GitHub PR/CI, customizable toolbar. Bun binary + marketplace plugin. TypeScript · 9 stars
- [monzou/mo-cmux](https://github.com/monzou/mo-cmux) — Serves Markdown through `mo` live-reload server in a browser split via `cmux browser open-split`. Auto-closes server when pane dismissed (via `cmux surface-health`). Shell · 2 stars
- [doublezz10/figure-viewer](https://github.com/doublezz10/figure-viewer) — Generates interactive HTML figure gallery from output directories, opens in cmux browser pane. Background watcher auto-refreshes. Detects cmux via `CMUX_SOCKET_PATH`/`CMUX_WORKSPACE_ID`. JavaScript
- [RyoHirota68/cmux-pencil-preview](https://github.com/RyoHirota68/cmux-pencil-preview) — `PostToolUse` hook on Pencil MCP `batch_design`: auto-exports PDF, reloads browser pane via `cmux browser <surface> reload`. Zero-friction design hot reload. Shell

---

## Workspace & Worktree Managers

- [kdcokenny/opencode-worktree](https://github.com/kdcokenny/opencode-worktree) — OpenCode plugin: auto-creates git worktrees, opens a new cmux workspace per worktree when `CMUX_WORKSPACE_ID` or `CMUX_SOCKET_PATH` detected. TypeScript · 318 stars
- [aschreifels/cwt](https://github.com/aschreifels/cwt) — Go CLI: worktrees inside cmux workspaces with configurable splits, sidebar badges (branch/ticket/provider), prompt injection via `cmux send-text`. Bundled skills teach agents `set-status`/`set-progress`/`log`/`notify`. Go · 1 star
- [bhandeland/fleet](https://github.com/bhandeland/fleet) — Bash worktree lifecycle manager: named workspace per branch, sidebar badges, multi-agent teams in splits, graceful degradation without cmux. Shell
- [tasuku43/kra](https://github.com/tasuku43/kra) — Go task manager: persistent 1:1:1 mapping (ticket → filesystem → cmux workspace). Full surface API with capability-gated fallback and stale-mapping auto-reconciliation. Go
- [wwaIII/proj](https://github.com/wwaIII/proj) — Rust TUI project launcher: opens projects in named cmux workspaces with `claude --dangerously-skip-permissions`, live `[CC]` badges via `lsof`. Rust

---

## Monitoring & Session Tools

- [AtAFork/ghostty-claude-code-session-restore](https://github.com/AtAFork/ghostty-claude-code-session-restore) — macOS launchd daemon: snapshots `claude`/`codex` sessions every 2s via `lsof`, restores into correct cmux surfaces via `cmux send`. Python · 21 stars
- [owizdom/context-brdige-for-cmux](https://github.com/owizdom/context-brdige-for-cmux) — Go daemon polling cmux socket every 5s, reads scrollback to detect agent sessions, stores in SQLite, auto-injects context handoff prompts into new sessions in same directory. Go · 1 star
- [alaasdk/cmux-ctl](https://github.com/alaasdk/cmux-ctl) — Textual Python TUI dashboard: live workspace grid via `cmux tree`/`sidebar-state`/`read-screen`, send input, launch/stop agents. Python
- [taichiiwamoto-s/cmux-context](https://github.com/taichiiwamoto-s/cmux-context) — Single-file Bash: scrapes Claude Code status bar from every workspace via `cmux read-screen`, renders color-coded context fill/model/rate-limits dashboard. Shell
- [ensarkovankaya/cmux-mirror](https://github.com/ensarkovankaya/cmux-mirror) — `cmux-mirror sync <host>`: mirrors remote cmux workspace layout to local instance over SSH, connecting each pane to its remote tmux session. Python

---

## Hardware & Launchers

- [gonzaloserrano/streamdeck-cmux](https://github.com/gonzaloserrano/streamdeck-cmux) — Stream Deck plugin via Unix socket (`/tmp/cmux.sock`): live workspace status on buttons (colors, CWD, Claude state, progress), switch workspaces or launch agents with a keypress. Nightly/stable toggle. TypeScript · 6 stars
- [stevenocchipinti/raycast-cmux](https://github.com/stevenocchipinti/raycast-cmux) — Raycast extension: fuzzy-search workspaces/surfaces, create workspaces, jump to latest notification — all via `cmux` CLI commands. TypeScript

---

## Windows Ports

- [mkurman/cmux-windows](https://github.com/mkurman/cmux-windows) — WPF/ConPTY, 19K LOC, 5 releases. Workspaces, sidebar, splits, OSC notifications, WebView2 browser, session persistence, CLI. C# · 16 stars
- [TRINITXX/cmux-windows](https://github.com/TRINITXX/cmux-windows) — Fork of mkurman adding Claude Code hooks (status detection, session auto-resume, Haiku tab titling), Zen mode, Dracula/One Dark themes, workspace templates. C#
- [aasm3535/wmux](https://github.com/aasm3535/wmux) — WinUI 3 + xterm.js. Sidebar, splits, OSC notifications, WebView2, native Mica backdrop. C#
- [shogotomita/cmux-win](https://github.com/shogotomita/cmux-win) — WPF/ConPTY under active development. Workspaces, panes, sidebar, OSC notifications, CLI, 24 test files. Missing browser/persistence. C#

---

## Linux Ports

- [asermax/seemux](https://github.com/asermax/seemux) — Most mature: Rust/GTK4, 30+ releases. Collapsible tab groups, splits, Claude Code hooks (`SEEMUX_SOCKET`/`SEEMUX_SESSION_ID`), quake mode, Agent Teams via tmux shim, plugin marketplace. Rust · 1 star
- [nice-bills/lmux](https://github.com/nice-bills/lmux) — Pure C, GTK4/VTE/WebKitGTK, 15K LOC. Workspaces, browser split, D-Bus notifications with rings, session persistence, Unix socket API. C
- [anurag-arjun/cove](https://github.com/anurag-arjun/cove) — Ghostty GTK fork adding vertical workspace sidebar. Workspace CRUD, notification badges, git branch/PWD display. Zig · 2 stars

---

## tmux-Based Alternatives

- [craigsc/cmux](https://github.com/craigsc/cmux) — Pure-bash worktree manager: `cmux new <branch>` spins up isolated worktrees for parallel Claude agents. Tab completion, setup hooks, merge/teardown. Shell · 367 stars
- [maedana/crmux](https://github.com/maedana/crmux) — Rust tmux sidebar aggregating Claude sessions: live status, model, context usage, permission alerts. Inspired by cmux's notification UX. Rust · 18 stars
- [wolffiex/cmux](https://github.com/wolffiex/cmux) — Fast (~22ms) Bun tmux layout manager: popup carousel, 10 preset layouts, git-based naming, AI window summaries via Anthropic API. TypeScript · 1 star
- [theforager/cmux](https://github.com/theforager/cmux) — Bash tmux session manager with interactive selector, live status indicators, `/cmux_name` slash command. Optimized for mobile SSH. Shell
- [jeremyeder/sisi-cmux](https://github.com/jeremyeder/sisi-cmux) — TypeScript CLI: auto-discovers projects, builds tmux workspace with Claude keybindings and per-type `dev/test/build` commands. TypeScript · 2 stars

---

## Other Alternatives

- [davis7dotsh/my-term](https://github.com/davis7dotsh/my-term) — Early-stage native macOS terminal prototype ("better-cmux"). Arc-style persistent sidebar, SwiftTerm. Swift · 1 star
- [Kaldy14/clui](https://github.com/Kaldy14/clui) — Electron app: project-scoped Claude Code threads with xterm.js terminals, git integration, LRU session hibernation. TypeScript
- [Pollux-Studio/maxc](https://github.com/Pollux-Studio/maxc) — Tauri-based programmable workspace: terminals + browser + agent orchestration via CLI and socket RPC. Rust · 1 star
- [wrock/wezterm-agent-cards](https://github.com/wrock/wezterm-agent-cards) — WezTerm plugin replicating cmux's status-card UX: curses Python sidebar with per-session cards driven by Claude hooks. Python · 1 star
- [danneu/danterm](https://github.com/danneu/danterm) — macOS terminal on libghostty (same engine as cmux). Vertical tabs, tab groups, splits, Claude notification hooks, Nix module. Swift
- [ipdelete/cmux](https://github.com/ipdelete/cmux) — Electron workspace using GitHub Copilot CLI/SDK: Monaco editor, PTY terminals, Copilot Chat. TypeScript

---

## Direct Forks

- [llv22/cmux_forward](https://github.com/llv22/cmux_forward) — Adds working-directory restore for Bash sessions. One targeted patch over upstream. Swift
- [adhyaay-karnwal/cmux](https://github.com/adhyaay-karnwal/cmux) — Abandoned. Extended with Docker isolation (OpenVSCode containers) and multi-CLI support (Claude/Codex/Gemini/Cursor/Amp/Opencode). TypeScript

---

## Themes, Layouts & Dotfiles

- [jacobtellep/cmux-setup](https://github.com/jacobtellep/cmux-setup) — One-command installer: 3-pane Conductor layout (Claude left, lazygit top-right, dev server bottom-right) with dark-teal Ghostty theme and git-delta. Shell
- [budah1987/cmux-script](https://github.com/budah1987/cmux-script) — Interactive workspace launcher: arrow-key project picker, 3-pane layout (Claude + yazi file tree + lazygit tabbed left split), auto-starts npm dev servers. Shell
- [rappdw/zen-term](https://github.com/rappdw/zen-term) — MacBook-to-DGX-Spark setup via Mosh. Three Zellij layouts (default auto-starts Claude + `nvidia-smi`). OSC notification helpers and pane-title glyphs. Shell
- [ctaho19/cmux-cursor-work-style](https://github.com/ctaho19/cmux-cursor-work-style) — Cursor CLI aesthetic: charcoal/blue Ghostty theme, Berkeley Mono 15pt, sidebar tint controls, Claude status line (dir/model/context%). Shell
- [chrisliu298/ghostty-config](https://github.com/chrisliu298/ghostty-config) — GitHub Dark, Berkeley Mono 18pt, 128 MiB scrollback, cmux-ready split keybinds.
- [jcyamacho/zdotfiles](https://github.com/jcyamacho/zdotfiles) — Zsh framework with `cmux.zsh` plugin: install/uninstall via Homebrew tap, `cmux-setup-cli` PATH symlink, `cmux-inside`/`cmux-ping` helpers.
- [karlorz/dev-docs-cmux](https://github.com/karlorz/dev-docs-cmux) — LLM-optimized docs for cmux's own tech stack (Convex, Hono, TanStack, etc.) from context7.com. Shell

---

## Build & Distribution

- [manaflow-ai/manaflow](https://github.com/manaflow-ai/manaflow) — Primary monorepo: parallel agent orchestration in isolated VS Code workspaces. Contains `cmux-proxy` and `cmux-env` Rust crates. TypeScript · 933 stars
- [webkaz/cmux-intel-builds](https://github.com/webkaz/cmux-intel-builds) — GitHub Actions: builds unsigned Intel Mac (x86_64) DMGs by polling releases every 6 hours.
- [lawrencecchen/cmux-proxy](https://github.com/lawrencecchen/cmux-proxy) — Rust reverse proxy for workspace network isolation. Per-workspace loopback IPs (`127.18.x.y`), optional LD_PRELOAD shim. Rust
- [lawrencecchen/cmux-env](https://github.com/lawrencecchen/cmux-env) — Rust daemon + CLI: shared env vars across shells/projects within workspaces. Bash/zsh/fish hooks, dotenv, base64 secrets. Rust
- [budah1987/homebrew-tools](https://github.com/budah1987/homebrew-tools) — Homebrew formula wrapping cmux with yazi + lazygit into a `workspace` launcher. Ruby
- [anhoder/homebrew-repo](https://github.com/anhoder/homebrew-repo) — Personal tap with `cmux-nightly` cask via Sparkle/appcast. Ruby

---

## Upstream

- [Ghostty](https://ghostty.org/) ([docs](https://ghostty.org/docs) · [config](https://ghostty.org/docs/config) · [source](https://github.com/ghostty-org/ghostty)) — the terminal engine under cmux.
- [agent-browser](https://github.com/vercel-labs/agent-browser) — Vercel's browser automation (23.4k stars), ported into cmux.

---

## Community

| Channel | Link |
|---------|------|
| Discussions | [github.com/…/discussions](https://github.com/manaflow-ai/cmux/discussions) |
| Issues | [github.com/…/issues](https://github.com/manaflow-ai/cmux/issues) |
| Discord | [invite](https://discord.gg/xsgFEVrWCZ) |
| X | [@manaflowai](https://x.com/manaflowai) |
| YouTube | [channel](https://www.youtube.com/channel/UCAa89_j-TWkrXfk9A3CbASw) |

[Show HN](https://news.ycombinator.com/item?id=47079718) · [r/ClaudeCode intro](https://www.reddit.com/r/ClaudeCode/comments/1r43cdr/introducing_cmux_tmux_for_claude_code/) · [r/ClaudeCode vertical tabs](https://www.reddit.com/r/ClaudeCode/comments/1r9g45u/i_made_a_ghosttybased_terminal_with_vertical_tabs/)

---

## Articles & Coverage

- [Official Demo Video](https://www.youtube.com/watch?v=i-WxO5YUTOs)
- [Product Hunt](https://www.producthunt.com/products/cmux)
- [YC Company Page (Manaflow)](https://www.ycombinator.com/companies/manaflow)
- [UBOS: Introducing cmux](https://ubos.tech/news/introducing-cmux-a-ghostty%E2%80%91based-macos-terminal-with-vertical-tabs-and-ai%E2%80%91agent-notifications/)
- [Digg: cmux — The Terminal for Multitasking](https://digg.com/technology/QjlMUZ5/cmux-the-terminal-for-multitasking)
- [Microlaunch](https://microlaunch.net/p/cmux)

---

## Contributing

PRs welcome. Please read [CONTRIBUTING.md](./CONTRIBUTING.md) first.

## License

MIT — see [LICENSE](./LICENSE).

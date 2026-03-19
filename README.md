# Awesome cmux [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of resources for **[cmux](https://github.com/manaflow-ai/cmux)** — the Ghostty-based macOS terminal built for coding agents.
> [!IMPORTANT]
> This list is for **`manaflow-ai/cmux`** only. Not the Go connection multiplexer by soheilhy.

## Contents

- [Getting Started](#getting-started)
- [Ghostty Config for cmux](#ghostty-config-for-cmux)
- [Automation & Scripting](#automation--scripting)
- [Ecosystem Overview](#ecosystem-overview)
- [Diff & Code Review](#diff--code-review)
- [Multi-Agent Orchestration](#multi-agent-orchestration)
- [MCP Servers](#mcp-servers)
- [Claude Code Skills & Plugins](#claude-code-skills--plugins)
- [Pi Agent Extensions](#pi-agent-extensions)
- [OpenCode, Copilot & Amp Integrations](#opencode-copilot--amp-integrations)
- [Workspace & Worktree Tools](#workspace--worktree-tools)
- [Browser & Viewer Tools](#browser--viewer-tools)
- [Hardware & Desktop Integration](#hardware--desktop-integration)
- [Session & Context Management](#session--context-management)
- [Terminal Ports & Alternatives](#terminal-ports--alternatives)
- [Infrastructure & Distribution](#infrastructure--distribution)
- [Configs, Themes & Setup](#configs-themes--setup)
- [Upstream](#upstream)
- [Community](#community)
- [Articles & Coverage](#articles--coverage)
- [Related Projects](#related-projects)

---

## Getting Started

**Install**

```sh
brew install --cask cmux          # stable
brew install --cask cmux-nightly  # nightly
```

Or grab the DMG directly: [stable](https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg) | [nightly](https://github.com/manaflow-ai/cmux/releases/download/nightly/cmux-nightly-macos.dmg)

**Official Resources**

| Resource | Link |
|----------|------|
| Website | [cmux.dev](https://www.cmux.dev/) |
| Source Code | [github.com/manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) |
| Docs | [Getting Started](https://www.cmux.dev/docs/getting-started) · [Concepts](https://www.cmux.dev/docs/concepts) · [Configuration](https://www.cmux.dev/docs/configuration) · [Keyboard Shortcuts](https://www.cmux.dev/docs/keyboard-shortcuts) |
| API | [API Reference](https://www.cmux.dev/docs/api) · [Browser Automation](https://www.cmux.dev/docs/browser-automation) · [Notifications](https://www.cmux.dev/docs/notifications) |
| Blog | [Introducing cmux](https://www.cmux.dev/blog/introducing-cmux) · [Show HN Launch](https://www.cmux.dev/blog/show-hn-launch) · [The Zen of cmux](https://www.cmux.dev/blog/zen-of-cmux) |
| Changelog | [changelog](https://www.cmux.dev/docs/changelog) |

---

## Ghostty Config for cmux

cmux reads your `~/.config/ghostty/config` automatically — themes, fonts, colors all carry over. Below is a production-tested config optimized for cmux's multi-agent workflow.

**Why this matters:** cmux inherits *everything* from Ghostty, but not every default works well with vertical tabs, split panes, and agent output. This config tunes the settings that matter most.

<details>
<summary><strong>Full config (click to expand)</strong></summary>

```ini
# ============================================================================
#  ghostty config — cmux-optimized, productivity-first
# ============================================================================

# --- theme & colors --------------------------------------------------------
theme = Catppuccin Mocha
background = 1e1e2e
foreground = cdd6f4

# --- cursor ----------------------------------------------------------------
cursor-color = f5e0dc
cursor-text = 1e1e2e
cursor-style = block
cursor-style-blink = false
cursor-opacity = 0.9

# --- selection -------------------------------------------------------------
selection-background = 585b70
selection-foreground = cdd6f4

# --- fonts -----------------------------------------------------------------
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

# --- transparency & blur ---------------------------------------------------
background-opacity = 0.95
background-blur = macos-glass-regular

# --- window & padding ------------------------------------------------------
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

# --- split panes -----------------------------------------------------------
unfocused-split-opacity = 0.65
unfocused-split-fill = 181825
split-divider-color = 45475a
split-inherit-working-directory = true
tab-inherit-working-directory = true
window-inherit-working-directory = true
window-inherit-font-size = true

# --- scrollback ------------------------------------------------------------
scrollback-limit = 50000

# --- clipboard -------------------------------------------------------------
clipboard-read = allow
clipboard-write = allow
clipboard-trim-trailing-spaces = true
clipboard-paste-protection = true
clipboard-paste-bracketed-safe = true
copy-on-select = clipboard

# --- shell integration -----------------------------------------------------
shell-integration = zsh
shell-integration-features = no-cursor
term = xterm-256color
confirm-close-surface = false

# --- macos specific --------------------------------------------------------
macos-option-as-alt = true
macos-non-native-fullscreen = true
focus-follows-mouse = false

# --- resize overlay --------------------------------------------------------
resize-overlay = after-first
resize-overlay-position = bottom-right
resize-overlay-duration = 500ms

# --- mouse & interaction ---------------------------------------------------
cursor-click-to-move = true
scroll-to-bottom = keystroke, no-output

# --- keybindings -----------------------------------------------------------
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

# --- palette (catppuccin mocha) --------------------------------------------
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

**Key decisions explained:**

| Setting | Why |
|---------|-----|
| `window-show-tab-bar = never` | cmux has its own vertical tabs — ghostty's native tab bar just wastes space |
| `unfocused-split-opacity = 0.65` | instantly see which agent pane is active when running 3-4 side by side |
| `background-opacity = 0.95` | frosted glass effect adds depth without hurting readability |
| `font-size = 16` + `font-thicken` | stays legible through blur and at lower opacity on retina |
| `scrollback-limit = 50000` | agent output is verbose — 50k lines covers long sessions without eating ram |
| `macos-option-as-alt = true` | enables word-jump keybindings (opt+arrow) — but [breaks @ on turkish keyboards](https://github.com/manaflow-ai/cmux/issues/1653) |
| `window-padding-x = 16` | breathing room between text and cmux's sidebar |

---

## Automation & Scripting

### Blog post

- [How to Scriptize cmux: The Full Automation Surface (CLI, AppleScript, Raw Sockets)](https://notes.yigitkonur.com/j7ohBAkoc651DC) — deep dive into every automation method cmux supports.

### AppleScript & Raw Socket Docs

Rewritten automation docs from the cmux source, organized as a 10-part guide:

| # | Topic |
|---|-------|
| 00 | [Index](./docs/applescript/README.md) |
| 01 | [Overview](./docs/applescript/01-overview.md) |
| 02 | [Setup, Permissions & Verification](./docs/applescript/02-setup-permissions-and-verification.md) |
| 03 | [AppleScript Wrapper Pattern](./docs/applescript/03-applescript-cli-wrapper-pattern.md) |
| 04 | [Command Catalog](./docs/applescript/04-command-catalog-practical-index.md) |
| 05 | [Browser Command Surface](./docs/applescript/05-browser-command-surface.md) |
| 06 | [Socket v2 Protocol](./docs/applescript/06-socket-v2-protocol.md) |
| 07 | [Runtime v2 Method Inventory](./docs/applescript/07-runtime-v2-method-inventory.md) |
| 08 | [CLI to v2 Mapping](./docs/applescript/08-cli-to-v2-mapping.md) |
| 09 | [Automation Recipe Playbook](./docs/applescript/09-automation-recipe-playbook.md) |
| 10 | [Errors, Diagnostics & Triage](./docs/applescript/10-errors-diagnostics-triage.md) |

---

## Ecosystem Overview

The cmux ecosystem spans **100+ public repositories** discovered via GitHub code search for cmux's three core primitives and repo/topic search. The community has built extensions across every integration surface: Claude Code skills, Pi agent extensions, OpenCode/Copilot/Amp bridges, MCP servers, multi-agent orchestrators, hardware integrations, and cross-platform ports.

| Primitive | Repos using it | Purpose |
|-----------|---------------|---------|
| `CMUX_WORKSPACE_ID` | 99 | Identifies the cmux workspace (group of tabs/surfaces) |
| `CMUX_SURFACE_ID` | 69 | Identifies a specific terminal surface (pane/tab) |
| `CMUX_SOCKET_PATH` | 64 | Path to the cmux Unix domain socket for IPC |

---

## Diff & Code Review

- [azu/cmux-hub](https://github.com/azu/cmux-hub) — Browser-based diff and code-review tool that reads `CMUX_SURFACE_ID` to identify the launching terminal, calls `cmux browser open-split` to render its UI as a split pane (self-terminating via `cmux surface-health` polling), and uses `cmux sidebar-state` to auto-detect the working directory. Review comments and toolbar actions are sent directly to the originating terminal surface via the `surface.send_text` JSON-RPC method over `/tmp/cmux.sock`. Features syntax-highlighted diffs (Shiki), commit history browsing, GitHub PR/CI integration, and a customizable toolbar with shell actions. Ships as a standalone Bun binary with auto-update and a Claude Code marketplace plugin. `v1.5.0` · TypeScript · 9 stars

---

## Multi-Agent Orchestration

Tools for running, coordinating, and managing multiple AI coding agents across cmux terminal panes.

- [aannoo/hcom](https://github.com/aannoo/hcom) — A Rust-based multi-AI-agent orchestrator that supports cmux as one of 24 terminal backends; when selected, it spawns agent workspaces via `cmux new-workspace` and tracks pane IDs through the `CMUX_WORKSPACE_ID` environment variable. Rust · 147 stars
- [dagster-io/erk](https://github.com/dagster-io/erk) — A Python GitHub PR and Graphite stack management TUI that integrates cmux as an optional workspace backend, offering `cmux checkout` and `cmux teleport` actions that call `cmux new-workspace`, `cmux rename-workspace`, and `cmux select-workspace` to open PRs in dedicated named workspaces. Python · 76 stars
- [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) — A TypeScript Pi agent extension providing a multi-backend pane abstraction (cmux/tmux/zellij) that spawns subagents as visible cmux split panes using `cmux new-split`, relays tasks via `cmux send`, polls completion via `cmux read-screen` watching for a sentinel string, and cleans up with `cmux close-surface`. TypeScript · 76 stars
- [burggraf/pi-teams](https://github.com/burggraf/pi-teams) — A TypeScript multi-backend terminal adapter library for Pi agent teams that implements a full `TerminalAdapter` interface for cmux, spawning agents as split panes via `cmux new-split`, checking liveness with `cmux list-pane-surfaces`, and managing workspace-level isolation through `cmux new-workspace` and `cmux workspace-action`. TypeScript · 37 stars
- [bjacobso/pimux](https://github.com/bjacobso/pimux) — A Bun/Effect TypeScript agent orchestrator that uses cmux as its mandatory workspace runtime, implementing a full `CmuxClient` Effect service that shells out to the cmux CLI to create per-task workspaces, split agent/shell panes, send commands, and drive sidebar status/progress/notifications through a complete task state machine. TypeScript
- [eduwass/cru](https://github.com/eduwass/cru) — A Claude Code agent team layout tool that treats cmux as a first-class pane backend, implementing native workspace management via a 447-line TypeScript module that drives splits, surface I/O, sidebar lifecycle phases (spawning/working/done with SF Symbol icons), and a detached progress-watcher process that tracks `~/.claude/tasks/` to update the cmux sidebar in real time. TypeScript
- [rjwittams/flotilla](https://github.com/rjwittams/flotilla) — A Rust development fleet management TUI (agents, branches, PRs, workspaces) that implements cmux as its primary workspace manager backend via a `CmuxWorkspaceManager` trait: it enumerates workspaces across all cmux windows, creates multi-pane layouts from YAML templates using the cmux CLI, and auto-detects cmux via `CMUX_SOCKET_PATH`. Rust
- [hummer98/cmux-team](https://github.com/hummer98/cmux-team) — A Claude Code skill and slash-command collection that orchestrates visible multi-agent development by having Claude spawn subagents as dedicated cmux workspaces using `cmux new-workspace`/`cmux new-split`, relay tasks via `cmux send`, monitor progress through `cmux read-screen` polling, and surface status in the cmux sidebar with `cmux set-status`. Shell
- [ygrec-app/supreme-leader-skill](https://github.com/ygrec-app/supreme-leader-skill) — A Claude Code skill implementing the "supreme leader" orchestration pattern: Claude creates a cmux team workspace, splits it into a worker grid (2–8 panes) using `cmux new-split`, dispatches tasks via `cmux send`, autonomously monitors workers via `cmux read-screen` polling in a loop, reviews deliverables, and issues fix cycles — never writing code itself.
- [baixianger/claude-orchestration-in-cmux](https://github.com/baixianger/claude-orchestration-in-cmux) — A Claude Code skill that turns Claude into a pane-level orchestrator inside cmux, using `cmux list-panes`, `cmux send`, `cmux send-key`, and `cmux read-screen` to delegate tasks to parallel Claude Code sessions running in sibling panes, coordinating them through git worktrees and shared `/tmp` handoff files.
- [Th3Sp3ct3R/cmux-claude-agents](https://github.com/Th3Sp3ct3R/cmux-claude-agents) — A Claude Code hook + slash command kit that intercepts the built-in Agent tool via `PreToolUse` when `CMUX_SOCKET_PATH` is set, redirecting execution agents (coder, tester, researcher) to visible cmux panes via `cmux new-pane`/`cmux send`/`cmux send-key`, and fires `cmux notify` when each agent finishes. Shell

---

## MCP Servers

Model Context Protocol servers that expose cmux capabilities to AI agents.

- [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) — A TypeScript MCP server (81 tools, npm `cmux-agent-mcp`) that exposes the full cmux hierarchy — windows, workspaces, panes, surfaces — via synchronous `execFileSync` CLI calls, reading `CMUX_WORKSPACE_ID`/`CMUX_SURFACE_ID` env vars as default targets. Includes high-level launchers to spawn grids of AI agents (claude/gemini/codex/opencode/goose) with auto-trust, bulk prompt delivery via `cmux_orchestrate`, session save/recover for crash resilience, and 12 browser automation tools. TypeScript
- [EtanHey/cmuxlayer](https://github.com/EtanHey/cmuxlayer) — A TypeScript MCP server providing 20 tools for programmatic cmux workspace control, with a dual-mode transport that connects to cmux via persistent Unix socket at `/tmp/cmux.sock` (V2 JSON-RPC, ~0.1ms latency) and falls back to CLI subprocess if the socket is unavailable. Includes a full agent lifecycle engine — spawn, monitor, and kill AI coding agents (claude/codex/gemini/kiro/cursor) running in cmux panes, with state stored in `~/.local/state/cmux-agents`. TypeScript
- [jasonraz/cmux-browser-mcp](https://github.com/jasonraz/cmux-browser-mcp) — An MCP server (JavaScript, single-file) that exposes 31 tools for driving cmux's embedded browser via subprocessed `cmux browser …` CLI calls, covering navigation, DOM snapshots, element interaction, JS evaluation, tab management, and cookie/storage access. Tracks the last-opened browser surface automatically so surface refs are optional on most calls. JavaScript · 3 stars

---

## Claude Code Skills & Plugins

Extensions that give Claude Code native awareness and control of cmux surfaces, browser, sidebar, and notifications.

### Featured

- [HazAT/pi-config](https://github.com/HazAT/pi-config) — A personal Pi config that provides first-class cmux integration on two levels: a TypeScript extension (`extensions/cmux/`) that hooks into Pi lifecycle events (`session_start`, `agent_start/end`, `turn_end`, `tool_execution_start/end`) and pushes live state (agent status, model, thinking level, token count, cost, active tool) to the cmux sidebar via `set-status`/`clear-status`/`notify` CLI calls guarded by `CMUX_SOCKET_PATH`; and a `skills/cmux/SKILL.md` reference card that instructs the agent how to orchestrate multi-terminal workflows using cmux's full surface/workspace/send/read-screen API. TypeScript · 155 stars
- [blueraai/bluera-base](https://github.com/blueraai/bluera-base) — A Claude Code base configuration repo that houses a production `cmux` skill package — comprising a full quick-reference SKILL.md plus five detailed API/concepts reference documents — along with two iterations of benchmark evaluation results measuring agent performance on cmux tasks (layout setup, browser login, notifications) with and without the skill loaded.
- [tslateman/cmux-claude-code](https://github.com/tslateman/cmux-claude-code) — Claude Code plugin that live-drives the cmux sidebar — shows "Thinking" on prompt submit, updates with emoji-labeled tool names (⚡ Bash, 📖 Read, 🔌 MCP tools) and a logarithmic progress bar per tool call, then shows "Done" with a desktop notification on completion, all as a no-op outside cmux. Shell
- [claude-studio/claude-studio](https://github.com/claude-studio/claude-studio) — An Electron + React dashboard for Claude Code usage analytics that ships two comprehensive cmux CLI reference documents (workspace/pane control and browser automation) as CLAUDE.md tool context, enabling the agent to orchestrate terminal splits and automate the embedded browser from within cmux.

### Skills

- [darkspock/cmux-skill](https://github.com/darkspock/cmux-skill) — The most complete standalone browser-automation SKILL.md available — covers every `cmux browser` subcommand from DOM interaction and JS eval to cookies, tabs, dialogs, and frames, plus general workspace/notification commands. 4 stars
- [mangledmonkey/cmux-skills](https://github.com/mangledmonkey/cmux-skills) — Auto-syncing plugin that bundles four upstream cmux skills — topology control, browser automation, a live-reloading markdown viewer panel (`cmux markdown open`), and an internal debug-window capture tool — kept current via weekly GitHub Actions sync from the official `manaflow-ai/cmux` repo. Shell
- [Stealinglight/cmux-claude-code-skill](https://github.com/Stealinglight/cmux-claude-code-skill) — Comprehensive cmux plugin with a concise core SKILL.md plus three deep-dive reference files covering the full CLI, browser automation, and all keyboard shortcuts — includes Python socket API examples.
- [umitaltintas/cmux-agent-toolkit](https://github.com/umitaltintas/cmux-agent-toolkit) — Agent-orchestration toolkit skill covering parallel fan-out patterns — teaches Claude to spawn agents via `cmux new-pane`, collect results with `cmux read-screen`, and synchronize between panes using `cmux wait-for`/`cmux wait-for --signal`; includes thorough topology management and tmux compatibility references.
- [bocktae80/cmux-pilot](https://github.com/bocktae80/cmux-pilot) — Korean-authored plugin that adds `/cmux-ws` slash commands to save, restore, and create named cmux workspace layouts — with panel configs, colors, browser URLs, and Claude session IDs — to a JSON file, with optional 15-minute cron-based autosave. Shell
- [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) — Opinionated plugin that auto-renames the workspace tab to the git repo name on session start (via `cmux rename-workspace`), fires `cmux notify` on task/session completion via hooks, and provides a best-practice SKILL.md with explicit restraint rules for when to use browser splits, progress bars, and notifications. Shell
- [jhta/cmux-skill](https://github.com/jhta/cmux-skill) — Developer-workflow skill focused on Neovim + git diff split-pane patterns — teaches Claude to use `cmux new-split`, `cmux send`, and `cmux read-screen` to open code files, view git diffs with delta, and run tests in new panes; includes a `cmux-helpers.sh` wrapper and socket API reference. Shell
- [hoonkim/cmux-skills-plugin](https://github.com/hoonkim/cmux-skills-plugin) — Korean-authored dual-skill plugin providing distinct browser automation (`cmux-browser`) and terminal pane control (`cmux-pane-control`) skills — the pane control skill teaches Claude to use `cmux tree`, `cmux read-screen`, and `cmux send` to read logs, run commands, and restart servers in other panes.
- [hashangit/cmux-skill](https://github.com/hashangit/cmux-skill) — Full-featured cmux skill with a comprehensive browser automation reference using element refs from `snapshot --interactive`, plus a decision matrix for in-app (`cmux notify`) vs system (`osascript`) notifications and a ready-to-use `install.sh` that wires `cmux notify` into Claude Code hooks. Shell
- [mikecfisher/cmux-skill](https://github.com/mikecfisher/cmux-skill) — General-purpose cmux skill with the most thorough CLI taxonomy reference covering every command category (connection, windows, workspaces, panes, surfaces, terminal I/O, browser, sidebar, notifications) — notable for documenting `capture-pane` as a tmux-compatible alias.
- [ygrec-app/offload-task-skill](https://github.com/ygrec-app/offload-task-skill) — Single-purpose skill that teaches Claude to offload a self-contained task to a background Claude Code session by splitting the current workspace pane with `cmux new-split`, launching `claude --dangerously-skip-permissions` in it via `cmux send`, then returning to the main conversation.
- [halindrome/cmux-tmux-mapping-for-cc](https://github.com/halindrome/cmux-tmux-mapping-for-cc) — Under-development plugin that provides a tmux-compatible abstraction layer (`mux_create_panel`, `mux_send`, `mux_destroy_panel`) routing panel operations to either cmux or tmux based on the active environment — automatically creates and cleans up isolated panels for each Claude sub-agent via hooks. Shell

---

## Pi Agent Extensions

Extensions for the [Pi](https://github.com/microsoft/pi) coding agent that integrate with cmux's sidebar, notifications, and browser.

- [espennilsen/pi](https://github.com/espennilsen/pi) — Pi agent home with extensions including pi-cmux for sidebar/notifications. TypeScript · 27 stars
- [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) — Context-aware notifications, sidebar status, and browser automation via cmux socket API. TypeScript · 13 stars
- [javiermolinar/pi-cmux](https://github.com/javiermolinar/pi-cmux) — cmux-powered terminal workflows for Pi: notifications, split panes, zoxide jumps, review helpers. TypeScript · 3 stars
- [joelhooks/pi-cmux](https://github.com/joelhooks/pi-cmux) — Sidebar status, notifications, live tool activity, and workspace control. TypeScript · 1 star
- [simonjohansson/pi-cmux](https://github.com/simonjohansson/pi-cmux) — cmux integration for Pi. TypeScript
- [benjaminmodayil/pi-cmux-notify](https://github.com/benjaminmodayil/pi-cmux-notify) — Pi extension for cmux notification relay.
- [storelayer/pi-cmux-browser](https://github.com/storelayer/pi-cmux-browser) — Pi agent & skill for web dev with Playwright — browse, inspect, test web apps via cmux browser. JavaScript
- [Whamp/pi-interactive-subagents-tmux](https://github.com/Whamp/pi-interactive-subagents-tmux) — Fork of pi-interactive-subagents replacing cmux with tmux. TypeScript

---

## OpenCode, Copilot & Amp Integrations

Bridges between cmux and other coding tools.

- [kdcokenny/ocx](https://github.com/kdcokenny/ocx) — The "shadcn for OpenCode config" — a CLI and registry system for managing OpenCode profiles and plugins. Its bundled KDCO workspace component integrates deeply with cmux, pushing session status, progress bars, sidebar logs, notifications, workspace-action marks, and flash triggers through the cmux CLI on every OpenCode lifecycle event. TypeScript · 418 stars
- [kdcokenny/opencode-notify](https://github.com/kdcokenny/opencode-notify) — An OpenCode plugin that delivers native OS notifications (macOS Notification Center, Windows Toast, Linux notify-send) when AI tasks complete, error, or require input, with optional cmux-native routing via `cmux notify` when `CMUX_WORKSPACE_ID` is set and automatic fallback to desktop notifications when cmux is unavailable. TypeScript · 100 stars
- [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) — OpenCode plugin (`npm: opencode-cmux`) that pushes full session lifecycle into cmux: sets sidebar status pills (working/waiting/question), drives progress bars from todo items, fires desktop notifications on idle/error/permission/question events, logs timeline entries, marks workspaces unread, and triggers flash — all scoped to the correct cmux workspace ID when available. TypeScript · 16 stars
- [Attamusc/copilot-cmux](https://github.com/Attamusc/copilot-cmux) — A GitHub Copilot CLI plugin that hooks into Copilot's `sessionStart`/`sessionEnd`/`preToolUse`/`postToolUse`/`errorOccurred` lifecycle events and translates them into cmux sidebar status (thinking/working/done/error), progress bars, logs, and notifications — communicating with cmux via a Unix socket (JSON-RPC) when available, falling back to the `cmux` CLI. TypeScript
- [Attamusc/opencode-cmux](https://github.com/Attamusc/opencode-cmux) — An OpenCode plugin with a production-grade cmux integration layer that distinguishes primary sessions from subagents, tracks active tool calls in real time, drives sidebar status/progress/logs with render throttling and log rate limiting, and communicates via a Unix socket (JSON-RPC) for ~1-2ms latency instead of spawning a CLI process per event. TypeScript
- [Joehoel/opencode-cmux](https://github.com/Joehoel/opencode-cmux) — A two-in-one package: an OpenCode plugin that pushes AI session status, todo progress, permissions, and notifications into cmux, plus a Zsh shell integration that auto-detects git repos, polls Azure DevOps PRs and pipelines and Jira tickets via background async workers, and displays them as cmux sidebar pills — notifying on pipeline failures and long-running shell commands. Shell
- [tadashi-aikawa/copilot-plugin-notify](https://github.com/tadashi-aikawa/copilot-plugin-notify) — A GitHub Copilot CLI plugin that sends OSC 777 escape sequences (`\e]777;notify;title;body\a`) to the terminal — the standard multiplexer notification protocol — triggering desktop notifications in cmux, tmux-notify, and any other OSC 777-aware terminal; supports configurable allow/deny rules for tools, paths, and URLs. Shell
- [block/cmux-amp](https://github.com/block/cmux-amp) — An official Amp plugin from Block (Square) that maps Amp agent lifecycle events (session start, agent thinking, tool calls by type, agent done/error/interrupted) to cmux sidebar status pills with tool-specific SF Symbol icons and colors, plus sidebar log entries. TypeScript

---

## Workspace & Worktree Tools

Tools for managing git worktrees, project workspaces, and development environments inside cmux.

- [kdcokenny/opencode-worktree](https://github.com/kdcokenny/opencode-worktree) — An OpenCode plugin that auto-creates git worktrees and spawns isolated terminal sessions; integrates with cmux by detecting `CMUX_WORKSPACE_ID` or `CMUX_SOCKET_PATH`+`CMUX_SOCKET_MODE=allowAll` to open a dedicated new cmux workspace per worktree rather than reusing the current one. TypeScript · 318 stars
- [aschreifels/cwt](https://github.com/aschreifels/cwt) — A purpose-built Go CLI that creates git worktrees inside new cmux workspaces, wiring up configurable pane splits, sidebar status badges (branch/ticket/provider), and prompt injection via `cmux send-text`; ships bundled AI skills teaching agents to use cmux notifications (`set-status`, `set-progress`, `log`, `notify`) throughout their sessions. Go · 1 star
- [bhandeland/fleet](https://github.com/bhandeland/fleet) — A Bash worktree lifecycle manager for parallel Claude Code sessions that, when cmux is present, creates a named cmux workspace per branch with sidebar status badges, launches Claude via `cmux send`, and supports multi-agent teams in split panes; gracefully degrades to a no-multiplexer mode when cmux is unavailable. Shell
- [tasuku43/kra](https://github.com/tasuku43/kra) — A Go task/workspace manager that maintains a persistent 1:1:1 mapping from ticket IDs to filesystem workspaces to cmux workspaces, driving the full cmux surface API (create, rename, select, close, status, panes, splits, markdown viewer, browser state) with capability-gated fallback and stale-mapping auto-reconciliation. Go
- [wwaIII/proj](https://github.com/wwaIII/proj) — A Rust TUI project launcher that opens projects in new named cmux workspaces running `claude --dangerously-skip-permissions`, with live `[CC]` badges on projects where Claude Code is currently active (detected via `lsof`). Rust

---

## Browser & Viewer Tools

Extensions that use cmux's embedded browser split pane for rendering content.

- [monzou/mo-cmux](https://github.com/monzou/mo-cmux) — A Claude Code plugin that serves a Markdown file through the `mo` live-reload server and displays it in a cmux browser split pane via `cmux browser open-split`, automatically closing the server when the pane is dismissed (detected via `cmux surface-health` polling). Shell · 2 stars
- [doublezz10/figure-viewer](https://github.com/doublezz10/figure-viewer) — A Node.js CLI that generates an interactive HTML figure gallery from a project's output directories (PNG, JPG, PDF, SVG) and opens it in a cmux browser pane (or system browser fallback), with a background watcher that auto-refreshes the view as new images are produced. Detects cmux via `CMUX_SOCKET_PATH` and `CMUX_WORKSPACE_ID`. JavaScript
- [RyoHirota68/cmux-pencil-preview](https://github.com/RyoHirota68/cmux-pencil-preview) — A Claude Code plugin that wires a `PostToolUse` hook to the Pencil MCP `batch_design` tool, automatically exporting the updated design as a PDF and reloading the designated cmux browser pane via `cmux browser <surface> reload` after every design iteration for zero-friction hot reload. Shell

---

## Hardware & Desktop Integration

Physical hardware controls and OS-level launchers for cmux.

- [gonzaloserrano/streamdeck-cmux](https://github.com/gonzaloserrano/streamdeck-cmux) — A Stream Deck plugin that connects to cmux's Unix socket (`/tmp/cmux.sock`) to display live workspace status — colors, active CWD, Claude run/input state, and progress bars — directly on hardware buttons, and lets you switch workspaces or launch a new `claude --dangerously-skip-permissions` session with a single physical keypress. Supports nightly/stable socket toggle. TypeScript · 6 stars
- [stevenocchipinti/raycast-cmux](https://github.com/stevenocchipinti/raycast-cmux) — A Raycast extension that wraps four `cmux` CLI commands — `list-workspaces`, `select-workspace`, `tree`, `move-surface`, and `new-workspace` — into keyboard-driven Raycast commands, letting you fuzzy-search and jump to any workspace or surface (tab), create a new workspace, or navigate to the latest notification without touching the mouse. TypeScript

---

## Session & Context Management

Tools for saving/restoring sessions, sharing context between agents, and monitoring workspace state.

- [AtAFork/ghostty-claude-code-session-restore](https://github.com/AtAFork/ghostty-claude-code-session-restore) — A macOS launchd daemon that watches for running `claude`/`codex` processes inside Ghostty tabs or cmux workspaces, snapshots their session IDs and working directories every 2 seconds via `lsof`, and restores them on next launch — using `cmux send` to replay sessions into the correct workspace surfaces and AppleScript to rebuild Ghostty tabs. Python · 21 stars
- [owizdom/context-brdige-for-cmux](https://github.com/owizdom/context-brdige-for-cmux) — A Go daemon that polls cmux's Unix socket API every 5 seconds, reads terminal scrollback from every pane to detect and parse Claude Code/Codex/Gemini/Aider sessions into a SQLite store, then automatically injects an LLM-generated context handoff prompt into any new agent session that opens in the same project directory — enabling zero-copy, zero-user-action cross-agent context continuity. Go · 1 star
- [alaasdk/cmux-ctl](https://github.com/alaasdk/cmux-ctl) — A Textual-based Python TUI that drives the cmux CLI (`tree`, `sidebar-state`, `read-screen`, `send`, `send-key`, `new-workspace`) to present a real-time grid dashboard of all cmux workspaces, showing live agent state, terminal output previews, and notification counts — with keyboard shortcuts to launch, stop, and send input to Claude Code agents without leaving the terminal. Python
- [taichiiwamoto-s/cmux-context](https://github.com/taichiiwamoto-s/cmux-context) — A single-file Bash script that calls `cmux list-workspaces` and `cmux read-screen` to scrape the Claude Code status bar from every active workspace, rendering a color-coded terminal dashboard showing context fill percentage, model, and rate limits at a glance. Shell
- [ensarkovankaya/cmux-mirror](https://github.com/ensarkovankaya/cmux-mirror) — A Python CLI tool (`cmux-mirror sync <host>`) that mirrors a remote machine's entire cmux workspace and pane layout to the local cmux instance over SSH, connecting each local pane to its corresponding remote tmux session for live terminal access to all remote workspaces simultaneously. Python

---

## Terminal Ports & Alternatives

### Cross-Platform Ports

**Windows**

- [mkurman/cmux-windows](https://github.com/mkurman/cmux-windows) — A fully implemented WPF/ConPTY terminal multiplexer for Windows 10/11 with workspaces, vertical sidebar, split panes, OSC notification ingestion, WebView2 browser pane, session persistence, and a CLI tool — the most mature native Windows cmux port with 5 releases. C# · 16 stars
- [TRINITXX/cmux-windows](https://github.com/TRINITXX/cmux-windows) — An active fork of mkurman/cmux-windows adding deep Claude Code integrations: hook-based per-workspace status detection (Running/Needs Input/Completed), Claude session auto-resume on restart, Haiku-powered tab auto-titling, Zen mode, Dracula/One Dark themes, and workspace templates. C#
- [aasm3535/wmux](https://github.com/aasm3535/wmux) — A WinUI 3 port using Windows App SDK with xterm.js for terminal rendering, implementing workspace sidebar, split panes, OSC notifications, WebView2 browser panel, and native WinUI 3 Mica backdrop. C#
- [shogotomita/cmux-win](https://github.com/shogotomita/cmux-win) — A WPF/ConPTY Windows port under active AI-assisted development, implementing workspaces, panes, sidebar, OSC notifications, and a CLI tool with 24 test files — missing browser pane and session persistence. C#

**Linux**

- [asermax/seemux](https://github.com/asermax/seemux) — The most production-ready Linux cmux port: a Rust/GTK4 terminal with 30+ releases, vertical sidebar with collapsible tab groups, split panes, Claude Code hook integration via `SEEMUX_SOCKET`/`SEEMUX_SESSION_ID` env vars, dropdown/quake mode, Agent Teams via tmux shim, session persistence, and a Claude Code plugin marketplace. Rust · 1 star
- [nice-bills/lmux](https://github.com/nice-bills/lmux) — A Linux terminal multiplexer in pure C using GTK4/VTE/WebKitGTK, implementing workspaces, browser split, D-Bus notifications with rings, session persistence, and a Unix socket API — delivered in a single 15,000+ LOC commit with 14 test files. C
- [anurag-arjun/cove](https://github.com/anurag-arjun/cove) — A fork of Ghostty's GTK Linux frontend adding a cmux-inspired vertical workspace sidebar atop Ghostty's GPU-accelerated terminal engine. Implements workspace CRUD, unread notification badges, and git branch/PWD display. Zig · 2 stars

### Conceptual Alternatives

- [craigsc/cmux](https://github.com/craigsc/cmux) — A pure-bash worktree lifecycle manager that spins up isolated git worktrees for parallel Claude Code agents with a single command (`cmux new <branch>`). Zero dependencies beyond git and the Claude CLI; includes tab completion, a project-specific setup hook system, and merge/teardown helpers. Shell · 367 stars
- [maedana/crmux](https://github.com/maedana/crmux) — A Rust-based tmux sidebar that aggregates all Claude Code sessions into a single monitoring pane showing live status, model info, context usage, and permission alerts — inspired by manaflow-ai/cmux's notification UX, reimplemented as a lightweight tmux plugin with RPC scriptability. Rust · 18 stars
- [jeremyeder/sisi-cmux](https://github.com/jeremyeder/sisi-cmux) — A TypeScript CLI that scans a directory, auto-discovers projects by type (Node, Python, Rust, etc.), and builds a tmux workspace with one window per project — includes Claude Code keybindings and context-aware `dev/test/build` commands. TypeScript · 2 stars
- [davis7dotsh/my-term](https://github.com/davis7dotsh/my-term) — An early-stage native macOS terminal prototype named "better-cmux," exploring an Arc-style persistent sidebar with per-window tabs and long-lived sessions using SwiftTerm. Swift · 1 star
- [Kaldy14/clui](https://github.com/Kaldy14/clui) — An Electron desktop app forked from t3code that organizes Claude Code CLI sessions into project-scoped threads with full xterm.js terminals, git workflow integration, and LRU hibernation of dormant sessions. TypeScript
- [Pollux-Studio/maxc](https://github.com/Pollux-Studio/maxc) — An open-source Tauri-based programmable developer workspace that unifies terminals, browser surfaces, and AI coding agent orchestration into structured workspaces controlled via a CLI and socket RPC API — a broader-scope alternative with automation-first design. Rust · 1 star
- [wolffiex/cmux](https://github.com/wolffiex/cmux) — A fast (~22ms) Bun-based tmux layout manager that adds a popup carousel UI for managing windows with 10 preset split layouts, auto-naming from git context, AI-powered window summaries via Anthropic API, and a directory picker. TypeScript · 1 star
- [wrock/wezterm-agent-cards](https://github.com/wrock/wezterm-agent-cards) — A WezTerm Claude Code plugin that replicates cmux's agent status card UX for Linux — a curses-based Python sidebar shows per-session status cards driven by Claude Code lifecycle hooks. Python · 1 star
- [danneu/danterm](https://github.com/danneu/danterm) — A personal macOS terminal built on libghostty (the same rendering engine as manaflow-ai/cmux) with a vertical tab sidebar, collapsible tab groups, split panes, and JSON-driven layout restoration — includes Claude Code notification hooks and a Nix home-manager module. Swift
- [theforager/cmux](https://github.com/theforager/cmux) — A bash-based Claude Code session manager using tmux, with an interactive session selector showing live status indicators (running/waiting/idle/error), session preview, and a `/cmux_name` slash command for auto-titling sessions — optimized for remote SSH access via mobile clients. Shell
- [ipdelete/cmux](https://github.com/ipdelete/cmux) — An Electron-based multi-repo workspace and agent manager using the GitHub Copilot CLI/SDK — provides a three-pane layout with Monaco editor, PTY terminals, and Copilot Chat, positioning itself as the Copilot-ecosystem equivalent. TypeScript

### Direct Forks of manaflow-ai/cmux

- [llv22/cmux_forward](https://github.com/llv22/cmux_forward) — A direct fork that adds working-directory restore when resuming Bash sessions — virtually identical to upstream with one targeted patch. Swift
- [adhyaay-karnwal/cmux](https://github.com/adhyaay-karnwal/cmux) — An abandoned fork extended with Docker-based isolation (each agent task runs in its own OpenVSCode container) and multi-CLI support spanning Claude Code, Codex, Gemini CLI, Cursor, Amp, and Opencode. TypeScript

---

## Infrastructure & Distribution

Homebrew taps, build pipelines, proxies, and official tooling.

- [manaflow-ai/manaflow](https://github.com/manaflow-ai/manaflow) — The primary open-source monorepo for the Manaflow/cmux platform — a parallel AI agent orchestration tool that spawns coding agents (Claude Code, Codex CLI, Gemini CLI, etc.) in isolated VS Code workspaces. Contains the Rust crates (`cmux-proxy`, `cmux-env`) as internal subpackages. TypeScript · 933 stars
- [manaflow-ai/homebrew-cmux](https://github.com/manaflow-ai/homebrew-cmux) — The official Homebrew tap for cmux, providing a stable-channel cask (`brew install --cask cmux`) that installs the cmux macOS terminal app and its CLI binary from releases. Ruby · 2 stars
- [webkaz/cmux-intel-builds](https://github.com/webkaz/cmux-intel-builds) — A community-maintained GitHub Actions workflow that automatically builds unsigned Intel Mac (x86_64) DMG installers of cmux by polling manaflow-ai/cmux releases every 6 hours, filling the gap left by the official ARM-only distribution.
- [lawrencecchen/cmux-proxy](https://github.com/lawrencecchen/cmux-proxy) — A Rust HTTP/WebSocket/TCP reverse proxy for cmux workspace network isolation, routing requests to per-workspace loopback IPs (`127.18.x.y`) via request headers; includes an optional LD_PRELOAD shim that transparently redirects socket calls for processes running inside workspace directories. Rust
- [lawrencecchen/cmux-env](https://github.com/lawrencecchen/cmux-env) — A Rust daemon (`envd`) and CLI client (`envctl`) that share environment variables across shells and project directories within cmux workspaces, with shell hook integration for bash/zsh/fish and support for dotenv file ingestion and base64-encoded secrets. Rust
- [budah1987/homebrew-tools](https://github.com/budah1987/homebrew-tools) — A personal Homebrew formula (`workspace`) that installs a shell script wrapping cmux with Yazi file explorer, lazygit, and live preview dependencies into a single `workspace` launcher command. Ruby
- [anhoder/homebrew-repo](https://github.com/anhoder/homebrew-repo) — A personal Homebrew tap providing a `cmux-nightly` cask tracking the nightly release channel via Sparkle/appcast. Ruby

---

## Configs, Themes & Setup

Starter configs, dotfiles, setup scripts, themes, and layout presets.

- [jacobtellep/cmux-setup](https://github.com/jacobtellep/cmux-setup) — One-command macOS installer that replicates Conductor's IDE layout in cmux — a `workspace` CLI command creates a 3-pane split with Claude Code (left), lazygit diff panel (top-right), and a dev server terminal (bottom-right), with matching Ghostty and lazygit dark-teal themes and git-delta configured as the pager. Shell
- [budah1987/cmux-script](https://github.com/budah1987/cmux-script) — Feature-rich interactive workspace launcher for cmux using its native CLI — presents an arrow-key project picker, creates a 3-pane layout (Claude Code in main pane, yazi file tree + lazygit in a tabbed left split), auto-starts npm dev servers and opens Chrome. Shell
- [rappdw/zen-term](https://github.com/rappdw/zen-term) — Reproducible AI development environment bridging a MacBook (cmux/Ghostty) to an NVIDIA DGX Spark via Mosh, with three Zellij layouts deployed remotely — default layout auto-starts Claude Code alongside a live `nvidia-smi` GPU monitor, with shell helpers that drive cmux notification rings and pane-title status glyphs via OSC sequences. Shell
- [ctaho19/cmux-cursor-work-style](https://github.com/ctaho19/cmux-cursor-work-style) — Work-machine setup for cmux inspired by the Cursor CLI aesthetic — installs a custom charcoal/blue Ghostty theme (`cursor-dark-cmux`), a Berkeley Mono 15pt config with cmux sidebar tint controls, and a Claude Code status line script that displays current directory, active model, and context window usage in matching colors. Shell
- [chrisliu298/ghostty-config](https://github.com/chrisliu298/ghostty-config) — Personal Ghostty terminal config compatible with cmux, using GitHub Dark theme, Berkeley Mono 18pt with custom cell sizing, 128 MiB scrollback, and cmux-ready split-pane keybinds.
- [jcyamacho/zdotfiles](https://github.com/jcyamacho/zdotfiles) — A Zsh dotfiles framework that ships a dedicated `cmux.zsh` plugin providing install/uninstall automation via the `manaflow-ai/cmux` Homebrew tap, a `cmux-setup-cli` function that symlinks the app-bundle binary into PATH, and shell helpers (`cmux-inside`, `cmux-ping`) for detecting and probing a running cmux session.
- [karlorz/dev-docs-cmux](https://github.com/karlorz/dev-docs-cmux) — Auto-fetched LLM-optimized documentation for cmux's tech stack (Convex, Hono, TanStack, shadcn, Tailwind, Bun, etc.) sourced from context7.com, structured so Claude Code can reference upstream library docs directly when developing the cmux application itself. Shell

---

## Upstream

- [Ghostty](https://ghostty.org/) ([docs](https://ghostty.org/docs) · [config reference](https://ghostty.org/docs/config) · [source](https://github.com/ghostty-org/ghostty)) — the terminal engine under cmux.
- [agent-browser](https://github.com/vercel-labs/agent-browser) — Vercel's browser automation (23.4k stars), ported into cmux.

---

## Community

| Channel | Link |
|---------|------|
| GitHub Discussions | [discussions](https://github.com/manaflow-ai/cmux/discussions) |
| GitHub Issues | [issues](https://github.com/manaflow-ai/cmux/issues) |
| Discord | [invite](https://discord.gg/xsgFEVrWCZ) |
| X / Twitter | [@manaflowai](https://x.com/manaflowai) |
| YouTube | [channel](https://www.youtube.com/channel/UCAa89_j-TWkrXfk9A3CbASw) |

**Notable threads:**
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

## Related Projects

- [coder/mux](https://github.com/coder/mux) — A different coding-agent multiplexer (1.4k stars, TypeScript). Not affiliated with `manaflow-ai/cmux`.

---

## Contributing

PRs welcome. Please read [CONTRIBUTING.md](./CONTRIBUTING.md) first.

## License

MIT — see [LICENSE](./LICENSE).

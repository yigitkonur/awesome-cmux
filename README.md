# Awesome cmux [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Last updated](https://img.shields.io/github/last-commit/yigitkonur/awesome-cmux?label=last%20updated)

> A curated, opinionated guide to the **[cmux](https://github.com/manaflow-ai/cmux)** ecosystem — the Ghostty-based macOS terminal built for AI coding agents. **120+ community projects** and growing. This list covers `manaflow-ai/cmux` only; for the Go connection multiplexer by soheilhy, see that repo directly.

cmux exposes three primitives that the entire plugin ecosystem builds on: `CMUX_WORKSPACE_ID`, `CMUX_SURFACE_ID`, and `CMUX_SOCKET_PATH`. Every project below uses at least one of them.

---

## Quick Start

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

## "I want to..."

| Goal | Go to |
|------|-------|
| See agent status at a glance in the sidebar | [Sidebar & Status Pills](#1-sidebar--status-pills) |
| Know how long a task will take | [Progress Bars & Estimation](#2-progress-bars--estimation) |
| Watch agent activity in real time | [Sidebar Logs & Activity Feed](#3-sidebar-logs--activity-feed) |
| Get notified when an agent finishes or needs help | [Desktop Notifications](#4-desktop-notifications) |
| Run many agents in parallel | [Multi-Agent Orchestration](#5-multi-agent-orchestration) |
| Let agents browse the web | [Browser Automation](#6-browser-automation) |
| Give each agent its own git branch | [Worktrees & Workspace Management](#7-worktrees--workspace-management) |
| Recover sessions after a restart | [Monitoring & Session Restore](#8-monitoring--session-restore) |
| Control cmux from my phone or another machine | [Remote & Mobile Access](#9-remote--mobile-access) |
| Set up a beautiful multi-pane layout | [Themes, Layouts & Config](#10-themes-layouts--config) |
| Find plugins for a specific agent | [By Agent](#by-agent) |
| Run cmux on Windows or Linux | [Cross-Platform Ports](#cross-platform-ports) |
| Use something tmux-based instead | [Alternatives](#alternatives) |
| Build my own plugin | [Build Your Own Plugin](#build-your-own-plugin) |

---

## Contents

- [Feature Dimensions](#feature-dimensions) — primary navigation
  - [1. Sidebar & Status Pills](#1-sidebar--status-pills)
  - [2. Progress Bars & Estimation](#2-progress-bars--estimation)
  - [3. Sidebar Logs & Activity Feed](#3-sidebar-logs--activity-feed)
  - [4. Desktop Notifications](#4-desktop-notifications)
  - [5. Multi-Agent Orchestration](#5-multi-agent-orchestration)
  - [6. Browser Automation](#6-browser-automation)
  - [7. Worktrees & Workspace Management](#7-worktrees--workspace-management)
  - [8. Monitoring & Session Restore](#8-monitoring--session-restore)
  - [9. Remote & Mobile Access](#9-remote--mobile-access)
  - [10. Themes, Layouts & Config](#10-themes-layouts--config)
- [By Agent](#by-agent) — secondary navigation
  - [Claude Code](#claude-code)
  - [Pi](#pi)
  - [OpenCode](#opencode)
  - [Copilot & Amp](#copilot--amp)
- [Cross-Platform Ports](#cross-platform-ports)
- [Alternatives](#alternatives)
- [Build Your Own Plugin](#build-your-own-plugin)
- [Reference](#reference)

---

## Feature Dimensions

Repos appear in every section they are relevant to. If a project touches sidebar, notifications, and progress, it shows up in all three. This is intentional — browse by the feature you need, not by where someone decided to file it.

### 1. Sidebar & Status Pills

cmux's vertical sidebar is the primary surface for agent feedback. Plugins write status pills — small key-value pairs that appear next to each workspace tab. The best ones update on every lifecycle event so you can see model name, token count, thinking state, and active tool at a glance without switching tabs.

> **Recommended**: [yigitkonur/cmux-claude-pro](https://github.com/yigitkonur/cmux-claude-pro) for Claude Code (16 hooks, most complete), [kdcokenny/ocx](https://github.com/kdcokenny/ocx) for OpenCode (520 stars, production-proven), [HazAT/pi-config](https://github.com/HazAT/pi-config) for Pi (228 stars, full multi-agent setup).

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [yigitkonur/cmux-claude-pro](https://github.com/yigitkonur/cmux-claude-pro) | Claude Code | Wire sixteen lifecycle hooks into the cmux Unix socket for real-time status pills, adaptive progress bars, formatted log entries, git branch metadata, and subagent tracking | TypeScript |
| [HazAT/pi-config](https://github.com/HazAT/pi-config) | Pi | Push agent status, model, tokens, and active tool to cmux sidebar on every lifecycle event via a multi-agent architecture with planning, scouting, and review subagents | TypeScript · ★228 |
| [kdcokenny/ocx](https://github.com/kdcokenny/ocx) | OpenCode | Manage portable OpenCode configuration profiles with sidebar status, progress, logs, and flash triggers on every lifecycle event | TypeScript · ★520 |
| [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) | OpenCode | Bridge OpenCode lifecycle events to cmux sidebar with status pills, todo-driven progress, timeline logs, and unread marks scoped per workspace | TypeScript · ★23 |
| [tslateman/cmux-claude-code](https://github.com/tslateman/cmux-claude-code) | Claude Code | Update sidebar with live session status through five hooks showing thinking state, tool names with emoji labels, and logarithmic progress bar | Shell |
| [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) | Claude Code | Auto-rename workspace tabs to git repo names, show live progress bars, and include restraint rules for Claude Code sessions | Shell |
| [KyleJamesWalker/cc-cmux-plugin](https://github.com/KyleJamesWalker/cc-cmux-plugin) | Claude Code | Inject the full cmux command reference into every session, set active/idle sidebar status, and auto-grant cmux CLI permissions | — |
| [Mirksen/cmux-toolkit](https://github.com/Mirksen/cmux-toolkit) | Claude Code | Create an IDE-like workspace that auto-opens edited files in a Vim subpane and provides a toggleable broot file browser sidebar | Shell |
| [w-winter/dot314](https://github.com/w-winter/dot314) | Pi | Sync sidebar state, token and cost stats, workspace renaming, and attention notifications via a curated Pi extension collection | TypeScript · ★77 |
| [espennilsen/pi](https://github.com/espennilsen/pi) | Pi | Provide socket JSON-RPC integration with 7 LLM tools for workspace and browser control in a version-controlled Pi home directory | TypeScript · ★68 |
| [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) | Pi | Maintain four live sidebar pills (model, state, thinking, tokens) via a persistent socket client with context-aware notifications | TypeScript · ★14 |
| [joelhooks/pi-cmux](https://github.com/joelhooks/pi-cmux) | Pi | Provide 3-second sidebar heartbeat, AI session naming via Haiku, and worker mode for orchestrator-spawned subagents | TypeScript · ★9 |
| [Attamusc/pi-cmux](https://github.com/Attamusc/pi-cmux) | Pi | Surface agent activity with real-time tool execution status, needs-attention notifications, dynamic progress estimation, and render throttling | TypeScript |
| [sanurb/pi-cmux](https://github.com/sanurb/pi-cmux) | Pi | Integrate Pi with live sidebar status pills, focus-aware debounced macOS notifications, and a safe workspace tool with an explicit command allowlist | TypeScript |
| [simonjohansson/pi-cmux](https://github.com/simonjohansson/pi-cmux) | Pi | Extend Pi with a single configurable `cmux_cli` tool that passes any argv to cmux, plus sidebar status updates and completion notifications | TypeScript |
| [Attamusc/opencode-cmux](https://github.com/Attamusc/opencode-cmux) | OpenCode | Deliver socket JSON-RPC sidebar updates (~1-2ms latency) with render throttling, log rate limiting, and subagent detection | TypeScript |
| [Joehoel/opencode-cmux](https://github.com/Joehoel/opencode-cmux) | OpenCode | Combine an OpenCode plugin with Zsh integration polling Azure DevOps and Jira as additional sidebar pills | Shell |
| [tully-8888/opencode-cmux-notify-plugin](https://github.com/tully-8888/opencode-cmux-notify-plugin) | OpenCode | Set live sidebar status for active work, track subagent lifecycles, and send desktop notifications for questions, permissions, and errors | Shell |
| [Attamusc/copilot-cmux](https://github.com/Attamusc/copilot-cmux) | Copilot | Push Copilot CLI session activity into sidebar status pills, progress bars, logs, and desktop notifications via socket JSON-RPC | TypeScript |
| [block/cmux-amp](https://github.com/block/cmux-amp) | Amp | Display Amp agent status in the cmux sidebar using the Amp Plugin API with SF Symbol icons | TypeScript |
| [taichiiwamoto-s/cmux-context](https://github.com/taichiiwamoto-s/cmux-context) | Claude Code | Visualize context window usage across all workspaces as color-coded progress bars with model name, line counts, and rate limits | Shell |
| [gonzaloserrano/streamdeck-cmux](https://github.com/gonzaloserrano/streamdeck-cmux) | — | Display cmux workspace status, progress bars, and notification badges on Elgato Stream Deck hardware buttons | TypeScript · ★7 |
| [jaequery/cmux-diff](https://github.com/jaequery/cmux-diff) | Claude Code | Show a Cursor-style changes panel inside cmux's browser split with syntax-highlighted diffs and AI-generated commit messages | TypeScript |
| [azu/cmux-hub](https://github.com/azu/cmux-hub) | Claude Code | Provide a browser-based diff viewer with syntax highlighting, inline review comments, commit history, and GitHub PR/CI status integration | TypeScript · ★15 |
| [maedana/crmux](https://github.com/maedana/crmux) | Claude Code | Display a tmux-based sidebar with live status, permission mode, repo, branch, and worktree for all Claude Code sessions | Rust · ★20 |
| [wrock/wezterm-agent-cards](https://github.com/wrock/wezterm-agent-cards) | Claude Code | Add a curses-based sidebar to WezTerm displaying Claude Code sessions as stacked status cards with real-time state tracking | Python |
| [EtanHey/cmuxlayer](https://github.com/EtanHey/cmuxlayer) | Multi | Expose 22 MCP tools for sidebar status updates, progress indicators, split creation, screen reading, and multi-agent orchestration | TypeScript |
| [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) | Multi | Expose 81 MCP tools for spawning agents, sidebar metadata, notifications, browser automation, and session recovery | TypeScript |
| [eduwass/cru](https://github.com/eduwass/cru) | Claude Code | Arrange agent team workers into a grid layout with a 447-line cmux module featuring lifecycle phases with SF Symbols and progress-watcher | TypeScript |
| [bocktae80/cmux-pilot](https://github.com/bocktae80/cmux-pilot) | Claude Code | Manage workspace-to-session mappings, automatically syncing state on every prompt and enabling bulk resume after system restart | Shell |

### 2. Progress Bars & Estimation

Long-running agent tasks need visible progress. cmux's sidebar supports progress bars that fill from 0-100%. The best plugins estimate completion dynamically — some use logarithmic curves, others count completed todo items. Without progress bars, you are left guessing whether an agent is stuck or just thinking hard.

> **Recommended**: [yigitkonur/cmux-claude-pro](https://github.com/yigitkonur/cmux-claude-pro) for adaptive progress estimation, [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) for todo-driven progress tracking.

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [yigitkonur/cmux-claude-pro](https://github.com/yigitkonur/cmux-claude-pro) | Claude Code | Drive adaptive progress bars from sixteen lifecycle hooks, estimating completion based on tool execution patterns and session state | TypeScript |
| [tslateman/cmux-claude-code](https://github.com/tslateman/cmux-claude-code) | Claude Code | Render a logarithmic progress bar that accounts for diminishing returns in long-running sessions | Shell |
| [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) | Claude Code | Display live progress bars for long-running tasks alongside sidebar tab renaming and completion notifications | Shell |
| [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) | OpenCode | Track progress via todo completion counts, updating the sidebar bar as each item resolves | TypeScript · ★23 |
| [Attamusc/pi-cmux](https://github.com/Attamusc/pi-cmux) | Pi | Estimate progress dynamically with render throttling to avoid sidebar flicker | TypeScript |
| [Attamusc/copilot-cmux](https://github.com/Attamusc/copilot-cmux) | Copilot | Translate Copilot CLI tool execution stages into sidebar progress bar increments | TypeScript |
| [Attamusc/opencode-cmux](https://github.com/Attamusc/opencode-cmux) | OpenCode | Track tool execution and file edit counts to render estimated progress with rate limiting | TypeScript |
| [taichiiwamoto-s/cmux-context](https://github.com/taichiiwamoto-s/cmux-context) | Claude Code | Show context window fill percentage as color-coded progress bars across all workspaces | Shell |
| [hummer98/using-cmux](https://github.com/hummer98/using-cmux) | Claude Code | Teach Claude Code how to control sidebar progress bars as part of sub-agent lifecycle management | Shell · ★24 |
| [EtanHey/cmuxlayer](https://github.com/EtanHey/cmuxlayer) | Multi | Provide progress indicator MCP tools alongside 22 other workspace and agent management tools | TypeScript |
| [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) | Multi | Include progress tracking among 81 MCP tools for multi-agent workspace orchestration | TypeScript |
| [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) | Multi | Show elapsed time and live progress in a TUI widget while sub-agents execute in dedicated panes | TypeScript · ★251 |
| [hummer98/cmux-team](https://github.com/hummer98/cmux-team) | Claude Code | Display real-time progress for conductor and worker sub-agents managed by a task queue daemon | TypeScript · ★9 |
| [Joehoel/opencode-cmux](https://github.com/Joehoel/opencode-cmux) | OpenCode | Update sidebar progress bars from OpenCode sessions alongside Azure DevOps and Jira polling | Shell |
| [gonzaloserrano/streamdeck-cmux](https://github.com/gonzaloserrano/streamdeck-cmux) | — | Render progress bars on Stream Deck hardware buttons by reading workspace state from the cmux socket | TypeScript · ★7 |

### 3. Sidebar Logs & Activity Feed

The sidebar can show scrolling log entries — timestamped messages about what the agent is doing. Logs are essential for debugging: you can see which tools were called, which files were edited, and where errors occurred without switching to the agent's pane.

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [yigitkonur/cmux-claude-pro](https://github.com/yigitkonur/cmux-claude-pro) | Claude Code | Write formatted sidebar log entries for every lifecycle hook with timestamps, tool names, and git metadata | TypeScript |
| [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) | OpenCode | Maintain a timeline of agent events as sidebar log entries with unread marks per workspace | TypeScript · ★23 |
| [Attamusc/copilot-cmux](https://github.com/Attamusc/copilot-cmux) | Copilot | Log Copilot prompt submission, tool execution, and completion events to the sidebar feed | TypeScript |
| [Attamusc/opencode-cmux](https://github.com/Attamusc/opencode-cmux) | OpenCode | Rate-limit log entries to prevent sidebar flooding while tracking tool execution and file edits | TypeScript |
| [Joehoel/opencode-cmux](https://github.com/Joehoel/opencode-cmux) | OpenCode | Write agent event logs alongside Azure DevOps and Jira sidebar pills | Shell |
| [simonjohansson/pi-cmux](https://github.com/simonjohansson/pi-cmux) | Pi | Log tool executions from Pi sessions with slash command support for direct cmux access | TypeScript |
| [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) | Multi | Include structured log output among 81 MCP tools for multi-agent session management | TypeScript |
| [claude-studio/claude-studio](https://github.com/claude-studio/claude-studio) | Claude Code | Visualize cost, token, and session statistics on a dashboard by parsing JSONL transcripts from ~/.claude/projects | TypeScript |

### 4. Desktop Notifications

When an agent finishes a task, hits an error, or needs permission, you want to know immediately — even if cmux is behind another window. Plugins use `cmux notify` or OSC 777 escape sequences to fire native macOS notifications. The best ones are focus-aware: they stay quiet when you are already looking at the workspace.

> **Recommended**: [kdcokenny/opencode-notify](https://github.com/kdcokenny/opencode-notify) for OpenCode (standalone, 127 stars), [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) for Pi (context-aware summaries).

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [yigitkonur/cmux-claude-pro](https://github.com/yigitkonur/cmux-claude-pro) | Claude Code | Fire targeted desktop notifications on completion, errors, and attention events alongside 16-hook sidebar integration | TypeScript |
| [kdcokenny/opencode-notify](https://github.com/kdcokenny/opencode-notify) | OpenCode | Deliver native OS notifications on task completion, errors, and input needed, with click-to-foreground, quiet hours, and custom sounds | TypeScript · ★127 |
| [tslateman/cmux-claude-code](https://github.com/tslateman/cmux-claude-code) | Claude Code | Send desktop notifications on completion or attention events from five lifecycle hooks | Shell |
| [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) | Claude Code | Fire completion notifications alongside tab renaming and live progress bars | Shell |
| [KyleJamesWalker/cc-cmux-plugin](https://github.com/KyleJamesWalker/cc-cmux-plugin) | Claude Code | Route notifications through `cmux notify` with auto-granted CLI permissions | — |
| [HazAT/pi-config](https://github.com/HazAT/pi-config) | Pi | Deliver notifications as part of a full multi-agent architecture with cost tracking and subagent coordination | TypeScript · ★228 |
| [w-winter/dot314](https://github.com/w-winter/dot314) | Pi | Send attention notifications when the Pi agent needs input, alongside sidebar state sync and token stats | TypeScript · ★77 |
| [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) | Pi | Provide context-aware notifications summarizing agent actions with LLM-callable tools for targeted alerts | TypeScript · ★14 |
| [joelhooks/pi-cmux](https://github.com/joelhooks/pi-cmux) | Pi | Send native macOS notifications with attention-cycle tab indicators and auto-generated session names | TypeScript · ★9 |
| [Attamusc/pi-cmux](https://github.com/Attamusc/pi-cmux) | Pi | Show needs-attention notifications that auto-clear after ten seconds with render throttling | TypeScript |
| [sanurb/pi-cmux](https://github.com/sanurb/pi-cmux) | Pi | Deliver focus-aware debounced macOS notifications alongside live sidebar status pills | TypeScript |
| [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) | OpenCode | Notify on permission requests and subagent activity, scoped per workspace with unread marks | TypeScript · ★23 |
| [kdcokenny/opencode-workspace](https://github.com/kdcokenny/opencode-workspace) | OpenCode | Bundle OS notifications alongside planning, delegation, and worktree plugins in a 16-component harness | TypeScript · ★292 |
| [Joehoel/opencode-cmux](https://github.com/Joehoel/opencode-cmux) | OpenCode | Send desktop notifications on permission requests, errors, and completions from OpenCode sessions | Shell |
| [tully-8888/opencode-cmux-notify-plugin](https://github.com/tully-8888/opencode-cmux-notify-plugin) | OpenCode | Notify on questions, permissions, retries, and finish events with automatic stale-state clearing | Shell |
| [Attamusc/copilot-cmux](https://github.com/Attamusc/copilot-cmux) | Copilot | Translate Copilot CLI events into desktop notifications via socket JSON-RPC | TypeScript |
| [tadashi-aikawa/copilot-plugin-notify](https://github.com/tadashi-aikawa/copilot-plugin-notify) | Copilot | Emit OSC 777 notification escape sequences for tool-use approvals and agent-stop alerts with configurable allow/deny rules | Shell |
| [Th3Sp3ct3R/cmux-claude-agents](https://github.com/Th3Sp3ct3R/cmux-claude-agents) | Claude Code | Send completion notifications when redirected agent panes finish their work | Shell |
| [rappdw/zen-term](https://github.com/rappdw/zen-term) | Claude Code | Forward OSC 777 notification rings from a DGX Spark back to the local MacBook running cmux via Mosh | Shell |
| [hummer98/using-cmux](https://github.com/hummer98/using-cmux) | Claude Code | Teach Claude Code notification patterns as part of sub-agent workflow skills | Shell · ★24 |
| [itsmaleen/cmux-companion](https://github.com/itsmaleen/cmux-companion) | — | Mirror cmux notifications to an iPhone via a Go bridge server over LAN WebSocket | Go / Swift |
| [aannoo/hcom](https://github.com/aannoo/hcom) | Multi | Deliver cross-agent notifications and file-edit collision detection across Claude Code, Gemini CLI, Codex, and OpenCode | Rust · ★185 |
| [eduwass/cru](https://github.com/eduwass/cru) | Claude Code | Fire lifecycle phase notifications using SF Symbols as part of agent team grid management | TypeScript |
| [mspiegel31/opencode-cmux](https://github.com/mspiegel31/opencode-cmux) | OpenCode | Push desktop notifications on idle or error alongside subagent viewer panes and browser tools | TypeScript |
| [bjacobso/pimux](https://github.com/bjacobso/pimux) | Pi | Notify as part of a task state machine managing parallel Pi agents in worktrees | TypeScript |

### 5. Multi-Agent Orchestration

Running multiple agents in parallel is cmux's superpower. An orchestrator agent splits panes, launches workers, sends them tasks, and monitors their output via `read-screen`. The best frameworks handle the full lifecycle: spawn, dispatch, poll for completion, collect results, and tear down. This section includes both ready-to-use frameworks and skill files that teach your agent how to orchestrate.

> **Recommended**: [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) (251 stars, works across cmux/tmux/zellij), [dagster-io/erk](https://github.com/dagster-io/erk) for plan-oriented workflows with PR automation.

**Frameworks**

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) | Multi | Spawn async sub-agents in dedicated multiplexer panes across cmux, tmux, zellij, or WezTerm with a live TUI progress widget | TypeScript · ★251 |
| [aannoo/hcom](https://github.com/aannoo/hcom) | Multi | Connect agents across terminals with cross-agent messaging, file-collision detection, and notifications for Claude Code, Gemini, Codex, and OpenCode | Rust · ★185 |
| [dagster-io/erk](https://github.com/dagster-io/erk) | Claude Code | Create implementation plans from AI, execute in isolated git worktrees, and ship code via automated PR submission | Python · ★78 |
| [burggraf/pi-teams](https://github.com/burggraf/pi-teams) | Pi | Turn one Pi agent into a coordinated team with specialist teammates, shared task board, direct messaging, and plan approval | TypeScript · ★55 |
| [kdcokenny/opencode-workspace](https://github.com/kdcokenny/opencode-workspace) | OpenCode | Bundle 16 components for multi-agent orchestration with plan and build orchestrators, specialist agents, and MCP servers | TypeScript · ★292 |
| [hummer98/cmux-team](https://github.com/hummer98/cmux-team) | Claude Code | Run a task queue daemon that spawns visible conductor and worker sub-agents in cmux split panes with a TUI dashboard | TypeScript · ★9 |
| [bjacobso/pimux](https://github.com/bjacobso/pimux) | Pi | Manage parallel Pi agents via an Effect service with per-task workspaces, sidebar state machine, and diff review workflow | TypeScript |
| [eduwass/cru](https://github.com/eduwass/cru) | Claude Code | Arrange agent team workers into a grid layout across tmux, Ghostty, or cmux with labeled tabs for parallel feature work | TypeScript |
| [rjwittams/flotilla](https://github.com/rjwittams/flotilla) | Multi | Correlate branches, PRs, issues, and terminal agents across repos into unified work items via a TUI dashboard | Rust |
| [manaflow-ai/manaflow](https://github.com/manaflow-ai/manaflow) | Multi | Spawn Claude Code, Codex, Gemini, and other agents in parallel VS Code workspaces with git diff view and one-click PR creation | TypeScript · ★997 |

**MCP Servers**

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) | Multi | Expose 81 tools for full agent hierarchy, grid launchers, bulk dispatch, and session recovery | TypeScript |
| [EtanHey/cmuxlayer](https://github.com/EtanHey/cmuxlayer) | Multi | Provide 22 tools via socket (~0.1ms) or CLI fallback with an agent lifecycle engine | TypeScript |

**Orchestration Skills** (teach your agent how to orchestrate)

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [hummer98/using-cmux](https://github.com/hummer98/using-cmux) | Claude Code | Teach visible sub-agent lifecycle patterns: split, send, `read-screen`, status, notifications, and recovery | Shell · ★24 |
| [ygrec-app/supreme-leader-skill](https://github.com/ygrec-app/supreme-leader-skill) | Claude Code | Plan subtasks, spawn a 2-8 worker grid, monitor via `read-screen` polling, review deliverables, and dispatch fixes | Markdown |
| [umitaltintas/cmux-agent-toolkit](https://github.com/umitaltintas/cmux-agent-toolkit) | Claude Code | Teach fan-out execution with spawn, synchronize via `wait-for`/`wait-for --signal`, and pane topology management | Markdown |
| [baixianger/claude-orchestration-in-cmux](https://github.com/baixianger/claude-orchestration-in-cmux) | Claude Code | Coordinate parallel work via pane delegation with `cmux send`/`read-screen` through worktrees | Markdown |
| [Th3Sp3ct3R/cmux-claude-agents](https://github.com/Th3Sp3ct3R/cmux-claude-agents) | Claude Code | Intercept Agent tool calls via a `PreToolUse` hook and redirect to visible cmux split panes | Shell |
| [ygrec-app/offload-task-skill](https://github.com/ygrec-app/offload-task-skill) | Claude Code | Offload a single task to a split pane with an autonomous worker to preserve main session context | Markdown |
| [meengi07/cmux-agent-observer-skill](https://github.com/meengi07/cmux-agent-observer-skill) | Multi | Launch visible worker panes for Codex and OpenCode with optional tmux wrapping and browser helper | Shell |
| [halindrome/cmux-tmux-mapping-for-cc](https://github.com/halindrome/cmux-tmux-mapping-for-cc) | Claude Code | Detect tmux vs cmux and transparently route panel operations through the correct backend | Shell |
| [HazAT/pi-config](https://github.com/HazAT/pi-config) | Pi | Configure a multi-agent architecture with cmux-visible subagents for planning, scouting, coding, and reviewing | TypeScript · ★228 |
| [espennilsen/pi](https://github.com/espennilsen/pi) | Pi | Maintain 22 extensions including subagent delegation and project context switching for Pi | TypeScript · ★68 |
| [w-winter/dot314](https://github.com/w-winter/dot314) | Pi | Provide branch-out workflows, a command center, and multi-repo project navigation for Pi agents | TypeScript · ★77 |
| [joelhooks/pi-cmux](https://github.com/joelhooks/pi-cmux) | Pi | Offer a worker mode preventing fork bombs in orchestrator-spawned agents | TypeScript · ★9 |
| [sanurb/pi-cmux-workflows](https://github.com/sanurb/pi-cmux-workflows) | Pi | Add slash commands for splitting panes with new agent sessions and handing off task context between splits | TypeScript |
| [owizdom/context-brdige-for-cmux](https://github.com/owizdom/context-brdige-for-cmux) | Multi | Run a background daemon that extracts agent context, persists to SQLite, and auto-injects handoff briefs into new sessions | Go |
| [bocktae80/cmux-pilot](https://github.com/bocktae80/cmux-pilot) | Claude Code | Manage workspace-to-session mappings with `/cmux-ws` commands and bulk resume after restarts | Shell |
| [alaasdk/cmux-ctl](https://github.com/alaasdk/cmux-ctl) | Claude Code | Display a real-time TUI dashboard of all workspaces with keyboard-driven agent launching and input | Python |
| [jeremyeder/sisi-cmux](https://github.com/jeremyeder/sisi-cmux) | Claude Code | Auto-discover projects and build tmux workspaces with one-key Claude Code integration and checkpoint save/restore | TypeScript |

### 6. Browser Automation

cmux embeds a WebKit browser pane that agents can control via CLI. Plugins use `cmux browser` for navigation, DOM interaction, screenshots, form filling, and JavaScript evaluation. The best ones expose the full 40+ subcommand surface. This is how agents can visually verify their work, run E2E tests, or display rich content alongside the terminal.

> **Recommended**: [darkspock/cmux-skill](https://github.com/darkspock/cmux-skill) for the most complete browser skill (7 stars), [jasonraz/cmux-browser-mcp](https://github.com/jasonraz/cmux-browser-mcp) for MCP-based browser control (43 tools).

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [darkspock/cmux-skill](https://github.com/darkspock/cmux-skill) | Multi | Teach agents the full `cmux browser` surface: DOM interaction, JS eval, cookies, tabs, dialogs, and frames | Markdown · ★7 |
| [jasonraz/cmux-browser-mcp](https://github.com/jasonraz/cmux-browser-mcp) | Claude Code | Expose 43 MCP tools for full browser control: navigation, clicking, form filling, screenshots, JS eval, and network inspection | JavaScript · ★5 |
| [hashangit/cmux-skill](https://github.com/hashangit/cmux-skill) | Claude Code | Provide element-ref browser control via `snapshot --interactive`, notification decision matrix, and auto-wired hooks | Shell |
| [hoonkim/cmux-skills-plugin](https://github.com/hoonkim/cmux-skills-plugin) | Claude Code | Enable browser automation and pane control via `cmux tree`/`read-screen`/`send`, documented in Korean | Markdown |
| [storelayer/pi-cmux-browser](https://github.com/storelayer/pi-cmux-browser) | Pi | Equip Pi with dual browser modes: cmux in-app browser for visual debugging and Playwright for headless workflows | JavaScript |
| [sanurb/pi-cmux-browser](https://github.com/sanurb/pi-cmux-browser) | Pi | Give Pi typed browser automation tools with click, fill, screenshot, and snapshot actions plus a spawnable web-dev subagent | TypeScript |
| [mastertyko/pi-cmux-preview](https://github.com/mastertyko/pi-cmux-preview) | Pi | Render assistant Markdown as styled HTML in a cmux browser pane with inline terminal screenshots and file previews | TypeScript |
| [sanurb/pi-cmux-workflows](https://github.com/sanurb/pi-cmux-workflows) | Pi | Add ringi-powered code reviews displayed in cmux browser panes alongside split and handoff slash commands | TypeScript |
| [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) | Pi | Provide LLM-callable browser automation tools alongside sidebar pills and context-aware notifications | TypeScript · ★14 |
| [azu/cmux-hub](https://github.com/azu/cmux-hub) | Claude Code | Provide a diff viewer in a browser split with syntax highlighting, inline review comments, and GitHub CI status | TypeScript · ★15 |
| [monzou/mo-cmux](https://github.com/monzou/mo-cmux) | Claude Code | Preview Markdown files in a cmux browser split with live-reload and fuzzy filename matching | Shell |
| [doublezz10/figure-viewer](https://github.com/doublezz10/figure-viewer) | OpenCode | Display scientific figures in a cmux browser pane with lightbox zoom, freshness indicators, and auto-refresh | JavaScript |
| [RyoHirota68/cmux-pencil-preview](https://github.com/RyoHirota68/cmux-pencil-preview) | Claude Code | Auto-export and hot-reload Pencil design PDF previews in the browser pane during design iterations | Shell |
| [jaequery/cmux-diff](https://github.com/jaequery/cmux-diff) | Claude Code | Show syntax-highlighted diffs with Shiki in a browser split with multi-file selection and AI commit messages | TypeScript |
| [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) | Claude Code | Open browser splits for UI verification alongside tab renaming, progress bars, and completion notifications | Shell |
| [mangledmonkey/cmux-skills](https://github.com/mangledmonkey/cmux-skills) | Claude Code | Teach Claude Code browser automation with form filling, screenshots, and debug window capture via four auto-syncing skills | Shell |
| [mikecfisher/cmux-skill](https://github.com/mikecfisher/cmux-skill) | Claude Code | Cover browser automation as part of a comprehensive CLI taxonomy documenting `capture-pane` and `CMUX_SOCKET_PASSWORD` | Markdown |
| [Stealinglight/cmux-claude-code-skill](https://github.com/Stealinglight/cmux-claude-code-skill) | Claude Code | Provide deep browser, CLI, and shortcuts references with Python socket API examples for WebKit automation | Shell |
| [goddaehee/cmux-claude-skill](https://github.com/goddaehee/cmux-claude-skill) | Claude Code | Teach the full 40+ browser subcommands alongside workspace navigation and tmux migration mapping, documented in Korean | Markdown |
| [mspiegel31/opencode-cmux](https://github.com/mspiegel31/opencode-cmux) | OpenCode | Expose optional `cmux browser` tools to the AI agent alongside subagent viewer panes and notifications | TypeScript |
| [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) | Multi | Include browser automation among 81 MCP tools for multi-agent workspace orchestration | TypeScript |
| [EtanHey/cmuxlayer](https://github.com/EtanHey/cmuxlayer) | Multi | Provide browser control tools alongside 22 other MCP tools for workspace management | TypeScript |

### 7. Worktrees & Workspace Management

Git worktrees give each agent an isolated copy of the repository on a separate branch — no merge conflicts, no stepping on each other's changes. The best plugins create a worktree, open a cmux workspace for it, launch an agent inside, and clean up when the branch merges. This is the foundation for safe parallel development.

> **Recommended**: [kdcokenny/opencode-worktree](https://github.com/kdcokenny/opencode-worktree) (392 stars, most popular), [craigsc/cmux](https://github.com/craigsc/cmux) (477 stars, tmux-based but the gold standard for worktree UX), [aschreifels/cwt](https://github.com/aschreifels/cwt) for Claude Code with ticket integration.

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [kdcokenny/opencode-worktree](https://github.com/kdcokenny/opencode-worktree) | OpenCode | Create isolated git worktrees where each spawns its own terminal with OpenCode, syncs files via hooks, and auto-commits on deletion | TypeScript · ★392 |
| [craigsc/cmux](https://github.com/craigsc/cmux) | Claude Code | Wrap git worktree lifecycle into single commands with isolated directories, shared git history, tab completion, and merge/teardown | Shell · ★477 |
| [aschreifels/cwt](https://github.com/aschreifels/cwt) | Claude Code | Create worktrees with full cmux dev environments, ticket integration from Linear/GitHub/Jira, draft mode, and a TUI wizard | Go |
| [bhandeland/fleet](https://github.com/bhandeland/fleet) | Claude Code | Manage worktree lifecycles for parallel Claude Code sessions with sidebar status, team spawning, and one-command merge-back | Shell |
| [tasuku43/kra](https://github.com/tasuku43/kra) | Claude Code | Map tickets one-to-one with cmux workspaces on the filesystem, auto-creating or removing sessions as tasks open and close | Go |
| [eunjae-lee/cmux-worktree](https://github.com/eunjae-lee/cmux-worktree) | — | Provide a YAML-based workspace provider with worktree creation, custom workflows, split layouts, and isolated browser storage | TypeScript |
| [dagster-io/erk](https://github.com/dagster-io/erk) | Claude Code | Execute implementation plans in isolated worktrees with `cmux checkout`/`cmux teleport` and automated PR submission | Python · ★78 |
| [bjacobso/pimux](https://github.com/bjacobso/pimux) | Pi | Give each parallel Pi agent its own worktree and workspace with sidebar status and a diff review workflow | TypeScript |
| [javiermolinar/pi-cmux](https://github.com/javiermolinar/pi-cmux) | Pi | Provide git worktree branching with handoff context alongside 12+ slash commands for splits and zoxide jumps | TypeScript · ★6 |
| [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) | Claude Code | Create workspaces for git worktrees alongside tab renaming, progress bars, and browser splits | Shell |
| [baixianger/claude-orchestration-in-cmux](https://github.com/baixianger/claude-orchestration-in-cmux) | Claude Code | Coordinate parallel work by creating git worktrees and managing merge cycles via pane delegation | Markdown |
| [Stealinglight/cmux-claude-code-skill](https://github.com/Stealinglight/cmux-claude-code-skill) | Claude Code | Teach Claude Code to create worktree-based isolated sessions alongside browser, sidebar, and notification skills | Shell |
| [rjwittams/flotilla](https://github.com/rjwittams/flotilla) | Multi | Correlate branches, PRs, and issues across repos with agent hook integration for worktree management | Rust |
| [Kaldy14/clui](https://github.com/Kaldy14/clui) | Claude Code | Wrap Claude Code in an Electron app with a git worktree per conversation thread and LRU hibernation | TypeScript |
| [kdcokenny/opencode-workspace](https://github.com/kdcokenny/opencode-workspace) | OpenCode | Include git worktree isolation among 16 bundled OpenCode components with multi-agent orchestration | TypeScript · ★292 |
| [wwaIII/proj](https://github.com/wwaIII/proj) | Claude Code | Launch named cmux workspaces from a TUI project picker with `[CC]` activity badges | Rust |

### 8. Monitoring & Session Restore

Agents can run for hours. When cmux restarts, crashes, or you close the lid, you need to pick up exactly where you left off. Session restore plugins snapshot running sessions and recreate them. Monitoring plugins give you a bird's-eye view of what every agent is doing across all workspaces.

> **Recommended**: [STRML/cmux-restore](https://github.com/STRML/cmux-restore) for Claude Code session mapping, [drolosoft/cmux-resurrect](https://github.com/drolosoft/cmux-resurrect) for full workspace restore with Markdown blueprints.

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [AtAFork/ghostty-claude-code-session-restore](https://github.com/AtAFork/ghostty-claude-code-session-restore) | Claude Code | Snapshot sessions every 2 seconds via launchd, resolve session IDs, and restore into correct cmux surfaces on relaunch | Python · ★22 |
| [STRML/cmux-restore](https://github.com/STRML/cmux-restore) | Claude Code | Map each Claude Code session ID to its surface UUID via a `SessionStart` hook and resume exact sessions after cmux restarts | Shell |
| [drolosoft/cmux-resurrect](https://github.com/drolosoft/cmux-resurrect) | — | Save and restore workspaces, splits, CWDs, commands, and Markdown workspace blueprints with dry-run preview | Go |
| [owizdom/context-brdige-for-cmux](https://github.com/owizdom/context-brdige-for-cmux) | Multi | Poll panes, extract structured context, persist to SQLite, and auto-inject compressed handoff briefs into new sessions | Go |
| [alaasdk/cmux-ctl](https://github.com/alaasdk/cmux-ctl) | Claude Code | Display a real-time Textual TUI dashboard of all workspaces with agent state tracking and notification badges | Python |
| [taichiiwamoto-s/cmux-context](https://github.com/taichiiwamoto-s/cmux-context) | Claude Code | Scrape Claude status bars from every workspace and render a context-fill dashboard with model and rate limit info | Shell |
| [ensarkovankaya/cmux-mirror](https://github.com/ensarkovankaya/cmux-mirror) | — | Mirror a remote cmux layout to a local instance over SSH with incremental sync support | Python |
| [bocktae80/cmux-pilot](https://github.com/bocktae80/cmux-pilot) | Claude Code | Enable bulk resume of all workspace sessions after system restart via workspace-to-session mapping | Shell |
| [claude-studio/claude-studio](https://github.com/claude-studio/claude-studio) | Claude Code | Parse JSONL transcripts to visualize cost, token, and session statistics on a dashboard with live agent state | TypeScript |
| [maedana/crmux](https://github.com/maedana/crmux) | Claude Code | Show live status, permission mode, repo, branch, and worktree for all Claude Code sessions in a tmux sidebar | Rust · ★20 |
| [gonzaloserrano/streamdeck-cmux](https://github.com/gonzaloserrano/streamdeck-cmux) | — | Read workspace state from the cmux socket and display it on Stream Deck hardware buttons | TypeScript · ★7 |
| [wrock/wezterm-agent-cards](https://github.com/wrock/wezterm-agent-cards) | Claude Code | Display real-time color-coded status cards for Claude Code sessions in a WezTerm sidebar | Python |
| [theforager/cmux](https://github.com/theforager/cmux) | Claude Code | Provide an interactive tmux session selector with real-time status indicators optimized for mobile SSH | Shell |
| [rjwittams/flotilla](https://github.com/rjwittams/flotilla) | Multi | Correlate agents, branches, and PRs across repos into unified work items via a TUI dashboard | Rust |
| [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) | Multi | Show a live TUI widget with elapsed time and progress while sub-agents execute across multiplexers | TypeScript · ★251 |
| [hummer98/cmux-team](https://github.com/hummer98/cmux-team) | Claude Code | Monitor conductor and worker sub-agents in real time via a TUI dashboard connected to a task queue daemon | TypeScript · ★9 |
| [meengi07/cmux-agent-observer-skill](https://github.com/meengi07/cmux-agent-observer-skill) | Multi | Track worker progress from the cmux sidebar with structured handoff notes in a dedicated directory | Shell |

### 9. Remote & Mobile Access

Sometimes you need to check on your agents from another room — or another device entirely. These projects bridge cmux to mobile apps, web browsers, and SSH sessions.

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [hummer98/cmux-remote](https://github.com/hummer98/cmux-remote) | — | Provide a self-hosted PWA bridge for remote workspace viewing and surface switching over WebSocket with xterm.js rendering | TypeScript |
| [itsmaleen/cmux-companion](https://github.com/itsmaleen/cmux-companion) | — | Mirror notifications to an iPhone app with volume-button workspace cycling, voice commands, and landscape-optimized navigation | Go / Swift |
| [ensarkovankaya/cmux-mirror](https://github.com/ensarkovankaya/cmux-mirror) | — | Mirror remote cmux workspace and pane structure to a local instance over SSH | Python |
| [rappdw/zen-term](https://github.com/rappdw/zen-term) | Claude Code | Connect a MacBook running cmux to a DGX Spark via Mosh with Zellij layouts and OSC 777 notification rings | Shell |
| [theforager/cmux](https://github.com/theforager/cmux) | Claude Code | Provide a mobile-friendly tmux session selector with compact columns designed for Terminus on iOS | Shell |

### 10. Themes, Layouts & Config

The right layout turns cmux from a terminal into a development cockpit. Three-pane setups with a file browser, agent, and git sidebar are popular. Themes set the mood; config tweaks (scrollback, opacity, key bindings) make everything feel right.

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [jacobtellep/cmux-setup](https://github.com/jacobtellep/cmux-setup) | Claude Code | Replicate Conductor's IDE-style 3-pane layout (Claude + lazygit + dev server) with a dark-teal theme in one command | Shell |
| [budah1987/cmux-script](https://github.com/budah1987/cmux-script) | Claude Code | Launch from an interactive project picker with yazi + lazygit + Claude Code in a 3-pane layout with auto-started dev servers | Shell |
| [rappdw/zen-term](https://github.com/rappdw/zen-term) | Claude Code | Configure a reproducible environment with three Zellij layouts, Mosh remote connection, and dynamic agent status indicators | Shell |
| [chrisliu298/ghostty-config](https://github.com/chrisliu298/ghostty-config) | — | Share a GitHub Dark theme with Berkeley Mono 18pt, 128 MiB scrollback, and cmux-ready keybinds | — |
| [jcyamacho/zdotfiles](https://github.com/jcyamacho/zdotfiles) | — | Provide a Zsh framework with Antidote, Starship, and install helpers for cmux, fzf, zoxide, and git-worktree utilities | Zsh |
| [karlorz/dev-docs-cmux](https://github.com/karlorz/dev-docs-cmux) | — | Fetch and maintain LLM-optimized documentation for common cmux dependencies via a make-driven workflow | Shell |
| [Mirksen/cmux-toolkit](https://github.com/Mirksen/cmux-toolkit) | Claude Code | Open edited files in a Vim subpane and provide a toggleable broot file browser sidebar per Claude session | Shell |
| [javiermolinar/pi-cmux](https://github.com/javiermolinar/pi-cmux) | Pi | Offer 12+ slash commands for vertical/horizontal splits, zoxide jumps, and PR review panes | TypeScript · ★6 |
| [stevenocchipinti/raycast-cmux](https://github.com/stevenocchipinti/raycast-cmux) | — | Search, navigate, and manage cmux workspaces and surfaces from Raycast without touching the mouse | TypeScript |
| [wwaIII/proj](https://github.com/wwaIII/proj) | Claude Code | Browse and select projects from a TUI picker to launch named cmux workspaces with activity badges | Rust |
| [drolosoft/cmux-resurrect](https://github.com/drolosoft/cmux-resurrect) | — | Save and restore workspace layouts from Markdown blueprints that are Obsidian-compatible and versionable | Go |
| [eunjae-lee/cmux-worktree](https://github.com/eunjae-lee/cmux-worktree) | — | Define workspace layouts in YAML with split panes, suspended tabs, and isolated browser storage per worktree | TypeScript |
| [wolffiex/cmux](https://github.com/wolffiex/cmux) | — | Manage tmux layouts through a popup UI with a visual carousel, 10 preset layouts, and AI-powered window summaries | TypeScript |
| [jhta/cmux-skill](https://github.com/jhta/cmux-skill) | Claude Code | Teach Claude Code Neovim + git diff patterns: open files, delta diffs, and run tests in adjacent panes | Shell |
| [blueraai/bluera-base](https://github.com/blueraai/bluera-base) | Claude Code | Provide shared conventions with multi-language `PostToolUse` validation hooks and automatic quality gates | Shell |
| [budah1987/homebrew-tools](https://github.com/budah1987/homebrew-tools) | Claude Code | Install the cmux workspace launcher via Homebrew with dependency management for yazi, lazygit, and dev tools | Ruby |
| [anhoder/homebrew-repo](https://github.com/anhoder/homebrew-repo) | — | Distribute a `cmux-nightly` cask via Homebrew tap from GitHub releases | Ruby |
| [KyleJamesWalker/cc-cmux-plugin](https://github.com/KyleJamesWalker/cc-cmux-plugin) | Claude Code | Inject cmux command reference into every session and auto-grant CLI permissions alongside sidebar status | — |
| [danneu/danterm](https://github.com/danneu/danterm) | — | Provide a macOS terminal on libghostty with vertical tabs, split panes, collapsible tab groups, and JSON-based layout restore | Swift |
| [davis7dotsh/my-term](https://github.com/davis7dotsh/my-term) | — | Prototype a native macOS terminal with an Arc-style persistent sidebar and long-lived sessions using SwiftTerm | Swift |

---

## By Agent

Cross-reference tables organized by the agent you use. Tags tell you which features each repo covers so you can pick exactly what you need.

### Claude Code

**Hooks & Sidebar Plugins**

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [yigitkonur/cmux-claude-pro](https://github.com/yigitkonur/cmux-claude-pro) | `sidebar` `progress` `logs` `notify` `monitor` | Wire sixteen lifecycle hooks into cmux for real-time status pills, adaptive progress bars, formatted log entries, git metadata, and subagent tracking | TypeScript |
| [tslateman/cmux-claude-code](https://github.com/tslateman/cmux-claude-code) | `sidebar` `progress` `notify` | Update sidebar with live status through five hooks: thinking state, emoji tool names, logarithmic progress bar, and desktop notifications | Shell |
| [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) | `sidebar` `notify` `progress` `browser` `worktree` | Auto-rename tabs to repo names, notify on completion, display progress bars, open browser splits, and create worktree workspaces | Shell |
| [KyleJamesWalker/cc-cmux-plugin](https://github.com/KyleJamesWalker/cc-cmux-plugin) | `sidebar` `notify` `config` | Inject cmux command reference, set active/idle sidebar status, route notifications, and auto-grant permissions | — |
| [Mirksen/cmux-toolkit](https://github.com/Mirksen/cmux-toolkit) | `layout` `sidebar` | Create an IDE-like workspace with auto-opening Vim subpane and toggleable broot file browser | Shell |
| [bocktae80/cmux-pilot](https://github.com/bocktae80/cmux-pilot) | `sidebar` `orchestrate` `config` | Manage workspace-to-session mappings with bulk resume after restart, documented in Korean | Shell |
| [taichiiwamoto-s/cmux-context](https://github.com/taichiiwamoto-s/cmux-context) | `sidebar` `progress` `monitor` | Visualize context window usage across all workspaces as color-coded progress bars | Shell |
| [eduwass/cru](https://github.com/eduwass/cru) | `orchestrate` `sidebar` `layout` | Arrange agent team workers into grid layouts with lifecycle phases, SF Symbols, and progress-watcher | TypeScript |
| [azu/cmux-hub](https://github.com/azu/cmux-hub) | `browser` `sidebar` `monitor` | Provide a browser-based diff viewer with syntax highlighting, review comments, and GitHub CI status | TypeScript · ★15 |
| [jaequery/cmux-diff](https://github.com/jaequery/cmux-diff) | `browser` `sidebar` | Show syntax-highlighted diffs in a browser split with AI-generated commit messages | TypeScript |

**Skills** (reference docs that teach Claude Code how to use cmux)

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [darkspock/cmux-skill](https://github.com/darkspock/cmux-skill) | `browser` `skill` | Cover the full `cmux browser` surface: DOM, JS eval, cookies, tabs, dialogs, and frames | Markdown · ★7 |
| [hashangit/cmux-skill](https://github.com/hashangit/cmux-skill) | `browser` `notify` `sidebar` `skill` | Provide element-ref browser control, notification decision matrix, and auto-wired hooks | Shell |
| [hoonkim/cmux-skills-plugin](https://github.com/hoonkim/cmux-skills-plugin) | `browser` `skill` | Enable browser automation and pane control via `cmux tree`/`read-screen`/`send`, in Korean | Markdown |
| [Stealinglight/cmux-claude-code-skill](https://github.com/Stealinglight/cmux-claude-code-skill) | `browser` `layout` `sidebar` `notify` `worktree` | Provide deep CLI, browser, and shortcuts references with Python socket API examples | Shell |
| [mikecfisher/cmux-skill](https://github.com/mikecfisher/cmux-skill) | `layout` `browser` `skill` | Cover the full CLI taxonomy including `capture-pane` alias and `CMUX_SOCKET_PASSWORD` | Markdown |
| [mangledmonkey/cmux-skills](https://github.com/mangledmonkey/cmux-skills) | `layout` `browser` `skill` | Teach pane topology, browser forms, markdown panels, and debug snapshots via four auto-syncing skills | Shell |
| [jhta/cmux-skill](https://github.com/jhta/cmux-skill) | `layout` `skill` `notify` | Teach Neovim + git diff patterns: open files, delta diffs, run tests in adjacent panes | Shell |
| [goddaehee/cmux-claude-skill](https://github.com/goddaehee/cmux-claude-skill) | `browser` `sidebar` `notify` `skill` | Cover the full CLI reference, 40+ browser subcommands, and tmux migration mapping, in Korean | Markdown |
| [halindrome/cmux-tmux-mapping-for-cc](https://github.com/halindrome/cmux-tmux-mapping-for-cc) | `layout` `orchestrate` | Detect tmux vs cmux and route panel operations through the correct backend | Shell |
| [hummer98/using-cmux](https://github.com/hummer98/using-cmux) | `layout` `notify` `sidebar` `progress` `skill` | Teach sub-agent lifecycle: split, send, read-screen, status, notifications, and recovery | Shell · ★24 |
| [umitaltintas/cmux-agent-toolkit](https://github.com/umitaltintas/cmux-agent-toolkit) | `orchestrate` `browser` `sidebar` `skill` | Teach fan-out execution, browser automation, sidebar updates, and wait-for signal synchronization | Markdown |
| [baixianger/claude-orchestration-in-cmux](https://github.com/baixianger/claude-orchestration-in-cmux) | `orchestrate` `worktree` `skill` | Coordinate parallel work via pane delegation, worktree creation, and merge cycle management | Markdown |
| [ygrec-app/supreme-leader-skill](https://github.com/ygrec-app/supreme-leader-skill) | `orchestrate` `monitor` `skill` | Plan subtasks, spawn 2-8 workers, monitor via polling, review deliverables, and dispatch fixes | Markdown |
| [ygrec-app/offload-task-skill](https://github.com/ygrec-app/offload-task-skill) | `orchestrate` `skill` | Offload a task to a split pane with an autonomous worker to preserve main session context | Markdown |

**Orchestration & Worktrees**

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [dagster-io/erk](https://github.com/dagster-io/erk) | `orchestrate` `worktree` | Create plans from AI, execute in isolated worktrees, and ship via automated PR submission | Python · ★78 |
| [hummer98/cmux-team](https://github.com/hummer98/cmux-team) | `orchestrate` `layout` `monitor` `progress` | Run a task queue daemon with conductor and worker sub-agents in split panes | TypeScript · ★9 |
| [Th3Sp3ct3R/cmux-claude-agents](https://github.com/Th3Sp3ct3R/cmux-claude-agents) | `orchestrate` `layout` `notify` | Intercept Agent tool calls via `PreToolUse` and redirect to visible cmux panes | Shell |
| [craigsc/cmux](https://github.com/craigsc/cmux) | `worktree` `orchestrate` | Wrap git worktree lifecycle into `cmux new <branch>` with tab completion and merge/teardown | Shell · ★477 |
| [aschreifels/cwt](https://github.com/aschreifels/cwt) | `worktree` `layout` `notify` `orchestrate` | Create worktrees with full cmux dev environments, ticket integration, and a TUI wizard | Go |
| [bhandeland/fleet](https://github.com/bhandeland/fleet) | `worktree` `sidebar` `orchestrate` `layout` | Manage worktree lifecycles with agent team spawning and one-command merge-back | Shell |
| [tasuku43/kra](https://github.com/tasuku43/kra) | `worktree` `orchestrate` | Map tickets to cmux workspaces, auto-creating or removing sessions as tasks change | Go |
| [Kaldy14/clui](https://github.com/Kaldy14/clui) | `layout` `worktree` | Wrap Claude Code in Electron with per-thread worktrees, resume support, and LRU hibernation | TypeScript |

**Session Restore & Monitoring**

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [AtAFork/ghostty-claude-code-session-restore](https://github.com/AtAFork/ghostty-claude-code-session-restore) | `monitor` | Snapshot sessions every 2s via launchd and restore into correct cmux surfaces on relaunch | Python · ★22 |
| [STRML/cmux-restore](https://github.com/STRML/cmux-restore) | `monitor` `layout` | Map session IDs to surface UUIDs and resume exact sessions after cmux restarts | Shell |
| [alaasdk/cmux-ctl](https://github.com/alaasdk/cmux-ctl) | `monitor` `notify` `orchestrate` | Display a real-time TUI dashboard with agent state tracking and keyboard-driven launching | Python |
| [claude-studio/claude-studio](https://github.com/claude-studio/claude-studio) | `monitor` `logs` | Visualize cost, token, and session statistics by parsing JSONL transcripts on a dashboard | TypeScript |
| [maedana/crmux](https://github.com/maedana/crmux) | `monitor` `sidebar` `layout` | Show live status for all Claude Code sessions in a tmux sidebar with vim-like navigation | Rust · ★20 |
| [wrock/wezterm-agent-cards](https://github.com/wrock/wezterm-agent-cards) | `sidebar` `monitor` | Display sessions as stacked status cards in WezTerm with real-time state tracking | Python |
| [theforager/cmux](https://github.com/theforager/cmux) | `layout` `monitor` | Provide an interactive tmux session selector with live status, optimized for mobile SSH | Shell |

**Layout & Config**

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [jacobtellep/cmux-setup](https://github.com/jacobtellep/cmux-setup) | `layout` `config` | Replicate Conductor's 3-pane layout with Claude + lazygit + dev server in one command | Shell |
| [budah1987/cmux-script](https://github.com/budah1987/cmux-script) | `layout` `sidebar` | Launch from a project picker with yazi + lazygit + Claude Code in 3 panes | Shell |
| [rappdw/zen-term](https://github.com/rappdw/zen-term) | `notify` `layout` `monitor` | Configure Mosh + Zellij layouts connecting MacBook to DGX Spark with OSC 777 notifications | Shell |
| [blueraai/bluera-base](https://github.com/blueraai/bluera-base) | `skill` `config` | Provide shared conventions with multi-language PostToolUse validation hooks and quality gates | Shell |
| [monzou/mo-cmux](https://github.com/monzou/mo-cmux) | `browser` | Preview Markdown files in a cmux browser split with live-reload and fuzzy matching | Shell |
| [RyoHirota68/cmux-pencil-preview](https://github.com/RyoHirota68/cmux-pencil-preview) | `browser` | Auto-export and hot-reload Pencil design PDF previews in the browser pane | Shell |
| [wwaIII/proj](https://github.com/wwaIII/proj) | `layout` `config` | Launch named cmux workspaces from a TUI project picker with activity badges | Rust |
| [budah1987/homebrew-tools](https://github.com/budah1987/homebrew-tools) | `layout` `config` | Install the workspace launcher via Homebrew with dependency management | Ruby |
| [jeremyeder/sisi-cmux](https://github.com/jeremyeder/sisi-cmux) | `layout` `orchestrate` | Auto-discover projects and build tmux workspaces with Claude Code integration and checkpoint save | TypeScript |

### Pi

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [HazAT/pi-config](https://github.com/HazAT/pi-config) | `orchestrate` `sidebar` `notify` `browser` `skill` | Configure a multi-agent architecture with cmux-visible subagents for planning, scouting, coding, and reviewing | TypeScript · ★228 |
| [w-winter/dot314](https://github.com/w-winter/dot314) | `sidebar` `notify` `orchestrate` `skill` `config` | Provide a curated extension collection with session management, model-aware compaction, and multi-repo command center | TypeScript · ★77 |
| [espennilsen/pi](https://github.com/espennilsen/pi) | `sidebar` `browser` `orchestrate` `skill` `config` | Maintain 22 Pi extensions including subagent delegation, changelogs, handoffs, and project context switching | TypeScript · ★68 |
| [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) | `orchestrate` `layout` `progress` `monitor` | Spawn async sub-agents in multiplexer panes with a live TUI progress widget across cmux, tmux, and zellij | TypeScript · ★251 |
| [burggraf/pi-teams](https://github.com/burggraf/pi-teams) | `orchestrate` `layout` `notify` | Turn one Pi agent into a coordinated team with shared task board, messaging, and plan approval | TypeScript · ★55 |
| [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) | `sidebar` `notify` `browser` `layout` | Provide context-aware notifications, 4 live sidebar pills, and LLM-callable browser automation tools | TypeScript · ★14 |
| [joelhooks/pi-cmux](https://github.com/joelhooks/pi-cmux) | `sidebar` `notify` `orchestrate` | Deliver 3s heartbeat, AI session naming, macOS notifications, and worker mode for subagent safety | TypeScript · ★9 |
| [javiermolinar/pi-cmux](https://github.com/javiermolinar/pi-cmux) | `layout` `notify` `worktree` `skill` | Provide 12+ slash commands for splits, zoxide jumps, worktree branching, and PR review panes | TypeScript · ★6 |
| [bjacobso/pimux](https://github.com/bjacobso/pimux) | `orchestrate` `worktree` `sidebar` `notify` `monitor` | Orchestrate parallel agents with per-task worktrees, sidebar state machine, and diff review workflow | TypeScript |
| [Attamusc/pi-cmux](https://github.com/Attamusc/pi-cmux) | `sidebar` `notify` `progress` | Surface real-time tool status, needs-attention alerts, and dynamic progress estimation with render throttling | TypeScript |
| [sanurb/pi-cmux](https://github.com/sanurb/pi-cmux) | `sidebar` `notify` `layout` | Integrate with live sidebar pills, focus-aware notifications, and a safe workspace command allowlist | TypeScript |
| [simonjohansson/pi-cmux](https://github.com/simonjohansson/pi-cmux) | `sidebar` `notify` `logs` | Extend Pi with a configurable `cmux_cli` tool, sidebar status updates, and tool execution logging | TypeScript |
| [storelayer/pi-cmux-browser](https://github.com/storelayer/pi-cmux-browser) | `browser` | Equip Pi with dual browser modes: cmux in-app for visual debugging, Playwright for headless workflows | JavaScript |
| [sanurb/pi-cmux-browser](https://github.com/sanurb/pi-cmux-browser) | `browser` | Give Pi typed browser automation tools with click, fill, screenshot, and a spawnable web-dev subagent | TypeScript |
| [sanurb/pi-cmux-workflows](https://github.com/sanurb/pi-cmux-workflows) | `layout` `browser` `orchestrate` | Add slash commands for splits, handoffs, and ringi code reviews in cmux browser panes | TypeScript |
| [mastertyko/pi-cmux-preview](https://github.com/mastertyko/pi-cmux-preview) | `browser` | Render assistant Markdown as styled HTML in a browser pane with screenshot capture | TypeScript |

### OpenCode

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [kdcokenny/ocx](https://github.com/kdcokenny/ocx) | `sidebar` `notify` `config` | Manage portable configuration profiles with sidebar status, progress, and flash triggers on lifecycle events | TypeScript · ★520 |
| [kdcokenny/opencode-worktree](https://github.com/kdcokenny/opencode-worktree) | `worktree` `layout` | Create isolated git worktrees that auto-spawn terminals with OpenCode, sync files, and auto-commit on deletion | TypeScript · ★392 |
| [kdcokenny/opencode-workspace](https://github.com/kdcokenny/opencode-workspace) | `orchestrate` `notify` `worktree` `mcp` `skill` | Bundle 16 components for multi-agent orchestration, specialist agents, OS notifications, and worktree isolation | TypeScript · ★292 |
| [kdcokenny/opencode-notify](https://github.com/kdcokenny/opencode-notify) | `notify` | Deliver native OS notifications with click-to-foreground, quiet hours, custom sounds, and optional cmux fallback | TypeScript · ★127 |
| [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) | `sidebar` `notify` `logs` | Bridge lifecycle events to status pills, todo-driven progress, timeline logs, and unread marks per workspace | TypeScript · ★23 |
| [Attamusc/opencode-cmux](https://github.com/Attamusc/opencode-cmux) | `sidebar` `notify` `logs` `progress` | Deliver socket JSON-RPC updates with render throttling, log rate limiting, and subagent detection | TypeScript |
| [Joehoel/opencode-cmux](https://github.com/Joehoel/opencode-cmux) | `sidebar` `progress` `notify` `logs` | Combine a plugin with Zsh integration polling Azure DevOps and Jira as sidebar pills | Shell |
| [mspiegel31/opencode-cmux](https://github.com/mspiegel31/opencode-cmux) | `sidebar` `notify` `browser` `monitor` | Display subagent sessions in TUI panes, push notifications on idle/error, and expose browser tools | TypeScript |
| [tully-8888/opencode-cmux-notify-plugin](https://github.com/tully-8888/opencode-cmux-notify-plugin) | `sidebar` `notify` `monitor` | Set live status, track subagent lifecycles, and notify on questions, permissions, and errors | Shell |
| [doublezz10/figure-viewer](https://github.com/doublezz10/figure-viewer) | `browser` | Display scientific figures in a browser pane with lightbox zoom, auto-refresh, and a slash command | JavaScript |

### Copilot & Amp

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [Attamusc/copilot-cmux](https://github.com/Attamusc/copilot-cmux) | `sidebar` `notify` `logs` `progress` | Push Copilot CLI activity into sidebar status pills, progress bars, logs, and desktop notifications | TypeScript |
| [tadashi-aikawa/copilot-plugin-notify](https://github.com/tadashi-aikawa/copilot-plugin-notify) | `notify` | Emit OSC 777 escape sequences from Copilot hooks for tool-use approvals and agent-stop alerts | Shell |
| [block/cmux-amp](https://github.com/block/cmux-amp) | `sidebar` | Display Amp agent status in the cmux sidebar using the Amp Plugin API with SF Symbol icons | TypeScript |
| [ipdelete/cmux](https://github.com/ipdelete/cmux) | `layout` `browser` | Provide an Electron workspace with file browsing, Monaco editor, Git integration, and Copilot Chat | TypeScript |

### Multi-Agent / Agent-Agnostic

These projects work across multiple agents or are agent-agnostic.

| Repo | Tags | Description | Lang |
|------|------|-------------|------|
| [manaflow-ai/manaflow](https://github.com/manaflow-ai/manaflow) | `orchestrate` `worktree` `browser` `monitor` | Spawn Claude Code, Codex, Gemini, and others in parallel VS Code workspaces with one-click PR creation | TypeScript · ★997 |
| [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) | `orchestrate` `layout` `progress` `monitor` | Spawn sub-agents across cmux, tmux, zellij, or WezTerm with a live TUI progress widget | TypeScript · ★251 |
| [aannoo/hcom](https://github.com/aannoo/hcom) | `orchestrate` `notify` `monitor` | Connect agents across terminals with messaging, file-collision detection, and multi-agent notifications | Rust · ★185 |
| [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) | `mcp` `orchestrate` `sidebar` `notify` `browser` | Expose 81 MCP tools for agent hierarchy, grid launchers, bulk dispatch, and session recovery | TypeScript |
| [EtanHey/cmuxlayer](https://github.com/EtanHey/cmuxlayer) | `mcp` `orchestrate` `sidebar` `progress` | Provide 22 MCP tools via socket for splits, screen reading, agent orchestration, and sidebar control | TypeScript |
| [jasonraz/cmux-browser-mcp](https://github.com/jasonraz/cmux-browser-mcp) | `mcp` `browser` | Expose 43 browser-only MCP tools with auto-tracked last-opened surface | JavaScript · ★5 |
| [darkspock/cmux-skill](https://github.com/darkspock/cmux-skill) | `browser` `skill` | Teach any agent the full `cmux browser` surface via a self-contained skill file | Markdown · ★7 |
| [owizdom/context-brdige-for-cmux](https://github.com/owizdom/context-brdige-for-cmux) | `monitor` `orchestrate` | Poll panes, persist context to SQLite, and auto-inject handoff briefs for cross-agent memory | Go |
| [rjwittams/flotilla](https://github.com/rjwittams/flotilla) | `worktree` `orchestrate` `monitor` | Correlate branches, PRs, and terminal agents across repos via a TUI dashboard | Rust |
| [meengi07/cmux-agent-observer-skill](https://github.com/meengi07/cmux-agent-observer-skill) | `orchestrate` `layout` `monitor` | Launch visible worker panes for Codex/OpenCode with progress tracking and handoff notes | Shell |

---

## Cross-Platform Ports

### Windows

| Repo | Description | Lang |
|------|-------------|------|
| [mkurman/cmux-windows](https://github.com/mkurman/cmux-windows) | Provide a native Windows terminal with ConPTY, split panes, workspace sidebar, OSC notifications, session persistence, and a named-pipe CLI API | C# · ★81 |
| [TRINITXX/cmux-windows](https://github.com/TRINITXX/cmux-windows) | Fork mkurman's implementation adding Claude Code hooks, Zen mode, Dracula/One Dark themes, and command log replay | C# |
| [aasm3535/wmux](https://github.com/aasm3535/wmux) | Build a WinUI 3 port with xterm.js, vertical sidebar, split panes, OSC notifications, WebView2 browser, and native Mica backdrop | C# |
| [shogotomita/cmux-win](https://github.com/shogotomita/cmux-win) | Build a WPF/ConPTY terminal with workspace splitting, sidebar pills, Claude Code hooks, and a 28-method named-pipe IPC server | C# |

### Linux

| Repo | Description | Lang |
|------|-------------|------|
| [asermax/seemux](https://github.com/asermax/seemux) | Provide a GTK4 terminal with tabbed sidebar, real-time Claude Code status, tab groups, quake dropdown, agent teams, and full session persistence | Rust |
| [nice-bills/lmux](https://github.com/nice-bills/lmux) | Build a pure-C GTK4/VTE terminal with split browser panes, D-Bus notifications, toggleable sidebar, and vim-style navigation | C |
| [anurag-arjun/cove](https://github.com/anurag-arjun/cove) | Fork Ghostty's GTK frontend adding a vertical workspace sidebar, keyboard navigation, planned socket API, and WebKitGTK browser | Zig |
| [bradwilson331/cmux-linux](https://github.com/bradwilson331/cmux-linux) | Port cmux to Linux with Rust, GTK4, GPU-accelerated Ghostty rendering, CDP browser automation, and a 34-subcommand socket CLI | Rust |
| [cai0baa/cmux-for-linux](https://github.com/cai0baa/cmux-for-linux) | Deliver a cross-platform Tauri workspace with React and xterm.js, now branded ptrcode, with workspaces and resizable splits | TypeScript · ★17 |

---

## Alternatives

Projects that solve similar problems without requiring the cmux application itself.

### tmux-Based

| Repo | Description | Lang |
|------|-------------|------|
| [craigsc/cmux](https://github.com/craigsc/cmux) | Wrap git worktree lifecycle into `cmux new <branch>` for isolated agent work with tab completion and merge/teardown | Shell · ★477 |
| [maedana/crmux](https://github.com/maedana/crmux) | Provide a tmux sidebar with live Claude Code status, permission mode, and vim-like navigation with scriptable RPC | Rust · ★20 |
| [wolffiex/cmux](https://github.com/wolffiex/cmux) | Manage tmux windows through a fast popup carousel with 10 preset layouts and AI-powered window summaries | TypeScript |
| [theforager/cmux](https://github.com/theforager/cmux) | Provide an interactive session selector with live status indicators optimized for mobile SSH via Terminus on iOS | Shell |
| [jeremyeder/sisi-cmux](https://github.com/jeremyeder/sisi-cmux) | Auto-discover projects and build tmux workspaces with Claude Code integration and checkpoint save/restore | TypeScript |

### Other Terminals & Workspaces

| Repo | Description | Lang |
|------|-------------|------|
| [adibhanna/tsm](https://github.com/adibhanna/tsm) | Manage persistent terminal sessions as background daemons with a native cmux backend for workspaces, splits, and sidebar sync | Go · ★118 |
| [danneu/danterm](https://github.com/danneu/danterm) | Build a macOS terminal on libghostty with vertical tabs, split panes, tab groups, bell alerts, and JSON layout restore | Swift |
| [Pollux-Studio/maxc](https://github.com/Pollux-Studio/maxc) | Combine terminal multiplexing, embedded browser, task orchestration, and a programmable CLI in a Tauri workspace | Rust |
| [Kaldy14/clui](https://github.com/Kaldy14/clui) | Wrap Claude Code in Electron with project-scoped threads, xterm.js, per-thread worktrees, and LRU hibernation | TypeScript |
| [wrock/wezterm-agent-cards](https://github.com/wrock/wezterm-agent-cards) | Replicate cmux's status-card UX in WezTerm via a curses-based sidebar with Claude Code hooks | Python |
| [davis7dotsh/my-term](https://github.com/davis7dotsh/my-term) | Prototype a native macOS terminal with an Arc-style persistent sidebar using SwiftTerm | Swift |
| [ipdelete/cmux](https://github.com/ipdelete/cmux) | Build an Electron workspace with Copilot CLI/SDK integration, Monaco editor, and PTY terminals | TypeScript |

### Forks

- [llv22/cmux_forward](https://github.com/llv22/cmux_forward) — Add working-directory restore for Bash sessions. One patch over upstream. Swift

---

## Build Your Own Plugin

cmux's plugin surface is intentionally simple: a Unix socket, a CLI, and environment variables. Every workspace gets `CMUX_WORKSPACE_ID`, `CMUX_SURFACE_ID`, and `CMUX_SOCKET_PATH` injected into its environment. Your plugin reads those vars, connects to the socket, and starts sending JSON-RPC messages.

The main integration points:

- **Sidebar status pills** — set key-value pairs that appear next to workspace tabs
- **Progress bars** — update a 0-100% bar in the sidebar
- **Sidebar logs** — write timestamped messages to a scrolling feed
- **Desktop notifications** — fire `cmux notify` or OSC 777 escape sequences
- **Browser automation** — control the embedded WebKit browser via `cmux browser` subcommands
- **Pane management** — split, send, read-screen, and manage surfaces via `cmux` CLI
- **Workspace lifecycle** — create, rename, switch, and close workspaces programmatically

For a detailed walkthrough of the sidebar integration API, see [docs/sidebar-integration-api.md](./docs/sidebar-integration-api.md).

For the full CLI and socket protocol reference:
- [cmux API Reference](https://www.cmux.dev/docs/api)
- [Browser Automation](https://www.cmux.dev/docs/browser-automation)
- [Notifications](https://www.cmux.dev/docs/notifications)
- [AppleScript Automation Guide](./docs/applescript/README.md) — 10-part deep-dive covering CLI wrappers, socket v2, and automation recipes

---

## Reference

### Build & Distribution

| Repo | Description | Lang |
|------|-------------|------|
| [manaflow-ai/manaflow](https://github.com/manaflow-ai/manaflow) | Primary monorepo containing `cmux-proxy` and `cmux-env` Rust crates alongside the orchestration platform | TypeScript · ★997 |
| [lawrencecchen/cmux-proxy](https://github.com/lawrencecchen/cmux-proxy) | Route HTTP/WebSocket/TCP traffic through a header-based reverse proxy with per-workspace network isolation | Rust |
| [lawrencecchen/cmux-env](https://github.com/lawrencecchen/cmux-env) | Coordinate shared environment variables across shells and projects through a lightweight daemon with prompt hooks | Rust |
| [webkaz/cmux-intel-builds](https://github.com/webkaz/cmux-intel-builds) | Automate Intel Mac x86_64 builds by polling upstream releases every 6 hours and publishing unsigned DMGs | — |
| [budah1987/homebrew-tools](https://github.com/budah1987/homebrew-tools) | Install the cmux workspace launcher script via Homebrew with dependency management | Ruby |
| [anhoder/homebrew-repo](https://github.com/anhoder/homebrew-repo) | Distribute a `cmux-nightly` cask via a personal Homebrew tap | Ruby |

### Upstream Dependencies

- [Ghostty](https://ghostty.org/) ([docs](https://ghostty.org/docs) · [config](https://ghostty.org/docs/config) · [source](https://github.com/ghostty-org/ghostty)) — the terminal engine under cmux
- [agent-browser](https://github.com/vercel-labs/agent-browser) — Vercel's browser automation, integrated into cmux · ★26351

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
| Discussions | [github.com/.../discussions](https://github.com/manaflow-ai/cmux/discussions) |
| Issues | [github.com/.../issues](https://github.com/manaflow-ai/cmux/issues) |
| Discord | [invite](https://discord.gg/xsgFEVrWCZ) |
| X | [@manaflowai](https://x.com/manaflowai) |
| YouTube | [channel](https://www.youtube.com/channel/UCAa89_j-TWkrXfk9A3CbASw) |

[Show HN](https://news.ycombinator.com/item?id=47079718) · [r/ClaudeCode intro](https://www.reddit.com/r/ClaudeCode/comments/1r43cdr/introducing_cmux_tmux_for_claude_code/) · [r/ClaudeCode vertical tabs](https://www.reddit.com/r/ClaudeCode/comments/1r9g45u/i_made_a_ghosttybased_terminal_with_vertical_tabs/)

### Articles & Coverage

[Official Demo Video](https://www.youtube.com/watch?v=i-WxO5YUTOs) · [Product Hunt](https://www.producthunt.com/products/cmux) · [YC (Manaflow)](https://www.ycombinator.com/companies/manaflow) · [UBOS](https://ubos.tech/news/introducing-cmux-a-ghostty%E2%80%91based-macos-terminal-with-vertical-tabs-and-ai%E2%80%91agent-notifications/) · [Digg](https://digg.com/technology/QjlMUZ5/cmux-the-terminal-for-multitasking) · [Microlaunch](https://microlaunch.net/p/cmux)

---

## Archived

These repositories have been deleted or are no longer accessible.

- [adhyaay-karnwal/cmux](https://github.com/adhyaay-karnwal/cmux) — Abandoned fork with Docker isolation and multi-CLI support. TypeScript
- [ctaho19/cmux-cursor-work-style](https://github.com/ctaho19/cmux-cursor-work-style) — Repository deleted. Previously contained a Cursor aesthetic theme with charcoal/blue colors and Berkeley Mono

---

## Contributing

Before opening a PR, verify your entry:

1. **Public repo** with a README
2. **Uses a cmux API** — `CMUX_SOCKET_PATH`, `cmux` CLI, socket protocol, or cmux env vars
3. **Themes/configs** must include at least one cmux-specific feature
4. **Description** — start with a verb, 30-50 words, neutral tone, no superlatives
5. **Format** — `[owner/repo](url) | \`tag\` | description | Lang · ★N`
6. **Placement** — add the repo to every feature dimension section it belongs in, plus the correct agent section

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full style guide.

## License

MIT — see [LICENSE](./LICENSE).

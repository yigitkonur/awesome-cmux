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
| **Claude Code** | | | |
| [yigitkonur/cmux-claude-pro](https://github.com/yigitkonur/cmux-claude-pro) | Claude Code | Cover the widest lifecycle surface of any Claude Code plugin: wire sixteen hooks for real-time status pills, adaptive progress bars, formatted log entries, git branch metadata, and subagent tracking simultaneously | TypeScript |
| [maedana/crmux](https://github.com/maedana/crmux) | Claude Code | Unlike cmux-native plugins, renders a tmux-based sidebar outside cmux itself, surfacing permission mode, repo, branch, and worktree alongside live status for every concurrent Claude Code session | Rust · ★20 |
| [azu/cmux-hub](https://github.com/azu/cmux-hub) | Claude Code | Focuses on post-session review rather than live pills: expose a browser-based diff viewer with inline comments, commit history, and GitHub PR/CI status that other Claude Code plugins omit | TypeScript · ★15 |
| [taichiiwamoto-s/cmux-context](https://github.com/taichiiwamoto-s/cmux-context) | Claude Code | Specializes in context-window awareness unlike general status plugins — visualize fill percentage, line counts, and rate limits as color-coded progress bars across all open workspaces simultaneously | Shell |
| [tslateman/cmux-claude-code](https://github.com/tslateman/cmux-claude-code) | Claude Code | Adds emoji-labeled tool names to status pills and uses a logarithmic progress curve that accounts for diminishing returns, unlike linear bars in other Shell-based Claude Code plugins | Shell |
| [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) | Claude Code | Uniquely bundles Claude-specific restraint rules alongside tab renaming and live progress bars, nudging the agent toward safer behavior rather than just reporting it | Shell |
| [eduwass/cru](https://github.com/eduwass/cru) | Claude Code | Targets multi-agent teams rather than single sessions: arrange workers in a labeled grid with a 447-line cmux module, SF Symbol lifecycle phases, and a progress-watcher — unlike single-session Claude Code plugins | TypeScript |
| [bocktae80/cmux-pilot](https://github.com/bocktae80/cmux-pilot) | Claude Code | Focuses on session persistence rather than live decoration: manage workspace-to-session mappings and bulk-resume all sessions after a system restart, a recovery workflow absent from other Claude Code plugins | Shell |
| [KyleJamesWalker/cc-cmux-plugin](https://github.com/KyleJamesWalker/cc-cmux-plugin) | Claude Code | Prioritizes onboarding over decoration: inject the full cmux command reference into every new session and auto-grant cmux CLI permissions, so the agent can use cmux tools without manual setup | — |
| [jaequery/cmux-diff](https://github.com/jaequery/cmux-diff) | Claude Code | Unlike status-pill plugins, adds a Cursor-style changes panel inside cmux's browser split with syntax-highlighted diffs and AI-generated commit messages as a persistent companion view | TypeScript |
| [wrock/wezterm-agent-cards](https://github.com/wrock/wezterm-agent-cards) | Claude Code | Targets WezTerm users exclusively: render Claude Code sessions as stacked curses-based status cards, unlike cmux-socket plugins that require the cmux sidebar infrastructure | Python |
| [Mirksen/cmux-toolkit](https://github.com/Mirksen/cmux-toolkit) | Claude Code | Skips status pills in favour of IDE ergonomics: auto-open edited files in a Vim subpane and toggle a broot file-browser sidebar, turning cmux into a lightweight editor environment | Shell |
| **Pi** | | | |
| [HazAT/pi-config](https://github.com/HazAT/pi-config) | Pi | Covers the broadest Pi surface of any plugin: push model, tokens, active tool, and cost to the sidebar via a built-in multi-agent architecture with dedicated planning, scouting, and review subagents | TypeScript · ★228 |
| [w-winter/dot314](https://github.com/w-winter/dot314) | Pi | Unlike single-script Pi plugins, ships as a curated extension collection that adds cost and token stats alongside sidebar state and workspace renaming — focuses on financial visibility other Pi plugins lack | TypeScript · ★77 |
| [espennilsen/pi](https://github.com/espennilsen/pi) | Pi | Extends Pi with 7 LLM-callable tools for workspace and browser control stored in a version-controlled home directory, adding capabilities beyond sidebar status that no other Pi plugin matches | TypeScript · ★68 |
| [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) | Pi | Maintains exactly four live pills (model, state, thinking, tokens) via a persistent socket client, and unlike joelhooks/pi-cmux's heartbeat approach, generates context-aware notification summaries using LLM calls | TypeScript · ★14 |
| [joelhooks/pi-cmux](https://github.com/joelhooks/pi-cmux) | Pi | Adds AI-generated session names via Claude Haiku on top of a 3-second heartbeat, and unlike sasha-computer/pi-cmux, includes explicit worker mode for orchestrator-spawned subagents | TypeScript · ★9 |
| [Attamusc/pi-cmux](https://github.com/Attamusc/pi-cmux) | Pi | Differentiates from other Pi plugins with render throttling to prevent sidebar flicker, dynamic progress estimation, and needs-attention alerts that auto-clear after ten seconds | TypeScript |
| [sanurb/pi-cmux](https://github.com/sanurb/pi-cmux) | Pi | Focuses specifically on safe command execution: adds an explicit allowlist for workspace tools alongside focus-aware debounced macOS notifications, a security layer absent from other Pi plugins | TypeScript |
| [simonjohansson/pi-cmux](https://github.com/simonjohansson/pi-cmux) | Pi | Prioritizes simplicity over breadth: expose a single configurable `cmux_cli` pass-through tool that forwards any argv to cmux, unlike multi-pill Pi plugins that hard-code their event mappings | TypeScript |
| **OpenCode** | | | |
| [kdcokenny/ocx](https://github.com/kdcokenny/ocx) | OpenCode | Adds portable configuration profile management on top of sidebar status — the only OpenCode plugin that lets you switch full environment profiles with flash triggers, making it production-proven at 520 stars | TypeScript · ★520 |
| [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) | OpenCode | Unlike kdcokenny/ocx's profile focus, drives progress from todo completion counts and scopes unread log marks per workspace, giving per-project visibility across parallel OpenCode sessions | TypeScript · ★23 |
| [Attamusc/opencode-cmux](https://github.com/Attamusc/opencode-cmux) | OpenCode | Prioritizes performance over features: delivers ~1-2ms socket latency with render throttling and log rate-limiting, unlike Shell-based OpenCode plugins that lack backpressure controls | TypeScript |
| [tully-8888/opencode-cmux-notify-plugin](https://github.com/tully-8888/opencode-cmux-notify-plugin) | OpenCode | Focuses on subagent lifecycle tracking alongside desktop notifications for questions, permissions, and errors — unlike Attamusc/opencode-cmux, does not throttle and targets completeness over performance | Shell |
| [Joehoel/opencode-cmux](https://github.com/Joehoel/opencode-cmux) | OpenCode | Uniquely integrates external project management services: polls Azure DevOps and Jira via Zsh to inject ticket and build status as additional sidebar pills alongside standard OpenCode status | Shell |
| **Copilot** | | | |
| [Attamusc/copilot-cmux](https://github.com/Attamusc/copilot-cmux) | Copilot | Bridge Copilot CLI events to the cmux sidebar via socket JSON-RPC, covering status pills, progress bars, log entries, and desktop notifications — the only dedicated Copilot sidebar plugin in the list | TypeScript |
| **Amp** | | | |
| [block/cmux-amp](https://github.com/block/cmux-amp) | Amp | Wire the official Amp Plugin API to the cmux sidebar with SF Symbol icons for agent state — the only first-party Amp plugin in the list, built and maintained by Block | TypeScript |
| **Multi-Agent / Agnostic** | | | |
| [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) | Multi | Expose 81 MCP tools spanning agent spawning, sidebar metadata, notifications, browser automation, and session recovery — the largest MCP surface area of any plugin here, unlike EtanHey/cmuxlayer's focused 22-tool set | TypeScript |
| [EtanHey/cmuxlayer](https://github.com/EtanHey/cmuxlayer) | Multi | Expose 22 tightly scoped MCP tools for sidebar updates, progress, split creation, and screen reading — smaller and more auditable than cmux-agent-mcp's 81-tool suite, while still covering multi-agent orchestration | TypeScript |
| [gonzaloserrano/streamdeck-cmux](https://github.com/gonzaloserrano/streamdeck-cmux) | — | Extends status visibility beyond the screen entirely: mirror workspace state, progress bars, and notification badges onto Elgato Stream Deck hardware buttons — the only physical-hardware integration in the list | TypeScript · ★7 |

### 2. Progress Bars & Estimation

Long-running agent tasks need visible progress. cmux's sidebar supports progress bars that fill from 0-100%. The best plugins estimate completion dynamically — some use logarithmic curves, others count completed todo items. Without progress bars, you are left guessing whether an agent is stuck or just thinking hard.

> **Recommended**: [yigitkonur/cmux-claude-pro](https://github.com/yigitkonur/cmux-claude-pro) for adaptive progress estimation, [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) for cross-multiplexer live TUI progress, [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) for todo-driven progress tracking.

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| **Claude Code** | | | |
| [hummer98/using-cmux](https://github.com/hummer98/using-cmux) | Claude Code | Teach Claude Code to own and drive sidebar progress bars as documented skill within a broader sub-agent lifecycle curriculum, making progress control an explicit agent capability rather than an implicit side-effect | Shell · ★24 |
| [hummer98/cmux-team](https://github.com/hummer98/cmux-team) | Claude Code | Display independent real-time progress bars for conductor and each worker sub-agent in a task-queue daemon, letting you distinguish which tier of the hierarchy is blocked | TypeScript · ★9 |
| [yigitkonur/cmux-claude-pro](https://github.com/yigitkonur/cmux-claude-pro) | Claude Code | Drive adaptive progress bars from sixteen lifecycle hooks, weighting tool execution patterns and session state to produce a continuously refined completion estimate rather than a fixed linear fill | TypeScript |
| [tslateman/cmux-claude-code](https://github.com/tslateman/cmux-claude-code) | Claude Code | Render a logarithmic progress bar that deliberately slows near 100% to reflect the diminishing-returns reality of long-running Claude Code sessions | Shell |
| [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) | Claude Code | Bundle live progress bars with auto tab renaming and completion notifications, covering the three most-wanted sidebar features in a single Shell hook file | Shell |
| [taichiiwamoto-s/cmux-context](https://github.com/taichiiwamoto-s/cmux-context) | Claude Code | Repurpose the progress bar slot to show context window fill percentage with color-coded urgency bands, giving a resource-pressure signal instead of a task-completion estimate | Shell |
| **Pi** | | | |
| [Attamusc/pi-cmux](https://github.com/Attamusc/pi-cmux) | Pi | Estimate progress dynamically from Pi lifecycle events while enforcing render throttling so rapid tool bursts do not cause sidebar flicker | TypeScript |
| **OpenCode** | | | |
| [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) | OpenCode | Track todo-item resolution as the progress signal — the bar advances each time a checklist item resolves, giving concrete task-based completion rather than an inferred estimate | TypeScript · ★23 |
| [Attamusc/opencode-cmux](https://github.com/Attamusc/opencode-cmux) | OpenCode | Combine tool-execution and file-edit counts into a blended progress estimate, capping update frequency with rate limiting to prevent sidebar jitter under fast OpenCode sessions | TypeScript |
| [Joehoel/opencode-cmux](https://github.com/Joehoel/opencode-cmux) | OpenCode | Update the sidebar progress bar from OpenCode events alongside Azure DevOps and Jira status pills, making it the only plugin that co-renders external ticket state next to local task progress | Shell |
| **Copilot** | | | |
| [Attamusc/copilot-cmux](https://github.com/Attamusc/copilot-cmux) | Copilot | Map discrete Copilot CLI tool-execution stages to fixed progress increments, producing a step-function bar that reflects which phase of the agent pipeline is active | TypeScript |
| **Multi / Other** | | | |
| [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) | Multi | Render elapsed time and live per-agent progress in a TUI widget while sub-agents execute in dedicated panes across cmux, tmux, zellij, or WezTerm — the widest multiplexer coverage of any progress plugin | TypeScript · ★251 |
| [EtanHey/cmuxlayer](https://github.com/EtanHey/cmuxlayer) | Multi | Expose progress indicator MCP tools as part of a 22-tool suite, letting any MCP-capable agent write progress state without being wired to a specific agent's lifecycle hooks | TypeScript |
| [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) | Multi | Embed progress tracking inside an 81-tool MCP server designed for multi-agent workspace orchestration, making progress updates composable with spawning, routing, and session-recovery tools | TypeScript |
| [gonzaloserrano/streamdeck-cmux](https://github.com/gonzaloserrano/streamdeck-cmux) | — | Render progress bars physically on Elgato Stream Deck buttons by polling the cmux socket — the only plugin to project sidebar state onto dedicated hardware rather than a terminal column | TypeScript · ★7 |

---

### 3. Sidebar Logs & Activity Feed

The sidebar can show scrolling log entries — timestamped messages about what the agent is doing. Logs are essential for debugging: you can see which tools were called, which files were edited, and where errors occurred without switching to the agent's pane. The entries here differ meaningfully in what they capture, how they handle high-frequency events, and whether they correlate logs to external systems.

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| **Claude Code** | | | |
| [yigitkonur/cmux-claude-pro](https://github.com/yigitkonur/cmux-claude-pro) | Claude Code | Emit formatted sidebar log entries for all sixteen lifecycle hooks — the only Claude Code plugin that attaches git branch and commit metadata to each entry, making logs navigable as a lightweight session audit trail | TypeScript |
| [claude-studio/claude-studio](https://github.com/claude-studio/claude-studio) | Claude Code | Parse JSONL transcripts from `~/.claude/projects` offline to render cost, token, and session statistics on a standalone dashboard rather than writing live log entries — suited for post-session analysis, not real-time monitoring | TypeScript |
| **Pi** | | | |
| [simonjohansson/pi-cmux](https://github.com/simonjohansson/pi-cmux) | Pi | Log Pi tool executions to the sidebar feed while also exposing a single passthrough `cmux_cli` tool that lets Pi issue any cmux command directly, making the agent itself a first-class log author | TypeScript |
| **OpenCode** | | | |
| [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) | OpenCode | Maintain a workspace-scoped event timeline with unread marks — entries persist across pane switches so you can return to a workspace and immediately see what happened while you were away | TypeScript · ★23 |
| [Attamusc/opencode-cmux](https://github.com/Attamusc/opencode-cmux) | OpenCode | Apply rate limiting to log writes so high-frequency tool bursts produce a readable digest rather than a flooding stream, prioritizing signal over completeness during intensive OpenCode sessions | TypeScript |
| [Joehoel/opencode-cmux](https://github.com/Joehoel/opencode-cmux) | OpenCode | Interleave OpenCode agent event logs with Azure DevOps pipeline and Jira ticket updates in a single sidebar feed, correlating local agent work with external project state | Shell |
| **Copilot** | | | |
| [Attamusc/copilot-cmux](https://github.com/Attamusc/copilot-cmux) | Copilot | Log the full Copilot prompt-submission → tool-execution → completion arc as discrete sidebar entries, providing a per-session breadcrumb trail of every agent action via socket JSON-RPC | TypeScript |
| **Multi / Other** | | | |
| [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) | Multi | Produce structured log output through an 81-tool MCP server so any orchestrating agent can write diagnostic entries to the sidebar without being bound to a single agent's event lifecycle | TypeScript |

### 4. Desktop Notifications

When an agent finishes a task, hits an error, or needs permission, you want to know immediately — even if cmux is behind another window. Plugins use `cmux notify` or OSC 777 escape sequences to fire native macOS notifications. The best ones are focus-aware: they stay quiet when you are already looking at the workspace.

> **Recommended**: [kdcokenny/opencode-notify](https://github.com/kdcokenny/opencode-notify) for OpenCode (standalone, 127 stars), [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) for Pi (context-aware summaries).

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| **Claude Code** | | | |
| [yigitkonur/cmux-claude-pro](https://github.com/yigitkonur/cmux-claude-pro) | Claude Code | Fire targeted notifications on completion, errors, and attention events; uniquely pairs notifications with a 16-hook sidebar that tracks live agent state — the only Claude Code notifier with deep sidebar integration | TypeScript |
| [hummer98/using-cmux](https://github.com/hummer98/using-cmux) | Claude Code | Teach notification patterns as reusable sub-agent workflow skills rather than hooks; uniquely treats notification behavior as a learnable Claude Code skill library, not an event handler | Shell · ★24 |
| [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) | Claude Code | Fire completion notifications alongside tab renaming and live progress bars; uniquely bundles three UX concerns (notify + rename + progress) in a single shell plugin rather than notifications alone | Shell |
| [tslateman/cmux-claude-code](https://github.com/tslateman/cmux-claude-code) | Claude Code | Send notifications on completion or attention events across five lifecycle hooks; leaner than hopchouinard's bundle — pure notification focus with no sidebar or tab side-effects | Shell |
| [Th3Sp3ct3R/cmux-claude-agents](https://github.com/Th3Sp3ct3R/cmux-claude-agents) | Claude Code | Send completion notifications specifically when redirected sub-agent panes finish; uniquely scoped to redirected-pane topology rather than the primary session | Shell |
| [KyleJamesWalker/cc-cmux-plugin](https://github.com/KyleJamesWalker/cc-cmux-plugin) | Claude Code | Route notifications through `cmux notify` with auto-granted CLI permissions pre-configured; distinguishes itself by solving the permission-prompt problem so notifications fire silently on first run | — |
| [rappdw/zen-term](https://github.com/rappdw/zen-term) | Claude Code | Forward OSC 777 rings from a remote DGX Spark to the local MacBook running cmux via Mosh; uniquely solves the remote-GPU-to-local-desktop notification gap — no other entry covers cross-host forwarding | Shell |
| [eduwass/cru](https://github.com/eduwass/cru) | Claude Code | Fire lifecycle-phase notifications rendered with SF Symbols inside an agent team grid; uniquely integrates notification glyphs into a multi-agent grid view rather than standalone alerts | TypeScript |
| **Pi** | | | |
| [HazAT/pi-config](https://github.com/HazAT/pi-config) | Pi | Deliver notifications as part of a full multi-agent architecture with cost tracking and subagent coordination; the most feature-complete Pi config — notifications are one layer of a production-grade orchestration stack | TypeScript · ★228 |
| [w-winter/dot314](https://github.com/w-winter/dot314) | Pi | Send attention notifications when Pi needs input, alongside sidebar state sync and token stats; uniquely surfaces token spend next to every alert so cost is visible at the moment attention is requested | TypeScript · ★77 |
| [bjacobso/pimux](https://github.com/bjacobso/pimux) | Pi | Notify as part of a task state machine managing parallel Pi agents across worktrees; uniquely ties notification events to worktree lifecycle transitions, not just session-level hooks | TypeScript |
| [joelhooks/pi-cmux](https://github.com/joelhooks/pi-cmux) | Pi | Send native macOS notifications combined with attention-cycle tab indicators and auto-generated session names; uniquely auto-names sessions from task context so notifications carry a human-readable label | TypeScript · ★9 |
| [Attamusc/pi-cmux](https://github.com/Attamusc/pi-cmux) | Pi | Show needs-attention banners that auto-clear after ten seconds with render throttling; unlike joelhooks' persistent indicators, alerts self-dismiss to avoid cluttering the notification center | TypeScript |
| [sanurb/pi-cmux](https://github.com/sanurb/pi-cmux) | Pi | Deliver focus-aware debounced macOS notifications alongside live sidebar status pills; uniquely suppresses rapid-fire alerts via debounce — the only Pi notifier with explicit debounce logic | TypeScript |
| [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) | Pi | Provide context-aware notifications that summarize agent actions using LLM-callable tools for targeted alerts; uniquely lets the agent itself decide when and what to notify — no static hook triggers | TypeScript · ★14 |
| **OpenCode** | | | |
| [kdcokenny/opencode-workspace](https://github.com/kdcokenny/opencode-workspace) | OpenCode | Bundle OS notifications inside a 16-component harness with planning, delegation, and worktree plugins; the most expansive OpenCode setup — notifications are one piece of a full orchestration suite | TypeScript · ★292 |
| [kdcokenny/opencode-notify](https://github.com/kdcokenny/opencode-notify) | OpenCode | Deliver native OS notifications on completion, errors, and input-needed events with click-to-foreground, quiet hours, and custom sounds; the only standalone OpenCode notifier with quiet-hours scheduling and sound customization | TypeScript · ★127 |
| [0xCaso/opencode-cmux](https://github.com/0xCaso/opencode-cmux) | OpenCode | Notify on permission requests and subagent activity scoped per workspace with unread marks; uniquely tracks unread notification state per workspace — alerts persist until explicitly acknowledged | TypeScript · ★23 |
| [mspiegel31/opencode-cmux](https://github.com/mspiegel31/opencode-cmux) | OpenCode | Push desktop notifications on idle or error alongside subagent viewer panes and browser tools; distinguishes itself by pairing notification events with visible subagent viewer panes in the same plugin | TypeScript |
| [Joehoel/opencode-cmux](https://github.com/Joehoel/opencode-cmux) | OpenCode | Send desktop notifications on permission requests, errors, and completions; the lightest OpenCode notifier — shell-only, no extra components, useful as a copy-paste starting point | Shell |
| [tully-8888/opencode-cmux-notify-plugin](https://github.com/tully-8888/opencode-cmux-notify-plugin) | OpenCode | Notify on questions, permissions, retries, and finish events with automatic stale-state clearing; uniquely handles stale-state cleanup on each trigger, preventing ghost notifications from aborted runs | Shell |
| **Copilot** | | | |
| [tadashi-aikawa/copilot-plugin-notify](https://github.com/tadashi-aikawa/copilot-plugin-notify) | Copilot | Emit OSC 777 escape sequences for tool-use approvals and agent-stop alerts with configurable allow/deny rules; uniquely exposes an allow/deny rule set so noisy approval events can be filtered before the notification fires | Shell |
| [Attamusc/copilot-cmux](https://github.com/Attamusc/copilot-cmux) | Copilot | Translate Copilot CLI socket JSON-RPC events into desktop notifications; lower-level than tadashi-aikawa's approach — operates on raw RPC messages rather than named hook events | TypeScript |
| **Multi / Other** | | | |
| [aannoo/hcom](https://github.com/aannoo/hcom) | Multi | Deliver cross-agent notifications and file-edit collision detection across Claude Code, Gemini CLI, Codex, and OpenCode in a single Rust daemon; the only entry covering four agents simultaneously and the only one that catches edit collisions | Rust · ★185 |
| [itsmaleen/cmux-companion](https://github.com/itsmaleen/cmux-companion) | — | Mirror cmux notifications to an iPhone via a Go bridge server over LAN WebSocket; uniquely extends notifications off the Mac entirely — no other entry targets a secondary device | Go / Swift |

### 5. Multi-Agent Orchestration

Running multiple agents in parallel is cmux's superpower. An orchestrator agent splits panes, launches workers, sends them tasks, and monitors their output via `read-screen`. The best frameworks handle the full lifecycle: spawn, dispatch, poll for completion, collect results, and tear down. This section includes both ready-to-use frameworks and skill files that teach your agent how to orchestrate.

> **Recommended**: [manaflow-ai/manaflow](https://github.com/manaflow-ai/manaflow) (997 stars, broadest agent coverage across VS Code workspaces), [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) (251 stars, works across cmux/tmux/zellij), [dagster-io/erk](https://github.com/dagster-io/erk) for plan-oriented workflows with PR automation.

**Frameworks**

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| **Multi-agent** | | | |
| [manaflow-ai/manaflow](https://github.com/manaflow-ai/manaflow) | Multi | Spawn Claude Code, Codex, Gemini, and other agents in parallel VS Code workspaces with git diff view and one-click PR creation — uniquely built around VS Code rather than terminal multiplexers | TypeScript · ★997 |
| [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) | Multi | Spawn async sub-agents in dedicated panes across cmux, tmux, zellij, or WezTerm with a live TUI progress widget — the only framework with first-class multiplexer portability built in | TypeScript · ★251 |
| [aannoo/hcom](https://github.com/aannoo/hcom) | Multi | Connect agents across terminals with cross-agent messaging, file-collision detection, and desktop notifications for Claude Code, Gemini, Codex, and OpenCode — focuses on safe concurrent file access rather than pane topology | Rust · ★185 |
| [rjwittams/flotilla](https://github.com/rjwittams/flotilla) | Multi | Correlate branches, PRs, issues, and terminal agents across repos into unified work items via a TUI dashboard — addresses multi-repo tracking rather than single-repo task dispatch | Rust |
| **Claude Code** | | | |
| [dagster-io/erk](https://github.com/dagster-io/erk) | Claude Code | Create implementation plans from AI, execute each in an isolated git worktree, and ship via automated PR submission — uniquely enforces full plan-execute-ship cycle with worktree isolation per task | Python · ★78 |
| [hummer98/cmux-team](https://github.com/hummer98/cmux-team) | Claude Code | Run a task-queue daemon that spawns conductor and worker sub-agents in visible cmux split panes with a TUI dashboard — differs from erk by operating entirely in-terminal with no git-worktree isolation | TypeScript · ★9 |
| [eduwass/cru](https://github.com/eduwass/cru) | Claude Code | Arrange agent team workers into a labeled grid across tmux, Ghostty, or cmux — focused purely on layout templating rather than task dispatch or lifecycle management | TypeScript |
| **Pi** | | | |
| [burggraf/pi-teams](https://github.com/burggraf/pi-teams) | Pi | Turn one Pi agent into a coordinated team with specialist teammates, shared task board, direct messaging, and plan-approval gates — Pi-native alternative to general multi-agent frameworks | TypeScript · ★55 |
| [bjacobso/pimux](https://github.com/bjacobso/pimux) | Pi | Manage parallel Pi agents via an Effect service with per-task workspaces, sidebar state machine, and diff review workflow — adds typed Effect-based orchestration on top of Pi's native agent model | TypeScript |
| **OpenCode** | | | |
| [kdcokenny/opencode-workspace](https://github.com/kdcokenny/opencode-workspace) | OpenCode | Bundle 16 components for multi-agent orchestration with plan and build orchestrators, specialist agents, and MCP servers — the most comprehensive starter kit purpose-built for OpenCode | TypeScript · ★292 |

**MCP Servers**

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| **Multi-agent** | | | |
| [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) | Multi | Expose 81 tools covering full agent hierarchy, grid launchers, bulk dispatch, and session recovery — broadest tool surface for agents that need granular programmatic control over cmux | TypeScript |
| [EtanHey/cmuxlayer](https://github.com/EtanHey/cmuxlayer) | Multi | Provide 22 focused tools via sub-millisecond socket transport with CLI fallback and an agent lifecycle engine — trades breadth for latency, optimized for high-frequency agent polling loops | TypeScript |

**Orchestration Skills** (teach your agent how to orchestrate)

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| **Claude Code** | | | |
| [hummer98/using-cmux](https://github.com/hummer98/using-cmux) | Claude Code | Teach visible sub-agent lifecycle patterns — split, send, `read-screen`, status, notifications, and recovery — the most complete reference for Claude Code agents new to cmux orchestration | Shell · ★24 |
| [ygrec-app/supreme-leader-skill](https://github.com/ygrec-app/supreme-leader-skill) | Claude Code | Plan subtasks, spawn a 2–8 worker grid, monitor via `read-screen` polling, review deliverables, and dispatch fix iterations — covers the full orchestrator loop in a single skill | Markdown |
| [umitaltintas/cmux-agent-toolkit](https://github.com/umitaltintas/cmux-agent-toolkit) | Claude Code | Teach fan-out execution with spawn, then synchronize via `wait-for`/`wait-for --signal` signals and explicit pane topology management — unique focus on barrier-style synchronization primitives | Markdown |
| [baixianger/claude-orchestration-in-cmux](https://github.com/baixianger/claude-orchestration-in-cmux) | Claude Code | Coordinate parallel work via pane delegation with `cmux send`/`read-screen` through worktrees — emphasizes git-worktree isolation as the coordination boundary rather than shared workspace | Markdown |
| [Th3Sp3ct3R/cmux-claude-agents](https://github.com/Th3Sp3ct3R/cmux-claude-agents) | Claude Code | Intercept Agent tool calls via a `PreToolUse` hook and redirect them to visible cmux split panes — hook-based approach means zero changes to the agent's own prompts or skills | Shell |
| [ygrec-app/offload-task-skill](https://github.com/ygrec-app/offload-task-skill) | Claude Code | Offload a single task to a dedicated split pane with an autonomous worker, preserving main session context and token budget — minimal single-task delegation rather than full grid orchestration | Markdown |
| [bocktae80/cmux-pilot](https://github.com/bocktae80/cmux-pilot) | Claude Code | Manage workspace-to-session mappings with `/cmux-ws` commands and bulk session resume after restarts — addresses persistent session bookkeeping that other skills leave to the user | Shell |
| [alaasdk/cmux-ctl](https://github.com/alaasdk/cmux-ctl) | Claude Code | Display a real-time TUI dashboard of all active workspaces with keyboard-driven agent launching and direct input — control-plane view complementing skills that focus on task dispatch | Python |
| [jeremyeder/sisi-cmux](https://github.com/jeremyeder/sisi-cmux) | Claude Code | Auto-discover projects and build tmux workspaces with one-key Claude Code integration and checkpoint save/restore — project-bootstrap companion rather than a runtime orchestration skill | TypeScript |
| [halindrome/cmux-tmux-mapping-for-cc](https://github.com/halindrome/cmux-tmux-mapping-for-cc) | Claude Code | Detect tmux vs cmux at runtime and transparently route all panel operations through the correct backend — enables skills written for one multiplexer to work unchanged on the other | Shell |
| **Pi** | | | |
| [HazAT/pi-config](https://github.com/HazAT/pi-config) | Pi | Configure a multi-agent architecture with cmux-visible subagents for planning, scouting, coding, and reviewing — the canonical reference for role-specialized Pi agent teams | TypeScript · ★228 |
| [w-winter/dot314](https://github.com/w-winter/dot314) | Pi | Provide branch-out workflows, a command center, and multi-repo project navigation for Pi agents — extends Pi's scope to cross-repo orchestration that single-repo skills cannot address | TypeScript · ★77 |
| [espennilsen/pi](https://github.com/espennilsen/pi) | Pi | Maintain 22 extensions including subagent delegation and project context switching — a general-purpose Pi config that bundles orchestration alongside unrelated productivity extensions | TypeScript · ★68 |
| [joelhooks/pi-cmux](https://github.com/joelhooks/pi-cmux) | Pi | Enforce a worker mode in orchestrator-spawned agents to prevent fork bombs — solves a single critical safety problem that every other Pi orchestration skill ignores | TypeScript · ★9 |
| [sanurb/pi-cmux-workflows](https://github.com/sanurb/pi-cmux-workflows) | Pi | Add slash commands for splitting panes with new agent sessions and handing off task context between splits — lightweight entry point for Pi users who want manual-trigger orchestration | TypeScript |
| **Multi-agent** | | | |
| [owizdom/context-brdige-for-cmux](https://github.com/owizdom/context-brdige-for-cmux) | Multi | Run a background daemon that extracts agent context, persists it to SQLite, and auto-injects handoff briefs into new sessions — the only skill addressing cold-start context loss across session boundaries | Go |
| [meengi07/cmux-agent-observer-skill](https://github.com/meengi07/cmux-agent-observer-skill) | Multi | Launch visible worker panes for Codex and OpenCode with optional tmux wrapping and a browser helper — extends cmux orchestration to non-Claude agents that lack native cmux support | Shell |

### 6. Browser Automation

cmux embeds a WebKit browser pane that agents can control via CLI. Plugins use `cmux browser` for navigation, DOM interaction, screenshots, form filling, and JavaScript evaluation. The best ones expose the full 40+ subcommand surface. This is how agents can visually verify their work, run E2E tests, or display rich content alongside the terminal.

> **Recommended**: [azu/cmux-hub](https://github.com/azu/cmux-hub) for the highest-starred diff viewer with CI status (★15), [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) for the best all-round Pi browser toolkit (★14), [jasonraz/cmux-browser-mcp](https://github.com/jasonraz/cmux-browser-mcp) for MCP-based browser control (43 tools).

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| **Claude Code** | | | |
| [azu/cmux-hub](https://github.com/azu/cmux-hub) | Claude Code | Open a syntax-highlighted diff viewer in a browser split with inline review comments and live GitHub CI status alongside the terminal — the only browser plugin combining code review and CI feedback in one pane | TypeScript · ★15 |
| [jasonraz/cmux-browser-mcp](https://github.com/jasonraz/cmux-browser-mcp) | Claude Code | Expose 43 discrete MCP tools covering navigation, DOM clicking, form filling, screenshots, JS eval, and network inspection — the widest MCP tool surface of any browser plugin | JavaScript · ★5 |
| [jaequery/cmux-diff](https://github.com/jaequery/cmux-diff) | Claude Code | Show Shiki-powered syntax-highlighted diffs in a browser split with multi-file selection and AI-generated commit message suggestions — distinct from azu/cmux-hub by pairing diff viewing with commit authoring | TypeScript |
| [hashangit/cmux-skill](https://github.com/hashangit/cmux-skill) | Claude Code | Control browser elements by stable ref via `snapshot --interactive`, applying a notification decision matrix to choose alert vs. pane — the only skill built around element-ref stability rather than XPath/CSS selectors | Shell |
| [RyoHirota68/cmux-pencil-preview](https://github.com/RyoHirota68/cmux-pencil-preview) | Claude Code | Auto-export Pencil design files to PDF and hot-reload them in the browser pane on each save — purpose-built for design iteration loops, not general web content | Shell |
| [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) | Claude Code | Open browser splits for UI verification and pair them with tab renaming, animated progress bars, and audio completion notifications — uniquely combines visual verification with rich status feedback | Shell |
| [mangledmonkey/cmux-skills](https://github.com/mangledmonkey/cmux-skills) | Claude Code | Teach Claude Code browser automation across four auto-syncing skill files covering form filling, screenshots, and debug window capture — structured as a multi-file skill suite rather than a single monolithic document | Shell |
| [Stealinglight/cmux-claude-code-skill](https://github.com/Stealinglight/cmux-claude-code-skill) | Claude Code | Document browser, CLI, and shortcuts references with concrete Python socket API examples for WebKit automation — the only skill that bridges the cmux Python socket API into browser control | Shell |
| [goddaehee/cmux-claude-skill](https://github.com/goddaehee/cmux-claude-skill) | Claude Code | Map all 40+ browser subcommands alongside workspace navigation and a tmux-to-cmux migration table, written in Korean — uniquely serves developers migrating existing tmux muscle memory | Markdown |
| [mikecfisher/cmux-skill](https://github.com/mikecfisher/cmux-skill) | Claude Code | Cover browser automation as part of a broad CLI taxonomy that uniquely documents `capture-pane` internals and `CMUX_SOCKET_PASSWORD` authentication — more reference than tutorial | Markdown |
| [monzou/mo-cmux](https://github.com/monzou/mo-cmux) | Claude Code | Preview Markdown files in a browser split with live-reload on save and fuzzy filename matching — focused narrowly on Markdown rendering rather than general browser control | Shell |
| [hoonkim/cmux-skills-plugin](https://github.com/hoonkim/cmux-skills-plugin) | Claude Code | Enable browser automation and pane control via `cmux tree`, `read-screen`, and `send`, with all documentation in Korean — distinct by emphasizing pane-tree introspection commands not covered in English-language skills | Markdown |
| **Pi** | | | |
| [sasha-computer/pi-cmux](https://github.com/sasha-computer/pi-cmux) | Pi | Give Pi LLM-callable browser automation tools alongside sidebar notification pills and context-aware inline notifications — the most starred Pi browser plugin and the only one with a native sidebar pill UI | TypeScript · ★14 |
| [sanurb/pi-cmux-browser](https://github.com/sanurb/pi-cmux-browser) | Pi | Provide Pi with typed browser automation actions (click, fill, screenshot, snapshot) plus a dedicated spawnable web-dev subagent — unique in offering a purpose-built subagent for frontend development tasks | TypeScript |
| [storelayer/pi-cmux-browser](https://github.com/storelayer/pi-cmux-browser) | Pi | Equip Pi with dual browser modes: cmux in-app WebKit for visual debugging and Playwright for headless CI workflows — the only Pi plugin that lets the agent switch between visual and headless modes per task | JavaScript |
| [mastertyko/pi-cmux-preview](https://github.com/mastertyko/pi-cmux-preview) | Pi | Render assistant Markdown responses as styled HTML in a cmux browser pane with inline terminal screenshots and file previews — turns the browser pane into a rich conversation renderer rather than a web browser | TypeScript |
| [sanurb/pi-cmux-workflows](https://github.com/sanurb/pi-cmux-workflows) | Pi | Display ringi-powered code reviews in cmux browser panes alongside split-pane and agent handoff slash commands — the only Pi plugin integrating a structured review workflow into the browser pane | TypeScript |
| **OpenCode** | | | |
| [doublezz10/figure-viewer](https://github.com/doublezz10/figure-viewer) | OpenCode | Display scientific figures in a cmux browser pane with lightbox zoom, freshness timestamps, and auto-refresh — purpose-built for data-science and research workflows where figures change frequently | JavaScript |
| [mspiegel31/opencode-cmux](https://github.com/mspiegel31/opencode-cmux) | OpenCode | Expose optional `cmux browser` tools to OpenCode's AI agent alongside subagent viewer panes and desktop notifications — the primary OpenCode integration offering agent-to-agent viewer handoff | TypeScript |
| **Multi / Other** | | | |
| [darkspock/cmux-skill](https://github.com/darkspock/cmux-skill) | Multi | Teach agents the full `cmux browser` surface covering DOM interaction, JS eval, cookies, tab management, dialogs, and frames — the most starred standalone skill document for browser subcommands | Markdown · ★7 |
| [multiagentcognition/cmux-agent-mcp](https://github.com/multiagentcognition/cmux-agent-mcp) | Multi | Include browser automation as one capability among 81 MCP tools for multi-agent workspace orchestration — browser control is a supporting feature within a much larger multi-agent coordination toolkit | TypeScript |
| [EtanHey/cmuxlayer](https://github.com/EtanHey/cmuxlayer) | Multi | Provide browser control tools alongside 22 other MCP tools for workspace management — a compact multi-tool server where browser access complements pane and session management rather than standing alone | TypeScript |

### 7. Worktrees & Workspace Management

Git worktrees give each agent an isolated copy of the repository on a separate branch — no merge conflicts, no stepping on each other's changes. The best plugins create a worktree, open a cmux workspace for it, launch an agent inside, and clean up when the branch merges. This is the foundation for safe parallel development.

> **Recommended**: [craigsc/cmux](https://github.com/craigsc/cmux) (477 stars, tmux-based gold standard for worktree UX), [kdcokenny/opencode-worktree](https://github.com/kdcokenny/opencode-worktree) (392 stars, most popular OpenCode option), [aschreifels/cwt](https://github.com/aschreifels/cwt) for Claude Code with ticket integration.

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| **Claude Code** | | | |
| [craigsc/cmux](https://github.com/craigsc/cmux) | Claude Code | Wrap the full git worktree lifecycle — create, switch, merge, and teardown — into single shell commands with tab completion and shared git history; sets the UX bar every other plugin is measured against | Shell · ★477 |
| [aschreifels/cwt](https://github.com/aschreifels/cwt) | Claude Code | Generate worktrees pre-wired to tickets pulled live from Linear, GitHub, or Jira, then walk through setup via an interactive TUI wizard with draft-mode support for work-in-progress branches | Go |
| [bhandeland/fleet](https://github.com/bhandeland/fleet) | Claude Code | Orchestrate multiple parallel Claude Code worktrees from a single sidebar that shows live session status, lets you spawn named agents per branch, and merges everything back in one command | Shell |
| [Kaldy14/clui](https://github.com/Kaldy14/clui) | Claude Code | Wrap Claude Code in an Electron GUI where every conversation thread gets its own git worktree, and idle threads are LRU-hibernated to keep resource usage bounded | TypeScript |
| [hopchouinard/cmux-plugin](https://github.com/hopchouinard/cmux-plugin) | Claude Code | Add worktree-scoped workspaces to cmux with automatic tab renaming, progress bars, and browser splits — lighter than fleet but covers the core create/switch/close loop | Shell |
| [dagster-io/erk](https://github.com/dagster-io/erk) | Claude Code | Execute implementation plans by checking out isolated worktrees via `cmux checkout`/`cmux teleport`, running agent steps inside, and submitting a PR automatically on completion | Python · ★78 |
| [tasuku43/kra](https://github.com/tasuku43/kra) | Claude Code | Map every open ticket one-to-one to a cmux workspace on disk, auto-creating the worktree when a task opens and removing it when the task closes — ticket state drives filesystem state | Go |
| [baixianger/claude-orchestration-in-cmux](https://github.com/baixianger/claude-orchestration-in-cmux) | Claude Code | Coordinate multi-agent parallel work by delegating subtasks to dedicated worktree panes and driving merge cycles through pane-level Claude Code invocations | Markdown |
| [Stealinglight/cmux-claude-code-skill](https://github.com/Stealinglight/cmux-claude-code-skill) | Claude Code | Teach Claude Code itself to manage worktree sessions via skills, bundling browser-open, sidebar-attach, and system-notification hooks alongside the worktree create/destroy primitives | Shell |
| [wwaIII/proj](https://github.com/wwaIII/proj) | Claude Code | Launch named cmux workspaces through a Rust TUI project picker that marks sessions running Claude Code with `[CC]` activity badges for at-a-glance fleet visibility | Rust |
| **Pi** | | | |
| [bjacobso/pimux](https://github.com/bjacobso/pimux) | Pi | Give each parallel Pi agent its own isolated worktree and dedicated workspace pane, with a sidebar showing live diff status and a structured review workflow before merging | TypeScript |
| [javiermolinar/pi-cmux](https://github.com/javiermolinar/pi-cmux) | Pi | Extend Pi sessions with git worktree branching that passes handoff context between agents, plus 12+ slash commands covering pane splits and zoxide-powered directory jumps | TypeScript · ★6 |
| **OpenCode** | | | |
| [kdcokenny/opencode-worktree](https://github.com/kdcokenny/opencode-worktree) | OpenCode | Spawn a dedicated terminal with OpenCode running inside each new git worktree, sync files via post-checkout hooks, and auto-commit staged changes on worktree deletion | TypeScript · ★392 |
| [kdcokenny/opencode-workspace](https://github.com/kdcokenny/opencode-workspace) | OpenCode | Bundle worktree isolation as one of 16 composable OpenCode workspace components, tying it into a broader multi-agent orchestration layer rather than treating it as a standalone script | TypeScript · ★292 |
| **Multi / Other** | | | |
| [eunjae-lee/cmux-worktree](https://github.com/eunjae-lee/cmux-worktree) | — | Drive worktree creation from a declarative YAML workspace definition, supporting custom pre/post workflows, configurable split layouts, and per-pane isolated browser storage | TypeScript |
| [rjwittams/flotilla](https://github.com/rjwittams/flotilla) | Multi | Correlate branches, open PRs, and issues across multiple repos simultaneously, with agent hook integration that triggers worktree setup and teardown from CI/PR events | Rust |

### 8. Monitoring & Session Restore

Agents can run for hours. When cmux restarts, crashes, or you close the lid, you need to pick up exactly where you left off. Session restore plugins snapshot running sessions and recreate them. Monitoring plugins give you a bird's-eye view of what every agent is doing across all workspaces.

> **Recommended**: [STRML/cmux-restore](https://github.com/STRML/cmux-restore) for Claude Code session mapping, [drolosoft/cmux-resurrect](https://github.com/drolosoft/cmux-resurrect) for full workspace restore with Markdown blueprints.

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| **Claude Code** | | | |
| [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) | Claude Code | Render a live TUI widget that tracks elapsed time and per-sub-agent progress while Claude Code orchestrates work across multiplexer panes — distinct from dashboard tools in that it surfaces timing and completion percentage, not session state | TypeScript · ★251 |
| [AtAFork/ghostty-claude-code-session-restore](https://github.com/AtAFork/ghostty-claude-code-session-restore) | Claude Code | Snapshot Claude Code session IDs every 2 seconds via launchd, resolve each ID to its cmux surface, and replay the full session layout into the correct panes on relaunch — optimized for Ghostty terminal | Python · ★22 |
| [maedana/crmux](https://github.com/maedana/crmux) | Claude Code | Embed a persistent tmux sidebar that shows live permission mode, repo, branch, and worktree for every active Claude Code session — reads directly from agent state rather than scraping status bars | Rust · ★20 |
| [hummer98/cmux-team](https://github.com/hummer98/cmux-team) | Claude Code | Monitor a conductor-and-workers Claude Code swarm in real time via a TUI dashboard wired to a task queue daemon — surfaces per-worker status and queue depth, not just top-level session state | TypeScript · ★9 |
| [STRML/cmux-restore](https://github.com/STRML/cmux-restore) | Claude Code | Map each Claude Code session ID to its surface UUID via a `SessionStart` hook, then resume exact sessions after cmux restarts — hook-driven approach avoids polling and survives rapid restarts | Shell |
| [claude-studio/claude-studio](https://github.com/claude-studio/claude-studio) | Claude Code | Parse JSONL transcripts to visualize cumulative cost, token burn rate, and session statistics on a dashboard with live agent state — cost-focused counterpart to status-bar scrapers | TypeScript |
| [alaasdk/cmux-ctl](https://github.com/alaasdk/cmux-ctl) | Claude Code | Display a real-time Textual TUI dashboard of all workspaces with agent state tracking and notification badges — pulls state from the cmux socket rather than terminal scraping | Python |
| [taichiiwamoto-s/cmux-context](https://github.com/taichiiwamoto-s/cmux-context) | Claude Code | Scrape Claude status bars from every workspace and render a context-fill dashboard with model and rate limit info — complements socket-based monitors by exposing token headroom | Shell |
| [bocktae80/cmux-pilot](https://github.com/bocktae80/cmux-pilot) | Claude Code | Resume all workspace sessions after a system restart by maintaining a persistent workspace-to-session mapping — single-command bulk replay distinct from per-session hook approaches | Shell |
| [wrock/wezterm-agent-cards](https://github.com/wrock/wezterm-agent-cards) | Claude Code | Display real-time color-coded status cards for Claude Code sessions in a WezTerm sidebar — WezTerm-native alternative to tmux sidebar monitors | Python |
| [theforager/cmux](https://github.com/theforager/cmux) | Claude Code | Provide an interactive tmux session selector with real-time status indicators tuned for low-bandwidth mobile SSH connections — prioritizes minimal rendering over rich dashboards | Shell |
| **Multi / Other** | | | |
| [rjwittams/flotilla](https://github.com/rjwittams/flotilla) | Multi | Correlate agents, branches, and PRs across multiple repos into unified work items via a TUI dashboard — cross-repo aggregation makes it distinct from single-workspace monitoring tools | Rust |
| [owizdom/context-brdige-for-cmux](https://github.com/owizdom/context-brdige-for-cmux) | Multi | Poll panes from any agent, extract structured context, persist snapshots to SQLite, and auto-inject compressed handoff briefs into new sessions — persistence layer differentiates it from in-memory restore tools | Go |
| [drolosoft/cmux-resurrect](https://github.com/drolosoft/cmux-resurrect) | — | Save and restore full workspaces including splits, CWDs, running commands, and Markdown workspace blueprints with dry-run preview — blueprint export makes rebuilding layouts reproducible without relying on session IDs | Go |
| [meengi07/cmux-agent-observer-skill](https://github.com/meengi07/cmux-agent-observer-skill) | Multi | Track worker sub-agent progress from the cmux sidebar using structured handoff notes written to a dedicated directory — file-based coordination approach contrasts with socket or daemon-driven monitors | Shell |
| [ensarkovankaya/cmux-mirror](https://github.com/ensarkovakaya/cmux-mirror) | — | Mirror a remote cmux layout to a local instance over SSH with incremental sync support — observability tool focused on remote-to-local layout replication rather than agent state | Python |
| [gonzaloserrano/streamdeck-cmux](https://github.com/gonzaloserrano/streamdeck-cmux) | — | Read workspace state from the cmux socket and display it on Stream Deck hardware buttons — physical-hardware output layer complementing software dashboards | TypeScript · ★7 |

### 9. Remote & Mobile Access

Sometimes you need to check on your agents from another room — or another device entirely. These projects bridge cmux to mobile apps, web browsers, and SSH sessions.

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [hummer98/cmux-remote](https://github.com/hummer98/cmux-remote) | — | Self-host a PWA bridge that streams live workspace state to any browser over WebSocket, rendering panes with xterm.js and supporting surface switching without an SSH tunnel | TypeScript |
| [ensarkovankaya/cmux-mirror](https://github.com/ensarkovakaya/cmux-mirror) | — | Mirror a remote cmux workspace's full pane and window structure to a local instance over SSH, keeping layouts in sync without manual replication | Python |
| [itsmaleen/cmux-companion](https://github.com/itsmaleen/cmux-companion) | — | Push cmux notifications to an iPhone app and cycle workspaces with the volume buttons, voice commands, or landscape-optimised tap targets | Go / Swift |
| [rappdw/zen-term](https://github.com/rappdw/zen-term) | Claude Code | Connect a local MacBook to a remote DGX Spark over Mosh, maintaining session continuity across flaky links with OSC 777 notification rings for agent events | Shell |
| [theforager/cmux](https://github.com/theforager/cmux) | Claude Code | Present a compact, mobile-friendly tmux session selector with narrow columns tuned for Terminus on iOS, so agents can be checked and switched from a phone | Shell |

---

### 10. Themes, Layouts & Config

The right layout turns cmux from a terminal into a development cockpit. Three-pane setups with a file browser, agent, and git sidebar are popular. Themes set the mood; config tweaks (scrollback, opacity, key bindings) make everything feel right.

| Repo | Agent | Description | Lang |
|------|-------|-------------|------|
| [jacobtellep/cmux-setup](https://github.com/jacobtellep/cmux-setup) | Claude Code | Replicate Conductor's IDE-style 3-pane layout — Claude agent, lazygit, and dev server — in a single bootstrap command with a dark-teal colour scheme | Shell |
| [budah1987/cmux-script](https://github.com/budah1987/cmux-script) | Claude Code | Launch an interactive project picker that opens yazi, lazygit, and Claude Code in a 3-pane layout and auto-starts the appropriate dev server for the selected project | Shell |
| [budah1987/homebrew-tools](https://github.com/budah1987/homebrew-tools) | Claude Code | Distribute the cmux workspace launcher above as a Homebrew formula, resolving yazi, lazygit, and dev-tool dependencies so any Mac can install it in one command | Ruby |
| [Mirksen/cmux-toolkit](https://github.com/Mirksen/cmux-toolkit) | Claude Code | Open files edited by Claude in a dedicated Vim subpane and toggle a broot file-browser sidebar per session, keeping the agent view uncluttered | Shell |
| [jhta/cmux-skill](https://github.com/jhta/cmux-skill) | Claude Code | Teach Claude Code Neovim-centric editing patterns: open files at the right line, render delta diffs, and run tests in adjacent panes without leaving the agent window | Shell |
| [KyleJamesWalker/cc-cmux-plugin](https://github.com/KyleJamesWalker/cc-cmux-plugin) | Claude Code | Inject a full cmux command reference into every Claude session context and auto-grant required CLI permissions, with a live sidebar showing session status | — |
| [blueraai/bluera-base](https://github.com/blueraai/bluera-base) | Claude Code | Establish shared multi-language conventions enforced by `PostToolUse` hooks that run validation and quality gates automatically after every Claude tool call | Shell |
| [wwaIII/proj](https://github.com/wwaIII/proj) | Claude Code | Browse and launch named cmux workspaces from a fast TUI project picker, showing per-workspace activity badges so Claude sessions are easy to locate and resume | Rust |
| [rappdw/zen-term](https://github.com/rappdw/zen-term) | Claude Code | Configure three distinct Zellij layouts for different workflow modes, with dynamic agent status indicators and reproducible environment bootstrapping via Nix | Shell |
| [javiermolinar/pi-cmux](https://github.com/javiermolinar/pi-cmux) | Pi | Add 12+ slash commands to Pi for vertical/horizontal splits, zoxide directory jumps, and dedicated PR review panes without leaving the Pi conversation | TypeScript · ★6 |
| [wolffiex/cmux](https://github.com/wolffiex/cmux) | — | Manage tmux window arrangements through a popup UI featuring a visual carousel, 10 named preset layouts, and AI-generated summaries of each window's current activity | TypeScript |
| [eunjae-lee/cmux-worktree](https://github.com/eunjae-lee/cmux-worktree) | — | Declare workspace layouts in YAML with split-pane definitions, suspended background tabs, and isolated browser storage per git worktree for clean parallel branches | TypeScript |
| [drolosoft/cmux-resurrect](https://github.com/drolosoft/cmux-resurrect) | — | Save and restore full workspace layouts using Markdown blueprint files that are Obsidian-compatible and git-versionable, surviving reboots without a tmux plugin manager | Go |
| [stevenocchipinti/raycast-cmux](https://github.com/stevenocchipinti/raycast-cmux) | — | Search, focus, and manage cmux workspaces and panes directly from Raycast with keyboard-driven commands, eliminating the need to touch the mouse or switch apps | TypeScript |
| [karlorz/dev-docs-cmux](https://github.com/karlorz/dev-docs-cmux) | — | Fetch and keep current LLM-optimised documentation for cmux dependencies via a make-driven workflow, ensuring agents always have accurate API references in context | Shell |
| [jcyamacho/zdotfiles](https://github.com/jcyamacho/zdotfiles) | — | Wire up a Zsh environment with Antidote plugin management, Starship prompt, and opinionated install helpers for cmux, fzf, zoxide, and git-worktree workflows | Zsh |
| [chrisliu298/ghostty-config](https://github.com/chrisliu298/ghostty-config) | — | Configure Ghostty with a GitHub Dark theme, Berkeley Mono 18pt, 128 MiB scrollback buffer, and cmux-ready key bindings tuned for long agent sessions | — |
| [danneu/danterm](https://github.com/danneu/danterm) | — | Build a macOS terminal on libghostty with vertical tab strips, split panes, collapsible tab groups, and JSON-serialised layout restore across restarts | Swift |
| [davis7dotsh/my-term](https://github.com/davis7dotsh/my-term) | — | Prototype a native macOS terminal emulator with an Arc-style persistent sidebar and long-lived SwiftTerm sessions designed to host cmux workspaces indefinitely | Swift |

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

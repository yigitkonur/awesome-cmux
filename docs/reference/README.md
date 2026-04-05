# cmux Documentation Reference

Self-contained reference documentation mirrored from [cmux.com/docs](https://cmux.com/docs). Each page is a comprehensive, standalone document covering one aspect of cmux.

## Core

| Document | Description |
|----------|-------------|
| [Getting Started](./getting-started.md) | Installation, CLI setup, auto-updates, session restore, and system requirements |
| [Concepts](./concepts.md) | The Window > Workspace > Pane > Surface > Panel hierarchy and how to navigate it |
| [Configuration](./configuration.md) | Ghostty config, `settings.json` schema reference with every supported key |
| [Custom Commands](./custom-commands.md) | `cmux.json` format for command palette commands and declarative workspace layouts |
| [Keyboard Shortcuts](./keyboard-shortcuts.md) | All default shortcuts with binding keys for customization, including chord support |

## API & Automation

| Document | Description |
|----------|-------------|
| [API Reference](./api.md) | Full CLI and Unix socket JSON-RPC protocol — workspaces, splits, input, notifications, sidebar metadata |
| [Browser Automation](./browser-automation.md) | 40+ `cmux browser` subcommands — navigation, DOM interaction, inspection, JS eval, state management |
| [Notifications](./notifications.md) | Desktop notifications via CLI, OSC 777/99, Claude Code hooks, and Copilot CLI hooks |
| [SSH](./ssh.md) | Remote workspaces with browser proxying, drag-and-drop scp, notification relay, and auto-reconnect |

## Agent Integrations

| Document | Description |
|----------|-------------|
| [Claude Code Teams](./claude-code-teams.md) | `cmux claude-teams` — teammate agents as native cmux splits via tmux shim translation |
| [oh-my-opencode](./oh-my-opencode.md) | `cmux omo` — OpenCode with oh-my-openagent multi-model orchestration in cmux splits |

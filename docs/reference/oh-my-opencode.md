# oh-my-opencode

> **Source:** [cmux.com/docs/agent-integrations/oh-my-opencode](https://cmux.com/docs/agent-integrations/oh-my-opencode)

`cmux omo` launches OpenCode with the oh-my-openagent plugin in a cmux-aware environment. oh-my-openagent orchestrates multiple AI models (Claude, GPT, Gemini, Grok) as specialized agents working in parallel. When it spawns agent panes, they become native cmux splits.

---

## Usage

```sh
cmux omo
cmux omo --continue
cmux omo --model claude-sonnet-4-6
```

All arguments after `omo` are forwarded to OpenCode.

---

## What You Get

oh-my-openagent's `TmuxSessionManager` spawns each background agent in its own pane. With `cmux omo`, those panes become native cmux splits instead of tmux panes:

- Each subagent (Hephaestus, Atlas, Oracle, etc.) gets its own cmux split, visible in the workspace
- Auto-layout management: agents are arranged in a grid (main-vertical by default) and resized as agents come and go
- Idle agents are automatically cleaned up after 3 consecutive idle polls with no new messages
- If the window is too small for a new agent pane, it queues and retries every 2 seconds until space is available
- Your main session stays in the primary pane while agents work beside it

---

## First Run

On first run, `cmux omo` automatically sets up everything:

1. Creates a shadow config at `~/.cmuxterm/omo-config/` with oh-my-opencode registered in the plugin array
2. Installs the `oh-my-opencode` npm package using bun or npm if not already present
3. Symlinks `node_modules`, `package.json`, and plugin config from your original `~/.config/opencode/` directory
4. Enables tmux mode in the oh-my-opencode config (`tmux.enabled` defaults to false, `cmux omo` turns it on)

> Your original `~/.config/opencode/` config is never modified. Running plain `opencode` works the same as before.

---

## How It Works

Same pattern as `cmux claude-teams`. A tmux shim intercepts tmux commands from oh-my-openagent's `TmuxSessionManager` and translates them into cmux API calls.

1. Creates a tmux shim at `~/.cmuxterm/omo-bin/tmux` that redirects to `cmux __tmux-compat`
2. Sets `TMUX` and `TMUX_PANE` to simulate a tmux session
3. Enables `tmux.enabled` in the oh-my-opencode config (required for visual pane spawning)
4. Points `OPENCODE_CONFIG_DIR` at the shadow config
5. Prepends the shim directory to `PATH` and execs into opencode

---

## Directories

| Path | Purpose |
|------|---------|
| `~/.cmuxterm/omo-bin/` | Contains the tmux shim script |
| `~/.cmuxterm/omo-config/` | Shadow OpenCode config with oh-my-opencode plugin registered and tmux enabled (symlinks to your original config) |
| `~/.cmuxterm/tmux-compat-store.json` | Persistent storage for tmux-compat buffers and hooks |

---

## Shadow Config

`cmux omo` uses a shadow config directory so your original OpenCode setup is unaffected:

- Copies your `~/.config/opencode/opencode.json` with oh-my-opencode added to the plugin array
- Symlinks `node_modules`, `package.json`, and `bun.lock` from the original directory
- Writes `oh-my-opencode.json` with `tmux.enabled` set to `true`
- Sets `OPENCODE_CONFIG_DIR` to the shadow directory before launching opencode

---

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `TMUX` | Fake tmux socket path encoding the current cmux workspace and pane |
| `TMUX_PANE` | Fake tmux pane identifier mapped to the current cmux pane |
| `OPENCODE_CONFIG_DIR` | Points to the shadow config directory with oh-my-opencode enabled |
| `CMUX_SOCKET_PATH` | Path to the cmux control socket for the shim to connect to |

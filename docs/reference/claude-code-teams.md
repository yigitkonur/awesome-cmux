# Claude Code Teams

> **Source:** [cmux.com/docs/agent-integrations/claude-code-teams](https://cmux.com/docs/agent-integrations/claude-code-teams)

`cmux claude-teams` launches Claude Code with agent teams enabled. When Claude spawns teammate agents, they appear as native cmux splits instead of tmux panes, with full sidebar metadata and notifications.

---

## Usage

```sh
cmux claude-teams
cmux claude-teams --continue
cmux claude-teams --model sonnet
```

All arguments after `claude-teams` are forwarded to Claude Code. The command defaults teammate mode to `auto` and sets the environment so Claude uses cmux splits.

---

## How It Works

`cmux claude-teams` creates a tmux shim script and configures the environment so Claude Code thinks it's running inside tmux. When Claude issues tmux commands to manage teammate panes, the shim translates them into cmux socket API calls.

1. Creates a tmux shim at `~/.cmuxterm/claude-teams-bin/tmux` that redirects to `cmux __tmux-compat`
2. Sets `TMUX` and `TMUX_PANE` environment variables to simulate a tmux session
3. Prepends the shim directory to `PATH` so Claude finds the shim before real tmux
4. Enables `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` and sets teammate mode to `auto`

---

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `TMUX` | Fake tmux socket path encoding the current cmux workspace and pane |
| `TMUX_PANE` | Fake tmux pane identifier mapped to the current cmux pane |
| `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` | Enables Claude Code agent teams feature |
| `CMUX_SOCKET_PATH` | Path to the cmux control socket for the shim to connect to |

---

## Directories

| Path | Purpose |
|------|---------|
| `~/.cmuxterm/claude-teams-bin/` | Contains the tmux shim script that translates tmux commands to cmux API calls |
| `~/.cmuxterm/tmux-compat-store.json` | Persistent storage for tmux-compat buffers and hooks |

---

## Supported tmux Commands

The shim translates these tmux commands into cmux operations:

| tmux Command | cmux Operation |
|-------------|----------------|
| `new-session`, `new-window` | Creates a new cmux workspace |
| `split-window` | Splits the current cmux pane |
| `send-keys` | Sends text to a cmux surface |
| `capture-pane` | Reads terminal text from a cmux surface |
| `select-pane`, `select-window` | Focuses a cmux pane or workspace |
| `kill-pane`, `kill-window` | Closes a cmux surface or workspace |
| `list-panes`, `list-windows` | Lists cmux panes or workspaces |

# SSH

> **Source:** [cmux.com/docs/ssh](https://cmux.com/docs/ssh)

`cmux ssh` creates a workspace for a remote machine. Browser panes route through the remote network, files drag-and-drop via scp, coding agents send notifications to your local sidebar, and sessions reconnect on drops.

---

## Usage

```sh
cmux ssh user@remote
cmux ssh user@remote --name "dev server"
cmux ssh user@remote -p 2222
cmux ssh user@remote -i ~/.ssh/id_ed25519
```

cmux ssh reads your `~/.ssh/config` for host aliases, identity files, and proxy settings. All flags mirror their ssh equivalents.

---

## Flags

| Flag | Description |
|------|-------------|
| `--name` | Set the workspace title |
| `-p, --port` | SSH port (default 22) |
| `-i, --identity` | Path to identity file |
| `-o, --ssh-option` | Pass arbitrary SSH options (e.g. `-o StrictHostKeyChecking=no`) |
| `--no-focus` | Create the workspace without switching to it |

---

## Browser Panes

Browser panes in a remote workspace route all HTTP and WebSocket traffic through the remote machine's network. Type `localhost:3000` and you're looking at the dev server running on the remote box. No `-L` flags, no manual port forwarding. Each remote workspace gets an isolated cookie store so sessions are scoped per-connection.

---

## Drag and Drop

Drag an image or file into a remote terminal and cmux uploads it via scp through the existing SSH connection. cmux detects the foreground SSH process by TTY and routes the upload through ControlMaster multiplexing.

---

## Notifications

Processes on the remote machine can run cmux commands that execute on your local instance. When a coding agent calls `cmux notify` on the remote box, the notification appears in your local sidebar. The blue ring lights up on the workspace tab. `Cmd+Shift+U` jumps to it. Notification spam from flaky connections is suppressed with a per-host cooldown.

---

## Coding Agents over SSH

`cmux claude-teams` and `cmux omo` both work inside SSH sessions. The Go relay daemon on the remote host handles the same tmux-compat translation that the local Swift CLI does. Teammate agents spawn as native cmux splits on your local machine while computation runs on the remote box.

```sh
# Inside an SSH session:
cmux claude-teams
cmux omo
```

---

## Reconnect

When the connection drops, cmux reconnects with exponential backoff (3s, 6s, 12s, up to 60s). The remote session persists and cmux reattaches on reconnect, resizing with smallest-screen-wins semantics. Default keepalive options (`ServerAliveInterval=20`, `ServerAliveCountMax=2`) are injected unless your config already sets them.

---

## Relay Daemon

On first connect, cmux probes the remote host (`uname -s`, `uname -m`) and uploads a versioned `cmuxd-remote` binary. The binary speaks JSON-RPC over stdio and handles three things:

| Feature | How |
|---------|-----|
| Browser traffic proxying | SOCKS5 and HTTP CONNECT over the daemon's stdio channel |
| CLI relay | Reverse TCP tunnel with HMAC-SHA256 auth so remote processes can call cmux commands locally |
| Session management | Persists sessions across reconnects, coordinates PTY resize across multiple attachments |

The daemon binary is stored at `~/.cmux/bin/cmuxd-remote/<version>/<os>-<arch>/cmuxd-remote` on the remote host and verified against a SHA-256 manifest embedded in the app.

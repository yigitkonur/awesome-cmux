# API Reference

> **Source:** [cmux.com/docs/api](https://cmux.com/docs/api)

cmux provides both a CLI tool and a Unix socket for programmatic control. Every command is available through both interfaces.

---

## Socket

| Build | Path |
|-------|------|
| Release | `/tmp/cmux.sock` |
| Debug | `/tmp/cmux-debug.sock` |
| Tagged debug build | `/tmp/cmux-debug-<tag>.sock` |

Override with the `CMUX_SOCKET_PATH` environment variable. Send one newline-terminated JSON request per call:

```json
{"id":"req-1","method":"workspace.list","params":{}}
// Response:
{"id":"req-1","ok":true,"result":{"workspaces":[...]}}
```

> JSON socket requests must use `method` and `params`. Legacy v1 JSON payloads such as `{"command":"..."}` are not supported.

---

## Access Modes

| Mode | Description | How to enable |
|------|-------------|---------------|
| **Off** | Socket disabled | Settings UI or `CMUX_SOCKET_MODE=off` |
| **cmux processes only** | Only processes spawned inside cmux terminals can connect | Default mode in Settings UI |
| **allowAll** | Allow any local process to connect (no ancestry check) | Environment override only: `CMUX_SOCKET_MODE=allowAll` |

> On shared machines, use **Off** or **cmux processes only**.

---

## CLI Options

| Flag | Description |
|------|-------------|
| `--socket PATH` | Custom socket path |
| `--json` | Output in JSON format |
| `--window ID` | Target a specific window |
| `--workspace ID` | Target a specific workspace |
| `--surface ID` | Target a specific surface |
| `--id-format refs\|uuids\|both` | Control identifier format in JSON output |

---

## Workspace Commands

### list-workspaces

List all open workspaces.

```sh
cmux list-workspaces
cmux list-workspaces --json
```

```json
{"id":"ws-list","method":"workspace.list","params":{}}
```

### new-workspace

Create a new workspace.

```sh
cmux new-workspace
```

```json
{"id":"ws-new","method":"workspace.create","params":{}}
```

### select-workspace

Switch to a specific workspace.

```sh
cmux select-workspace --workspace <id>
```

```json
{"id":"ws-select","method":"workspace.select","params":{"workspace_id":"<id>"}}
```

### current-workspace

Get the currently active workspace.

```sh
cmux current-workspace
cmux current-workspace --json
```

```json
{"id":"ws-current","method":"workspace.current","params":{}}
```

### close-workspace

Close a workspace.

```sh
cmux close-workspace --workspace <id>
```

```json
{"id":"ws-close","method":"workspace.close","params":{"workspace_id":"<id>"}}
```

---

## Split Commands

### new-split

Create a new split pane. Directions: `left`, `right`, `up`, `down`.

```sh
cmux new-split right
cmux new-split down
```

```json
{"id":"split-new","method":"surface.split","params":{"direction":"right"}}
```

### list-surfaces

List all surfaces in the current workspace.

```sh
cmux list-surfaces
cmux list-surfaces --json
```

```json
{"id":"surface-list","method":"surface.list","params":{}}
```

### focus-surface

Focus a specific surface.

```sh
cmux focus-surface --surface <id>
```

```json
{"id":"surface-focus","method":"surface.focus","params":{"surface_id":"<id>"}}
```

---

## Input Commands

### send

Send text input to the focused terminal.

```sh
cmux send "echo hello"
cmux send "ls -la\n"
```

```json
{"id":"send-text","method":"surface.send_text","params":{"text":"echo hello\n"}}
```

### send-key

Send a key press. Keys: `enter`, `tab`, `escape`, `backspace`, `delete`, `up`, `down`, `left`, `right`.

```sh
cmux send-key enter
```

```json
{"id":"send-key","method":"surface.send_key","params":{"key":"enter"}}
```

### send-surface

Send text to a specific surface.

```sh
cmux send-surface --surface <id> "command"
```

```json
{"id":"send-surface","method":"surface.send_text","params":{"surface_id":"<id>","text":"command"}}
```

### send-key-surface

Send a key press to a specific surface.

```sh
cmux send-key-surface --surface <id> enter
```

```json
{"id":"send-key-surface","method":"surface.send_key","params":{"surface_id":"<id>","key":"enter"}}
```

---

## Notification Commands

### notify

Send a notification.

```sh
cmux notify --title "Title" --body "Body"
cmux notify --title "T" --subtitle "S" --body "B"
```

```json
{"id":"notify","method":"notification.create","params":{"title":"Title","subtitle":"S","body":"Body"}}
```

### list-notifications

```sh
cmux list-notifications
cmux list-notifications --json
```

```json
{"id":"notif-list","method":"notification.list","params":{}}
```

### clear-notifications

```sh
cmux clear-notifications
```

```json
{"id":"notif-clear","method":"notification.clear","params":{}}
```

---

## Sidebar Metadata Commands

Set status pills, progress bars, and log entries in the sidebar for any workspace. Useful for build scripts, CI integrations, and AI coding agents that want to surface state at a glance.

### set-status

Set a sidebar status pill. Use a unique key so different tools can manage their own entries.

```sh
cmux set-status build "compiling" --icon hammer --color "#ff9500"
cmux set-status deploy "v1.2.3" --workspace workspace:2
```

### clear-status

Remove a sidebar status entry by key.

```sh
cmux clear-status build
```

### list-status

List all sidebar status entries for a workspace.

```sh
cmux list-status
```

### set-progress

Set a progress bar in the sidebar (0.0 to 1.0).

```sh
cmux set-progress 0.5 --label "Building..."
cmux set-progress 1.0 --label "Done"
```

### clear-progress

```sh
cmux clear-progress
```

### log

Append a log entry to the sidebar. Levels: `info`, `progress`, `success`, `warning`, `error`.

```sh
cmux log "Build started"
cmux log --level error --source build "Compilation failed"
cmux log --level success -- "All 42 tests passed"
```

### clear-log / list-log

```sh
cmux clear-log
cmux list-log
cmux list-log --limit 5
```

### sidebar-state

Dump all sidebar metadata (cwd, git branch, ports, status, progress, logs).

```sh
cmux sidebar-state
cmux sidebar-state --workspace workspace:2
```

---

## Utility Commands

### ping

Check if cmux is running and responsive.

```sh
cmux ping
```

```json
{"id":"ping","method":"system.ping","params":{}}
// Response: {"id":"ping","ok":true,"result":{"pong":true}}
```

### capabilities

List available socket methods and current access mode.

```sh
cmux capabilities
cmux capabilities --json
```

```json
{"id":"caps","method":"system.capabilities","params":{}}
```

### identify

Show focused window/workspace/pane/surface context.

```sh
cmux identify
cmux identify --json
```

```json
{"id":"identify","method":"system.identify","params":{}}
```

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `CMUX_SOCKET_PATH` | Override the socket path used by CLI and integrations |
| `CMUX_SOCKET_ENABLE` | Force-enable/disable socket (`1`/`0`, `true`/`false`, `on`/`off`) |
| `CMUX_SOCKET_MODE` | Override access mode (`cmuxOnly`, `allowAll`, `off`) |
| `CMUX_WORKSPACE_ID` | Auto-set: current workspace ID |
| `CMUX_SURFACE_ID` | Auto-set: current surface ID |
| `TERM_PROGRAM` | Set to `ghostty` |
| `TERM` | Set to `xterm-ghostty` |

---

## Detecting cmux

```bash
# Prefer explicit socket path if set
SOCK="${CMUX_SOCKET_PATH:-/tmp/cmux.sock}"
[ -S "$SOCK" ] && echo "Socket available"

# Check for the CLI
command -v cmux &>/dev/null && echo "cmux available"

# In cmux-managed terminals these are auto-set
[ -n "${CMUX_WORKSPACE_ID:-}" ] && [ -n "${CMUX_SURFACE_ID:-}" ] && echo "Inside cmux surface"

# Distinguish from regular Ghostty
[ "$TERM_PROGRAM" = "ghostty" ] && [ -n "${CMUX_WORKSPACE_ID:-}" ] && echo "In cmux"
```

---

## Examples

### Python Client

```python
import json, os, socket

SOCKET_PATH = os.environ.get("CMUX_SOCKET_PATH", "/tmp/cmux.sock")

def rpc(method, params=None, req_id=1):
    payload = {"id": req_id, "method": method, "params": params or {}}
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        sock.connect(SOCKET_PATH)
        sock.sendall(json.dumps(payload).encode("utf-8") + b"\n")
        return json.loads(sock.recv(65536).decode("utf-8"))

# List workspaces
print(rpc("workspace.list", req_id="ws"))

# Send notification
print(rpc("notification.create", {"title": "Hello", "body": "From Python!"}, req_id="notify"))
```

### Shell Script

```bash
#!/bin/bash
SOCK="${CMUX_SOCKET_PATH:-/tmp/cmux.sock}"

cmux_cmd() {
    printf "%s\n" "$1" | nc -U "$SOCK"
}

cmux_cmd '{"id":"ws","method":"workspace.list","params":{}}'
cmux_cmd '{"id":"notify","method":"notification.create","params":{"title":"Done","body":"Task complete"}}'
```

### Build Script with Notification

```bash
#!/bin/bash
npm run build
if [ $? -eq 0 ]; then
    cmux notify --title "Build Success" --body "Ready to deploy"
else
    cmux notify --title "Build Failed" --body "Check the logs"
fi
```

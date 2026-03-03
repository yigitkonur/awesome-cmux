# 02 — Setup, Permissions, and Verification

## Baseline checks

```bash
defaults read /Applications/cmux.app/Contents/Info CFBundleIdentifier
command -v cmux || echo "cmux CLI not on PATH"

cmux ping
cmux capabilities --json | jq '.protocol, .version, (.methods|length)'
```

## AppleScript execution model

Use AppleScript as an orchestrator and call the CLI via shell:

```applescript
do shell script quoted form of "/Applications/cmux.app/Contents/Resources/bin/cmux" & " ping"
```

## Permission matrix

| Action | Typical macOS permission |
|---|---|
| `do shell script` to cmux CLI | no special permission beyond shell execution |
| `tell application id "com.cmuxterm.app" to activate` | may prompt Automation permission depending on runner |
| UI scripting via `System Events` | Accessibility permission required |

## Quick health probe

```applescript
set cmuxCLI to "/Applications/cmux.app/Contents/Resources/bin/cmux"
set pong to do shell script quoted form of cmuxCLI & " ping"
set ws to do shell script quoted form of cmuxCLI & " current-workspace"
return "ping=" & pong & linefeed & "workspace=" & ws
```

## Socket-level probe

```bash
python3 - <<'PY'
import socket, json
s=socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect('/tmp/cmux.sock')
s.sendall((json.dumps({"id":"1","method":"system.ping","params":{}})+"\n").encode())
print(s.recv(65535).decode().strip())
s.close()
PY
```

# Notifications

> **Source:** [cmux.com/docs/notifications](https://cmux.com/docs/notifications)

cmux supports desktop notifications, allowing AI agents and scripts to alert you when they need attention.

---

## Lifecycle

1. **Received** — notification appears in panel, desktop alert fires (if not suppressed)
2. **Unread** — badge shown on workspace tab
3. **Read** — cleared when you view that workspace
4. **Cleared** — removed from panel

### Suppression

Desktop alerts are suppressed when:

- The cmux window is focused
- The specific workspace sending the notification is active
- The notification panel is open

### Notification Panel

- `Cmd+Shift+I` — open the notification panel
- Click a notification to jump to that workspace
- `Cmd+Shift+U` — jump directly to the workspace with the most recent unread notification

---

## Custom Command

Run a shell command every time a notification is scheduled. Set it in **Settings > App > Notification Command**. The command runs via `/bin/sh -c` with these environment variables:

| Variable | Description |
|----------|-------------|
| `CMUX_NOTIFICATION_TITLE` | Notification title (workspace name or app name) |
| `CMUX_NOTIFICATION_SUBTITLE` | Notification subtitle |
| `CMUX_NOTIFICATION_BODY` | Notification body text |

### Examples

```sh
# Text-to-speech
say "$CMUX_NOTIFICATION_TITLE"

# Custom sound file
afplay /path/to/sound.aiff

# Log to file
echo "$CMUX_NOTIFICATION_TITLE: $CMUX_NOTIFICATION_BODY" >> ~/notifications.log
```

The command runs independently of the system sound picker. Set the picker to "None" to use only the custom command, or keep both.

---

## Sending Notifications

### CLI

```sh
cmux notify --title "Task Complete" --body "Your build finished"
cmux notify --title "Claude Code" --subtitle "Waiting" --body "Agent needs input"
```

### OSC 777 (Simple)

The RXVT protocol uses a fixed format with title and body:

```sh
printf '\e]777;notify;My Title;Message body here\a'
```

Shell function:

```sh
notify_osc777() {
    local title="$1"
    local body="$2"
    printf '\e]777;notify;%s;%s\a' "$title" "$body"
}

notify_osc777 "Build Complete" "All tests passed"
```

### OSC 99 (Rich — Kitty Protocol)

Supports subtitles and notification IDs:

```sh
# Simple notification
printf '\e]99;i=1;e=1;d=0:Hello World\e\\'

# With title, subtitle, and body
printf '\e]99;i=1;e=1;d=0;p=title:Build Complete\e\\'
printf '\e]99;i=1;e=1;d=0;p=subtitle:Project X\e\\'
printf '\e]99;i=1;e=1;d=1;p=body:All tests passed\e\\'
```

### Protocol Comparison

| Feature | OSC 99 | OSC 777 |
|---------|--------|---------|
| Title + body | Yes | Yes |
| Subtitle | Yes | No |
| Notification ID | Yes | No |
| Complexity | Higher | Lower |

Use OSC 777 for simple notifications. Use OSC 99 when you need subtitles or notification IDs. Use the CLI (`cmux notify`) for the easiest integration.

---

## Claude Code Hooks

cmux integrates with Claude Code via hooks to notify you when tasks complete.

### 1. Create the Hook Script

```bash
#!/bin/bash
# ~/.claude/hooks/cmux-notify.sh
# Skip if not in cmux
[ -S /tmp/cmux.sock ] || exit 0

EVENT=$(cat)
EVENT_TYPE=$(echo "$EVENT" | jq -r '.hook_event_name // "unknown"')
TOOL=$(echo "$EVENT" | jq -r '.tool_name // ""')

case "$EVENT_TYPE" in
    "Stop")
        cmux notify --title "Claude Code" --body "Session complete"
        ;;
    "PostToolUse")
        [ "$TOOL" = "Task" ] && cmux notify --title "Claude Code" --body "Agent finished"
        ;;
esac
```

```sh
chmod +x ~/.claude/hooks/cmux-notify.sh
```

### 2. Configure Claude Code

```json
// ~/.claude/settings.json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/cmux-notify.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Task",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/cmux-notify.sh"
          }
        ]
      }
    ]
  }
}
```

Restart Claude Code to apply the hooks.

---

## GitHub Copilot CLI Hooks

Copilot CLI supports hooks that run shell commands at lifecycle events.

```json
// ~/.copilot/config.json
{
  "hooks": {
    "userPromptSubmitted": [
      {
        "type": "command",
        "bash": "if command -v cmux &>/dev/null; then cmux set-status copilot_cli Running; fi",
        "timeoutSec": 3
      }
    ],
    "agentStop": [
      {
        "type": "command",
        "bash": "if command -v cmux &>/dev/null; then cmux notify --title 'Copilot CLI' --body 'Done'; cmux set-status copilot_cli Idle; fi",
        "timeoutSec": 5
      }
    ],
    "errorOccurred": [
      {
        "type": "command",
        "bash": "if command -v cmux &>/dev/null; then cmux notify --title 'Copilot CLI' --subtitle 'Error' --body 'An error occurred'; cmux set-status copilot_cli Error; fi",
        "timeoutSec": 5
      }
    ],
    "sessionEnd": [
      {
        "type": "command",
        "bash": "if command -v cmux &>/dev/null; then cmux clear-status copilot_cli; fi",
        "timeoutSec": 3
      }
    ]
  }
}
```

For repo-level hooks, create `.github/hooks/notify.json` with the same structure.

---

## Integration Examples

### Notify After Long Command

```sh
# Add to ~/.zshrc
notify-after() {
  "$@"
  local exit_code=$?
  if [ $exit_code -eq 0 ]; then
    cmux notify --title "Command Complete" --body "$1"
  else
    cmux notify --title "Command Failed" --body "$1 (exit $exit_code)"
  fi
  return $exit_code
}

# Usage: notify-after npm run build
```

### Python

```python
import sys

def notify(title: str, body: str):
    """Send OSC 777 notification."""
    sys.stdout.write(f'\x1b]777;notify;{title};{body}\x07')
    sys.stdout.flush()

notify("Script Complete", "Processing finished")
```

### Node.js

```javascript
function notify(title, body) {
  process.stdout.write(`\x1b]777;notify;${title};${body}\x07`);
}

notify('Build Done', 'webpack finished');
```

### tmux Passthrough

If using tmux inside cmux, enable passthrough:

```
# .tmux.conf
set -g allow-passthrough on
```

```sh
printf '\ePtmux;\e\e]777;notify;Title;Body\a\e\\'
```

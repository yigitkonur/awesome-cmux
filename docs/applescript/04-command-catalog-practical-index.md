# 04 — Command Catalog (Practical Index)

This index is the practical view of the extracted CLI surface.

## Global form

```bash
cmux <path>
cmux [--socket PATH] [--window WINDOW] [--password PASSWORD] [--json] [--id-format refs|uuids|both] <command> [options]
```

## Handle formats

- UUIDs
- refs: `window:N`, `workspace:N`, `pane:N`, `surface:N`
- indexes (where accepted)

## Core workflows

### Window / workspace
- `list-windows`, `current-window`, `new-window`, `focus-window`, `close-window`
- `list-workspaces`, `new-workspace`, `select-workspace`, `current-workspace`, `close-workspace`, `reorder-workspace`

### Pane / surface
- `list-panes`, `focus-pane`, `new-pane`
- `new-surface`, `move-surface`, `reorder-surface`, `close-surface`, `surface-health`
- `new-split`, `drag-surface-to-split`

### Terminal I/O
- `read-screen`, `send`, `send-key`, `send-panel`, `send-key-panel`

### Notification + sidebar metadata
- `notify`, `list-notifications`, `clear-notifications`
- `set-status`, `list-status`, `set-progress`, `log`, `sidebar-state`

### Browser
- `browser open`, `open-split`, `navigate`, `snapshot`, `eval`, `wait`, `click`, `type`, `fill`, `get`, `find`, `identify`

### tmux-style compatibility
- `capture-pane`, `resize-pane`, `swap-pane`, `break-pane`, `join-pane`, `clear-history`, `set-buffer`, `paste-buffer`

For a complete command set, use:

```bash
cmux help
cmux browser --help
```

# 07 — Runtime v2 Method Inventory

Total runtime methods in source snapshot: **172**.

## Family counts

| Family | Count |
|---|---:|
| app | 2 |
| auth | 1 |
| browser | 84 |
| debug | 29 |
| notification | 5 |
| pane | 9 |
| surface | 17 |
| system | 4 |
| tab | 1 |
| target | 3 |
| window | 5 |
| workspace | 12 |

## High-value methods by family

- **system**: `system.ping`, `system.capabilities`, `system.identify`, `system.tree`
- **workspace**: `workspace.create`, `workspace.select`, `workspace.current`, `workspace.list`
- **surface**: `surface.create`, `surface.split`, `surface.focus`, `surface.send_text`, `surface.read_text`
- **pane**: `pane.create`, `pane.list`, `pane.focus`, `pane.resize`
- **notification**: `notification.create`, `notification.list`, `notification.clear`
- **browser**: `browser.navigate`, `browser.snapshot`, `browser.eval`, `browser.wait`, `browser.get.*`, `browser.find.*`, `browser.tab.*`
- **debug**: `debug.window.screenshot`, `debug.terminal.read_text`, `debug.layout`

## Suggested refresh command

```bash
cmux capabilities --json | jq '.methods | length, .[0:20]'
```

Use this file as a family-level map; query live capabilities before automating production workflows.

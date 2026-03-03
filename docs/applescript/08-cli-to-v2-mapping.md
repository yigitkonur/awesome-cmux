# 08 — CLI / Legacy to v2 Mapping

Key migration mappings from legacy command families to v2 methods.

| Legacy / CLI family | v2 method |
|---|---|
| `list_windows` | `window.list` |
| `current_window` | `window.current` |
| `new_window` | `window.create` |
| `close_window` | `window.close` |
| `list_workspaces` | `workspace.list` |
| `new_workspace` | `workspace.create` |
| `select_workspace` | `workspace.select` |
| `current_workspace` | `workspace.current` |
| `close_workspace` | `workspace.close` |
| `list_surfaces` | `surface.list` |
| `new_surface` | `surface.create` |
| `new_split` | `surface.split` |
| `send` | `surface.send_text` |
| `send_key` | `surface.send_key` |
| `notify` | `notification.create` |
| `list_notifications` | `notification.list` |
| `clear_notifications` | `notification.clear` |
| `open_browser` | `browser.open_split` |
| `navigate` | `browser.navigate` |
| `browser_reload` | `browser.reload` |
| `get_url` | `browser.url.get` |
| `set_app_focus` | `app.focus_override.set` |
| `simulate_app_active` | `app.simulate_active` |
| `screenshot` | `debug.window.screenshot` |

For broader migration notes: see cmux `docs/v2-api-migration.md`.

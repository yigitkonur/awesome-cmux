# Keyboard Shortcuts

> **Source:** [cmux.com/docs/keyboard-shortcuts](https://cmux.com/docs/keyboard-shortcuts)

Default cmux keyboard shortcuts. Every cmux-owned shortcut can be changed in Settings or `~/.config/cmux/settings.json`, including two-step chords.

---

## Shortcut Chords

cmux supports two-step shortcut chords in `~/.config/cmux/settings.json`:

```jsonc
{
  "shortcuts": {
    "bindings": {
      "newSurface": ["ctrl+b", "c"],
      "showNotifications": ["ctrl+b", "i"],
      "toggleSidebar": "cmd+b"
    }
  }
}
```

- Use a plain string for a one-step shortcut
- Use a two-item array for a chord (prefix stroke + following key)
- Each item uses the same syntax: `cmd+b`, `ctrl+b`, `shift+/`, `ctrl+1`

---

## App

Application, window, and top-level command shortcuts.

| Action | Shortcut | Binding key |
|--------|----------|-------------|
| Settings | `Cmd+,` | `openSettings` |
| Reload configuration | `Cmd+Shift+,` | `reloadConfiguration` |
| Command palette | `Cmd+Shift+P` | `commandPalette` |
| New window | `Cmd+Shift+N` | `newWindow` |
| Close window | `Ctrl+Cmd+W` | `closeWindow` |
| Toggle full screen | `Ctrl+Cmd+F` | `toggleFullScreen` |
| Send feedback | `Opt+Cmd+F` | `sendFeedback` |
| Quit cmux | `Cmd+Q` | `quit` |

---

## Workspaces

Workspaces live in the sidebar. Each workspace has its own set of panes and surfaces.

| Action | Shortcut | Binding key |
|--------|----------|-------------|
| Toggle sidebar | `Cmd+B` | `toggleSidebar` |
| New workspace | `Cmd+N` | `newTab` |
| Open folder | `Cmd+O` | `openFolder` |
| Go to workspace (switcher) | `Cmd+P` | `goToWorkspace` |
| Next workspace | `Ctrl+Cmd+]` | `nextSidebarTab` |
| Previous workspace | `Ctrl+Cmd+[` | `prevSidebarTab` |
| Select workspace 1-9 | `Cmd+1`-`Cmd+9` | `selectWorkspaceByNumber` |
| Rename workspace | `Cmd+Shift+R` | `renameWorkspace` |
| Close workspace | `Cmd+Shift+W` | `closeWorkspace` |

---

## Surfaces

Surfaces are tabs inside a pane.

| Action | Shortcut | Binding key |
|--------|----------|-------------|
| New surface | `Cmd+T` | `newSurface` |
| Next surface | `Cmd+Shift+]` | `nextSurface` |
| Previous surface | `Cmd+Shift+[` | `prevSurface` |
| Select surface 1-9 | `Ctrl+1`-`Ctrl+9` | `selectSurfaceByNumber` |
| Rename tab | `Cmd+R` | `renameTab` |
| Close tab | `Cmd+W` | `closeTab` |
| Close other tabs in pane | `Opt+Cmd+T` | `closeOtherTabsInPane` |
| Reopen closed browser panel | `Cmd+Shift+T` | `reopenClosedBrowserPanel` |
| Toggle terminal copy mode | `Cmd+Shift+M` | `toggleTerminalCopyMode` |

---

## Split Panes

| Action | Shortcut | Binding key |
|--------|----------|-------------|
| Focus pane left | `Opt+Cmd+Left` | `focusLeft` |
| Focus pane right | `Opt+Cmd+Right` | `focusRight` |
| Focus pane up | `Opt+Cmd+Up` | `focusUp` |
| Focus pane down | `Opt+Cmd+Down` | `focusDown` |
| Split right | `Cmd+D` | `splitRight` |
| Split down | `Cmd+Shift+D` | `splitDown` |
| Split browser right | `Opt+Cmd+D` | `splitBrowserRight` |
| Split browser down | `Opt+Cmd+Shift+D` | `splitBrowserDown` |
| Toggle pane zoom | `Cmd+Shift+Enter` | `toggleSplitZoom` |

---

## Browser

| Action | Shortcut | Binding key |
|--------|----------|-------------|
| Open browser | `Cmd+Shift+L` | `openBrowser` |
| Focus address bar | `Cmd+L` | `focusBrowserAddressBar` |
| Back | `Cmd+[` | `browserBack` |
| Forward | `Cmd+]` | `browserForward` |
| Reload page | `Cmd+R` | `browserReload` |
| Zoom in | `Cmd+=` | `browserZoomIn` |
| Zoom out | `Cmd+-` | `browserZoomOut` |
| Actual size | `Cmd+0` | `browserZoomReset` |
| Toggle developer tools | `Opt+Cmd+I` | `toggleBrowserDeveloperTools` |
| Show JavaScript console | `Opt+Cmd+C` | `showBrowserJavaScriptConsole` |
| Toggle React Grab | `Opt+Cmd+G` | `toggleReactGrab` |

---

## Find

| Action | Shortcut | Binding key |
|--------|----------|-------------|
| Find | `Cmd+F` | `find` |
| Find next | `Cmd+G` | `findNext` |
| Find previous | `Cmd+Shift+G` | `findPrevious` |
| Hide find bar | `Cmd+Shift+F` | `hideFind` |
| Use selection for find | `Cmd+E` | `useSelectionForFind` |

---

## Notifications

| Action | Shortcut | Binding key |
|--------|----------|-------------|
| Show notifications | `Cmd+I` | `showNotifications` |
| Jump to latest unread | `Cmd+Shift+U` | `jumpToUnread` |
| Flash focused panel | `Cmd+Shift+H` | `triggerFlash` |

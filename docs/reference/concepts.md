# Concepts

> **Source:** [cmux.com/docs/concepts](https://cmux.com/docs/concepts)

cmux organizes your terminals in a four-level hierarchy. Understanding these levels helps when using the socket API, CLI, and keyboard shortcuts.

---

## Hierarchy

```
Window
  └── Workspace (sidebar entry)
        └── Pane (split region)
              └── Surface (tab within pane)
                    └── Panel (terminal or browser content)
```

---

## Window

A macOS window. Open multiple windows with `Cmd+Shift+N`. Each window has its own sidebar with independent workspaces.

---

## Workspace

A sidebar entry. Each workspace contains one or more split panes. Workspaces are what you see listed in the left sidebar.

In the UI and keyboard shortcuts, workspaces are often called "tabs" since they behave like tabs in the sidebar. The socket API and environment variables use the term "workspace".

| Context | Term used |
|---------|-----------|
| Sidebar UI | Tab |
| Keyboard shortcuts | Workspace or tab |
| Socket API | `workspace` |
| Environment variable | `CMUX_WORKSPACE_ID` |

**Shortcuts:** `Cmd+N` (new), `Cmd+1`-`Cmd+9` (jump), `Cmd+Shift+W` (close), `Ctrl+Cmd+[` / `Ctrl+Cmd+]` (prev/next)

---

## Pane

A split region within a workspace. Created by splitting with `Cmd+D` (right) or `Cmd+Shift+D` (down). Navigate between panes with `Opt+Cmd` + arrow keys.

Each pane can hold multiple surfaces (tabs within the pane).

---

## Surface

A tab within a pane. Each pane has its own tab bar and can hold multiple surfaces. Created with `Cmd+T`, navigated with `Cmd+[` / `Cmd+]` or `Ctrl+1`-`Ctrl+9`.

Surfaces are the individual terminal or browser sessions you interact with. Each surface has its own `CMUX_SURFACE_ID` environment variable.

---

## Panel

The content inside a surface. Currently two types:

- **Terminal** — a Ghostty terminal session
- **Browser** — an embedded web view

Panel is mostly an internal concept. In the socket API and CLI, you interact with surfaces rather than panels directly.

---

## Visual Example

```
┌──────────────────────────────────────────────────────┐
│ ┌──────────┐ ┌─────────────────────────────────────┐ │
│ │ Sidebar  │ │ Workspace "dev"                     │ │
│ │          │ │                                     │ │
│ │          │ │ ┌───────────────┬─────────────────┐ │ │
│ │ > dev    │ │ │ Pane 1        │ Pane 2          │ │ │
│ │   server │ │ │ [S1] [S2]     │ [S1]            │ │ │
│ │   logs   │ │ │               │                 │ │ │
│ │          │ │ │  Terminal     │  Terminal       │ │ │
│ │          │ │ │               │                 │ │ │
│ │          │ │ └───────────────┴─────────────────┘ │ │
│ └──────────┘ └─────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

- The window contains a sidebar with three workspaces (dev, server, logs)
- Workspace "dev" is selected, showing two panes side by side
- Pane 1 has two surfaces ([S1] and [S2] in the tab bar), with S1 active
- Pane 2 has one surface
- Each surface contains a panel (a terminal in this case)

---

## Summary

| Level | What it is | Created by | Identified by |
|-------|-----------|------------|---------------|
| Window | macOS window | `Cmd+Shift+N` | — |
| Workspace | Sidebar entry | `Cmd+N` | `CMUX_WORKSPACE_ID` |
| Pane | Split region | `Cmd+D` / `Cmd+Shift+D` | Pane ID (socket API) |
| Surface | Tab within pane | `Cmd+T` | `CMUX_SURFACE_ID` |
| Panel | Terminal or browser | Automatic | Panel ID (internal) |

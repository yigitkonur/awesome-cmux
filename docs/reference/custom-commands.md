# Custom Commands

> **Source:** [cmux.com/docs/custom-commands](https://cmux.com/docs/custom-commands)

Define custom commands and workspace layouts by adding a `cmux.json` file to your project root or `~/.config/cmux/`. Commands appear in the command palette.

---

## File Locations

cmux looks for configuration in two places:

- **Per-project:** `./cmux.json` — lives in your project directory, takes precedence
- **Global:** `~/.config/cmux/cmux.json` — applies to all projects, fills in commands not defined locally

Local commands override global commands with the same name. Changes are picked up automatically — no restart needed.

---

## Schema

A `cmux.json` file contains a `commands` array. Each command is either a simple shell command or a full workspace definition:

```json
{
  "commands": [
    {
      "name": "Start Dev",
      "keywords": ["dev", "start"],
      "workspace": { "..." }
    },
    {
      "name": "Run Tests",
      "command": "npm test",
      "confirm": true
    }
  ]
}
```

---

## Simple Commands

A simple command runs a shell command in the currently focused terminal:

```json
{
  "commands": [
    {
      "name": "Run Tests",
      "keywords": ["test", "check"],
      "command": "npm test",
      "confirm": true
    }
  ]
}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Displayed in the command palette |
| `description` | No | Optional description |
| `keywords` | No | Extra search terms for the command palette |
| `command` | Yes | Shell command to run in the focused terminal |
| `confirm` | No | Show a confirmation dialog before running |

Simple commands run in the focused terminal's current working directory. If your command relies on project-relative paths, prefix it with `cd "$(git rev-parse --show-toplevel)" &&` to run from the repo root.

---

## Workspace Commands

A workspace command creates a new workspace with a custom layout of splits, terminals, and browser panes:

```json
{
  "commands": [
    {
      "name": "Dev Environment",
      "keywords": ["dev", "fullstack"],
      "restart": "confirm",
      "workspace": {
        "name": "Dev",
        "cwd": ".",
        "layout": {
          "direction": "horizontal",
          "split": 0.5,
          "children": [
            {
              "pane": {
                "surfaces": [
                  {
                    "type": "terminal",
                    "name": "Frontend",
                    "command": "npm run dev",
                    "focus": true
                  }
                ]
              }
            },
            {
              "pane": {
                "surfaces": [
                  {
                    "type": "terminal",
                    "name": "Backend",
                    "command": "cargo watch -x run",
                    "cwd": "./server",
                    "env": { "RUST_LOG": "debug" }
                  }
                ]
              }
            }
          ]
        }
      }
    }
  ]
}
```

### Workspace Fields

| Field | Description |
|-------|-------------|
| `name` | Workspace tab name (defaults to command name) |
| `cwd` | Working directory for the workspace |
| `color` | Workspace tab color |
| `layout` | Layout tree defining splits and panes |

### Restart Behavior

Controls what happens when a workspace with the same name already exists:

| Value | Behavior |
|-------|----------|
| `"ignore"` | Switch to the existing workspace (default) |
| `"recreate"` | Close and recreate without asking |
| `"confirm"` | Ask the user before recreating |

---

## Layout Tree

The layout tree defines how panes are arranged using recursive split nodes.

### Split Node

Divides space into two children:

| Field | Description |
|-------|-------------|
| `direction` | `"horizontal"` or `"vertical"` |
| `split` | Divider position from 0.1 to 0.9 (default 0.5) |
| `children` | Exactly two child nodes (split or pane) |

### Pane Node

A leaf node containing one or more surfaces (tabs within the pane).

---

## Surface Definition

Each surface in a pane can be a terminal or a browser:

| Field | Description |
|-------|-------------|
| `type` | `"terminal"` or `"browser"` |
| `name` | Custom tab title |
| `command` | Shell command to auto-run on creation (terminal only) |
| `cwd` | Working directory for this surface |
| `env` | Environment variables as key-value pairs |
| `url` | URL to open (browser only) |
| `focus` | Focus this surface after creation |

### Working Directory Resolution

| Value | Behavior |
|-------|----------|
| `.` or omitted | Workspace working directory |
| `./subdir` | Relative to workspace working directory |
| `~/path` | Expanded to home directory |
| Absolute path | Used as-is |

---

## Full Example

```json
{
  "commands": [
    {
      "name": "Web Dev",
      "description": "Docs site with live preview",
      "keywords": ["web", "docs", "next", "frontend"],
      "restart": "confirm",
      "workspace": {
        "name": "Web Dev",
        "cwd": "./web",
        "color": "#3b82f6",
        "layout": {
          "direction": "horizontal",
          "split": 0.5,
          "children": [
            {
              "pane": {
                "surfaces": [
                  {
                    "type": "terminal",
                    "name": "Next.js",
                    "command": "npm run dev",
                    "focus": true
                  }
                ]
              }
            },
            {
              "direction": "vertical",
              "split": 0.6,
              "children": [
                {
                  "pane": {
                    "surfaces": [
                      {
                        "type": "browser",
                        "name": "Preview",
                        "url": "http://localhost:3777"
                      }
                    ]
                  }
                },
                {
                  "pane": {
                    "surfaces": [
                      {
                        "type": "terminal",
                        "name": "Shell",
                        "env": { "NODE_ENV": "development" }
                      }
                    ]
                  }
                }
              ]
            }
          ]
        }
      }
    },
    {
      "name": "Debug Log",
      "description": "Tail the debug event log from the running dev app",
      "keywords": ["log", "debug", "tail", "events"],
      "restart": "ignore",
      "workspace": {
        "name": "Debug Log",
        "layout": {
          "direction": "horizontal",
          "split": 0.5,
          "children": [
            {
              "pane": {
                "surfaces": [
                  {
                    "type": "terminal",
                    "name": "Events",
                    "command": "tail -f /tmp/cmux-debug.log",
                    "focus": true
                  }
                ]
              }
            },
            {
              "pane": {
                "surfaces": [
                  {
                    "type": "terminal",
                    "name": "Shell"
                  }
                ]
              }
            }
          ]
        }
      }
    },
    {
      "name": "Setup",
      "description": "Initialize submodules and build dependencies",
      "keywords": ["setup", "init", "install"],
      "command": "./scripts/setup.sh",
      "confirm": true
    },
    {
      "name": "Reload",
      "description": "Build and launch the debug app tagged to the current branch",
      "keywords": ["reload", "build", "run", "launch"],
      "command": "./scripts/reload.sh --tag $(git branch --show-current)"
    },
    {
      "name": "Run Unit Tests",
      "keywords": ["test", "unit"],
      "command": "./scripts/test-unit.sh",
      "confirm": true
    }
  ]
}
```

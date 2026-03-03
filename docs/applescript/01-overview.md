# 01 — Overview

cmux automation is most reliable when treated as a 3-layer control stack:

1. **AppleScript** for orchestration and app-level flow
2. **cmux CLI** (via `do shell script`) for most command operations
3. **Raw socket v2 JSON** for method-level control when CLI parsing is limiting

## Key findings

- cmux does not rely on a rich AppleScript dictionary for command-level control.
- The CLI provides broad coverage for workspace/pane/surface/browser workflows.
- `capabilities --json` exposes a larger method surface than some CLI parser paths.

## Surface snapshot (from 2026-03-03 docs)

- Top-level CLI command tokens: **91**
- Usage command lines: **110**
- Runtime v2 methods: **172**
- Runtime method families: **12**

## Method families

- `app`, `auth`, `browser`, `debug`, `notification`, `pane`, `surface`, `system`, `tab`, `target`, `window`, `workspace`

## Rule of thumb

Use CLI first. If runtime has a method but CLI can’t address it cleanly, send JSON directly over `/tmp/cmux.sock`.

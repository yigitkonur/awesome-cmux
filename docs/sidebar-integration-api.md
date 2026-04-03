# cmux Sidebar Integration API

> The definitive reference for building agent plugins that update cmux's sidebar — status pills, progress bars, logs, notifications, and metadata. Derived from reverse-engineering 12 production integrations across Claude Code, Pi, OpenCode, Copilot CLI, and Amp.

## Table of Contents

- [Architecture](#architecture)
- [Environment Variables](#environment-variables)
- [Connection Methods](#connection-methods)
- [Protocol Reference](#protocol-reference)
  - [Status Pills](#1-status-pills)
  - [Progress Bar](#2-progress-bar)
  - [Sidebar Logs](#3-sidebar-logs)
  - [Notifications](#4-notifications)
  - [Metadata](#5-metadata)
  - [Agent PID & Crash Recovery](#6-agent-pid--crash-recovery)
  - [Workspace & Surface Control](#7-workspace--surface-control)
- [Progress Estimation Algorithms](#progress-estimation-algorithms)
- [Status Priority System](#status-priority-system)
- [State Management Patterns](#state-management-patterns)
- [Best Practices](#best-practices)
- [Complete Examples](#complete-examples)
- [Quick Reference Card](#quick-reference-card)

---

## Architecture

```
┌──────────────────────────────────────┐
│  Your Agent / CLI Tool               │
│  (emits hook events or lifecycle     │
│   callbacks)                         │
└──────────────┬───────────────────────┘
               │
       ┌───────▼───────┐
       │  Your Plugin   │  ← you build this
       │  (handler.ts   │
       │   or script)   │
       └───────┬────────┘
               │  V1 text commands  (preferred — fast)
               │  or CLI subprocess (simple — slower)
               │  or V2 JSON-RPC    (for notifications)
       ┌───────▼────────┐
       │  cmux socket    │  $CMUX_SOCKET_PATH
       │  server         │  (default: /tmp/cmux.sock)
       └───────┬────────┘
               │
       ┌───────▼────────┐
       │  Sidebar UI     │  GPU-accelerated, vertical
       │  ┌────────────┐ │
       │  │ Status Pill │ │  ← set_status
       │  │ Progress ██ │ │  ← set_progress
       │  │ Log entries │ │  ← log
       │  │ Git branch  │ │  ← report_git_branch
       │  │ Model name  │ │  ← report_meta
       │  └────────────┘ │
       └─────────────────┘
```

**Two protocols coexist** on the same Unix socket:

| Protocol | Format | Use For |
|---|---|---|
| **V1 text** | `command arg1 arg2 --flag=value\n` → response `OK\n` | Status pills, progress, logs, git, meta, agent PID |
| **V2 JSON-RPC** | `{"id":"1","method":"...","params":{...}}\n` → `{"id":"1","ok":true,"result":{...}}\n` | Notifications, browser control, workspace queries |

---

## Environment Variables

cmux sets these in every child shell:

| Variable | Example | Description |
|---|---|---|
| `CMUX_SOCKET_PATH` | `/tmp/cmux.sock` | Path to the Unix domain socket. **Primary detection signal.** |
| `CMUX_WORKSPACE_ID` | `ws:a1b2c3d4` | UUID of the workspace (tab) this terminal belongs to. |
| `CMUX_SURFACE_ID` | `surface:42` | UUID of the terminal pane (surface) within the workspace. |
| `TERM_PROGRAM` | `ghostty` | Always `ghostty` inside cmux (it wraps libghostty). |

**Detection pattern** (check before any cmux operation):

```typescript
// TypeScript
const isCmux = !!process.env.CMUX_SOCKET_PATH;

// Shell
[ -n "$CMUX_SOCKET_PATH" ] || exit 0
```

Some plugins also verify the socket is alive:

```bash
# Shell — verify socket exists and cmux responds
[ -S "${CMUX_SOCKET_PATH:-/tmp/cmux.sock}" ] && cmux ping >/dev/null 2>&1 || exit 0
```

---

## Connection Methods

### Method 1: Unix Socket (V1 Text Protocol) — Recommended

**~5-8ms latency.** One connection per command. Connect → write command → read response → close.

```typescript
import { createConnection } from "node:net";

function sendCommand(socketPath: string, command: string): void {
  try {
    const socket = createConnection({ path: socketPath }, () => {
      socket.write(command + "\n", () => socket.destroy());
    });
    socket.on("error", () => socket.destroy());
    socket.setTimeout(1000, () => socket.destroy());
  } catch {
    // Silently ignore — cmux may not be running
  }
}

// Usage:
sendCommand(process.env.CMUX_SOCKET_PATH!, 'set_status my_agent "Working" --icon=bolt.fill --color=#4C8DFF');
```

**With response** (for commands that return data):

```typescript
async function sendAndReceive(socketPath: string, command: string): Promise<string> {
  return new Promise((resolve) => {
    const chunks: Buffer[] = [];
    let settled = false;

    const finish = (result: string) => {
      if (settled) return;
      settled = true;
      socket?.removeAllListeners();
      socket?.destroy();
      resolve(result);
    };

    const timer = setTimeout(() => finish(""), 1000);
    const socket = createConnection({ path: socketPath }, () => {
      socket.write(command + "\n");
    });

    socket.on("data", (chunk) => chunks.push(chunk));
    socket.on("end", () => {
      clearTimeout(timer);
      finish(Buffer.concat(chunks).toString("utf-8").trimEnd());
    });
    socket.on("error", () => { clearTimeout(timer); finish(""); });
    socket.setTimeout(1000, () => { clearTimeout(timer); finish(""); });
  });
}
```

### Method 2: CLI Binary — Simple

**~30ms latency.** Spawns a subprocess for each command.

```bash
# Shell — fire and forget
cmux set-status my_agent "Working" --icon bolt.fill --color "#4C8DFF" 2>/dev/null || true

# Shell — with workspace scoping
cmux set-status my_agent "Working" --icon bolt.fill --color "#4C8DFF" --workspace "$CMUX_WORKSPACE_ID"
```

```typescript
// TypeScript — fire and forget
import { execFile } from "node:child_process";

function cmux(...args: string[]): void {
  execFile("cmux", args, { timeout: 2000 }, () => {});
}

cmux("set-status", "my_agent", "Working", "--icon", "bolt.fill", "--color", "#4C8DFF");
```

### Method 3: Persistent Socket — Lowest Latency

**~1-2ms latency.** Single long-lived connection. Used by sasha-computer/pi-cmux.

```typescript
import { createConnection, type Socket } from "node:net";

class PersistentCmuxClient {
  private socket: Socket | null = null;
  private pendingV1: Array<(response: string) => void> = [];

  constructor(private socketPath: string) {}

  connect(): Promise<boolean> {
    return new Promise((resolve) => {
      this.socket = createConnection({ path: this.socketPath }, () => resolve(true));
      this.socket.on("data", (chunk) => {
        // V1 responses are line-delimited; resolve oldest pending request
        const lines = chunk.toString().split("\n").filter(Boolean);
        for (const line of lines) {
          this.pendingV1.shift()?.(line);
        }
      });
      this.socket.on("error", () => resolve(false));
      this.socket.setTimeout(3000, () => resolve(false));
    });
  }

  /** Fire-and-forget V1 text command */
  v1(command: string): void {
    this.socket?.write(command + "\n");
  }

  close(): void {
    this.socket?.destroy();
    this.socket = null;
  }
}
```

### Method 4: V2 JSON-RPC — For Structured Operations

Used for notifications, browser control, workspace queries.

```typescript
function sendJsonRpc(socketPath: string, method: string, params: Record<string, unknown>): void {
  const payload = JSON.stringify({ id: `req-${Date.now()}`, method, params });
  sendCommand(socketPath, payload); // reuse the V1 socket transport
}

// Surface-targeted notification:
sendJsonRpc(socketPath, "notification.create_for_surface", {
  surface_id: process.env.CMUX_SURFACE_ID,
  title: "Claude Code",
  subtitle: "Done",
  body: "Fixed the auth bug",
});
```

### Choosing a Method

| Scenario | Recommended Method |
|---|---|
| Short-lived hook process (Claude Code, Copilot) | Socket V1 (fire-and-forget) |
| Long-lived plugin (Pi, OpenCode, Amp) | Persistent socket or CLI |
| Shell scripts | CLI binary |
| Notifications | V2 JSON-RPC or CLI `cmux notify` |
| Querying workspace state | V2 JSON-RPC |
| Quick prototype | CLI binary |

---

## Protocol Reference

### Argument Quoting

Values containing spaces, `"`, or `|` must be double-quoted. The quoting function:

```typescript
function q(value: string): string {
  if (value.includes(" ") || value.includes('"') || value.includes("|")) {
    return `"${value.replace(/\\/g, "\\\\").replace(/"/g, '\\"')}"`;
  }
  return value;
}
```

### Workspace Scoping

All V1 commands accept `--tab=<workspaceId>` to target a specific workspace tab. Without it, the command targets the caller's workspace (from `CMUX_WORKSPACE_ID`).

```
set_status my_agent "Working" --tab=ws:a1b2c3d4
```

CLI equivalent uses `--workspace`:

```bash
cmux set-status my_agent "Working" --workspace "$CMUX_WORKSPACE_ID"
```

---

### 1. Status Pills

The primary sidebar element. Each pill has a **key** (identifier), **value** (display text), **icon** (SF Symbol), and **color** (hex).

#### `set_status` — Create or Update a Pill

```
set_status <key> <value> [--icon=<sf_symbol>] [--color=<hex>] [--pid=<pid>] [--tab=<workspace_id>]
```

```bash
# CLI equivalent
cmux set-status <key> <value> [--icon <sf_symbol>] [--color <hex>]
```

| Parameter | Required | Description |
|---|---|---|
| `key` | Yes | Unique identifier for this pill. Convention: `agent_name` (e.g., `claude_code`, `pi_agent`, `amp`). |
| `value` | Yes | Display text (e.g., `"Working: Edit: config.ts"`, `"Thinking..."`). |
| `--icon` | No | [SF Symbol](https://developer.apple.com/sf-symbols/) name. See [Icon Reference](#sf-symbol-icon-reference). |
| `--color` | No | Hex color with `#` prefix for socket, without for CLI. (e.g., `#4C8DFF` / `4C8DFF`). |
| `--pid` | No | Associate a PID with this status entry (used with `set_agent_pid`). |
| `--tab` | No | Target workspace ID. Defaults to caller's workspace. |

**Examples:**

```
# Socket V1
set_status claude_code "Working: Edit: config.ts" --icon=hammer.fill --color=#4C8DFF --tab=ws:abc123

# CLI
cmux set-status claude_code "Working: Edit: config.ts" --icon hammer.fill --color 4C8DFF
```

#### `clear_status` — Remove a Pill

```
clear_status <key> [--tab=<workspace_id>]
```

```bash
cmux clear-status <key>
```

#### Multi-Key Strategy

You can register **multiple independent pills** under different keys. They appear as separate entries in the sidebar:

```
set_status pi_state "Working" --icon=bolt.fill --color=#F59E0B
set_status pi_model "opus-4-6" --icon=brain --color=#8B5CF6
set_status pi_tokens "45k/200k" --icon=number --color=#6B7280
```

| Strategy | Keys | Pro | Con |
|---|---|---|---|
| **Single key** | `my_agent` | Simple, one cleanup call | Can't show multiple data points |
| **Multi-key** (2-3) | `my_state`, `my_model` | Layered info at a glance | Must clean up each key |
| **Dashboard** (4-6) | `pi_state/model/thinking/tokens/cost/tool` | Rich monitoring | Sidebar clutter; complex cleanup |
| **Two slots** | `state`, `tool` | Lifecycle + current action independently | Coordinated clearing needed |

Always **clear all your keys on session end**:

```typescript
const MY_KEYS = ["my_state", "my_model", "my_tokens"];

function clearAll(socket: CmuxSocket, cmd: CmuxCommands): void {
  for (const key of MY_KEYS) {
    socket.fire(cmd.clearStatus(key));
  }
}
```

#### SF Symbol Icon Reference

Common icons used across the ecosystem:

| Category | Icon | SF Symbol Name | Used For |
|---|---|---|---|
| **Lifecycle** | ✓ | `checkmark.circle` | Ready, idle, done |
| | ✓✓ | `checkmark.seal` | Done (completed) |
| | ✓✓✓ | `checkmark.circle.fill` | Done (filled variant) |
| | ✗ | `xmark.circle` | Error |
| | ⏸ | `pause.circle` | Interrupted |
| | ○ | `circle` | Idle (not started) |
| | ○· | `circle.dotted` | Spawning |
| **Activity** | 🧠 | `brain` | Thinking, model name |
| | 🔨 | `hammer.fill` | Working (generic) |
| | 🔨 | `hammer` | Working (tool fallback) |
| | ⚡ | `bolt.fill` | Working (energetic) |
| | ↻ | `arrow.circlepath` | Working (spinner feel) |
| | ↻△ | `arrow.triangle.2.circlepath` | Compacting, refreshing |
| **Tools** | 👁 | `eye` | Reading |
| | ✏️ | `pencil` | Editing, writing |
| | > | `terminal` | Bash, running commands |
| | 🔍 | `magnifyingglass` | Grep, glob, searching |
| | 👥 | `person.2` | Subagent, task |
| | 👥 | `person.2.fill` | Team (filled) |
| | ✨ | `sparkles` | Thinking level, oracle |
| | 🌐 | `globe` | Web fetch, web search |
| | 🔧 | `wrench` | Generic tool |
| **Status** | ✋ | `hand.raised.fill` | Waiting for permission |
| | 🔒 | `lock` | Permission required |
| | ❓ | `help-circle` | Question pending |
| | 🔔 | `bell.fill` | Needs input |
| **Data** | # | `number` | Token count |
| | $ | `dollarsign.circle` | Cost |
| | 💬 | `text.bubble` | Session name |

#### Color Palette Reference

Colors used across the ecosystem (with the contexts they're typically used in):

| Hex | Color | Typical Use |
|---|---|---|
| `#22C55E` / `50fa7b` | Green | Ready, idle, done, cost |
| `#50C878` | Green (mint) | Ready, done (cmux-claude-pro) |
| `#4C8DFF` | Blue | Working, agent heartbeat |
| `#0ea5e9` | Sky blue | Thinking (Attamusc/copilot) |
| `#3B82F6` | Blue | Token count |
| `#F59E0B` / `ffd700` | Amber/Gold | Thinking, working, tools active |
| `#FFD700` | Gold | Thinking (cmux-claude-pro) |
| `#FF6B35` / `ffb86c` | Orange | Waiting for permission, interrupted |
| `#EF4444` / `ff5555` | Red | Error, permission required, token warning |
| `#9B59B6` | Purple | Compacting |
| `#8B5CF6` / `a78bfa` | Purple/Violet | Model name, spawning |
| `#A855F7` | Purple | Question pending |
| `#6B7280` / `adb5bd` | Gray | Idle (muted), inactive, off |
| `#ffffff` | White | Thinking (block/amp Dracula) |

---

### 2. Progress Bar

A horizontal progress indicator in the sidebar.

#### `set_progress` — Set Progress Value

```
set_progress <value> [--label=<text>] [--tab=<workspace_id>]
```

```bash
cmux set-progress <value> [--label <text>]
```

| Parameter | Required | Description |
|---|---|---|
| `value` | Yes | Float between `0.00` and `1.00`. |
| `--label` | No | Human-readable label (e.g., `"5 tools"`, `"3/8 tasks done"`, `"Complete"`). |

**Examples:**

```
# Socket V1
set_progress 0.33 --label="5 tools" --tab=ws:abc123

# CLI
cmux set-progress 0.33 --label "5 tools"

# 100% complete
set_progress 1.00 --label="Complete"
```

#### `clear_progress` — Remove Progress Bar

```
clear_progress [--tab=<workspace_id>]
```

```bash
cmux clear-progress
```

#### When to Show Progress

| Situation | Show Progress? | Algorithm |
|---|---|---|
| Short task (< 3 tools) | Optional | `n/(n+K)` |
| Multi-tool response | Yes | `n/(n+K)` with adaptive K |
| Task with known step count | Yes | `completed/total` |
| Long-running team/swarm | Yes | Detached watcher polling task files |
| Quick lookup / single answer | No | — |

---

### 3. Sidebar Logs

Scrollable log entries below the status pills.

#### `log` — Add a Log Entry

```
log [--level=<level>] [--source=<name>] [--tab=<workspace_id>] -- <message>
```

```bash
cmux log [--level <level>] [--source <name>] -- <message>
```

| Parameter | Required | Description |
|---|---|---|
| `--level` | No | One of: `info`, `progress`, `success`, `warning`, `error`. Default: `info`. |
| `--source` | No | Source label (e.g., `"claude"`, `"pi"`, `"amp"`, `"cru"`). |
| `message` | Yes | Free-form text. Appears after the `--` separator. |

**Examples:**

```
log --level=info --source=claude --tab=ws:abc123 -- "Read: src/handler.ts"
log --level=success --source=claude -- "Task completed"
log --level=warning --source=claude -- "FAIL Read: nonexistent.ts"
log --level=error --source=claude -- "API timeout after 30s"
log --level=progress --source=cru -- "3/8 tasks completed"
```

#### `clear_log` — Clear All Log Entries

```
clear_log [--tab=<workspace_id>]
```

```bash
cmux clear-log
```

#### Log Rate Limiting (Recommended)

Rapid tool execution can flood the sidebar. Implement a sliding window rate limiter:

```typescript
class LogRateLimiter {
  private timestamps: number[] = [];
  constructor(
    private maxPerWindow: number = 5,
    private windowMs: number = 1000,
  ) {}

  allow(): boolean {
    const now = Date.now();
    this.timestamps = this.timestamps.filter((t) => now - t < this.windowMs);
    if (this.timestamps.length >= this.maxPerWindow) return false;
    this.timestamps.push(now);
    return true;
  }
}

// Usage:
const limiter = new LogRateLimiter(5, 1000); // 5 logs/sec
if (limiter.allow()) {
  socket.fire(cmd.log("Edit: config.ts", { level: "info", source: "claude" }));
}
```

**File edit debounce** — suppress repeated edits to the same file within 500ms:

```typescript
const recentEdits = new Map<string, number>(); // path → timestamp

function shouldLogEdit(filePath: string): boolean {
  const now = Date.now();
  const last = recentEdits.get(filePath);
  if (last && now - last < 500) return false;
  recentEdits.set(filePath, now);
  // Keep map bounded:
  if (recentEdits.size > 10) {
    const oldest = [...recentEdits.entries()].sort((a, b) => a[1] - b[1])[0];
    recentEdits.delete(oldest[0]);
  }
  return true;
}
```

---

### 4. Notifications

Desktop notifications (macOS Notification Center) with optional workspace targeting.

#### Method A: CLI (simplest)

```bash
cmux notify --title "Claude Code" --subtitle "Done" --body "Fixed the auth bug"
```

#### Method B: V1 Text — Broadcast

```
notify "title|subtitle|body"
```

#### Method C: V1 Text — Targeted to Workspace + Surface

```
notify_target <workspace_id> <surface_id> "title|subtitle|body"
```

Targeted notifications light up the correct workspace tab even when the user is focused elsewhere.

#### Method D: V2 JSON-RPC — Structured

```json
{"id":"req-1","method":"notification.create","params":{"title":"Claude Code","subtitle":"Done","body":"Fixed the auth bug","workspace_id":"ws:abc123"}}
```

Surface-targeted:

```json
{"id":"req-1","method":"notification.create_for_surface","params":{"surface_id":"surface:42","title":"Claude Code","subtitle":"Done","body":"Fixed the auth bug"}}
```

#### Method E: OSC Escape Sequences

Terminal escape sequences that trigger cmux's notification daemon:

```bash
# OSC 777 (compatible with many terminals)
printf '\e]777;notify;Title;Body\a'

# OSC 99 (iTerm2-style, multi-part)
printf '\e]99;i=1;Title\a'
printf '\e]99;i=1;p=body;Body\a'
```

#### Clear Notifications

```
clear_notifications [--tab=<workspace_id>]
```

#### Focus-Aware Notifications

Avoid notifying when the user is already watching:

```typescript
function isFocused(socketPath: string): boolean {
  const result = cmuxSync("identify", "--json");
  const data = JSON.parse(result);
  return data.caller?.surface_ref === data.focused?.surface_ref;
}

// Only notify when user is NOT looking at this pane:
if (!isFocused(socketPath)) {
  socket.fire(cmd.notifyTarget(wid, sid, "Claude Code", "Done", summary));
}
```

#### Attention Cycle (Tab Unread Indicator)

Light up the workspace tab when the agent needs input, clear when the user responds:

```bash
# Light up tab:
cmux workspace-action --action mark-unread

# Clear on user interaction:
cmux workspace-action --action mark-read
```

---

### 5. Metadata

Additional information shown in the sidebar below status pills.

#### `report_git_branch` — Show Git Branch

```
report_git_branch <branch> [--status=dirty] [--tab=<workspace_id>]
```

Detects and displays the current git branch with an optional dirty indicator.

```typescript
import { execSync } from "node:child_process";

function detectGitInfo(cwd: string): { branch: string; dirty: boolean } {
  const branch = execSync("git rev-parse --abbrev-ref HEAD", { cwd }).toString().trim();
  const status = execSync("git status --porcelain", { cwd }).toString().trim();
  return { branch, dirty: status.length > 0 };
}

const git = detectGitInfo(process.cwd());
socket.fire(cmd.reportGitBranch(git.branch, git.dirty));
```

#### `report_meta` — Show Arbitrary Metadata

```
report_meta <key> <value> [--icon=<sf_symbol>] [--color=<hex>] [--tab=<workspace_id>]
```

```
report_meta model "claude-opus-4-6" --icon=brain --color=#8B5CF6
```

#### `clear_meta` — Remove Metadata

```
clear_meta <key> [--tab=<workspace_id>]
```

---

### 6. Agent PID & Crash Recovery

Register your agent's PID so cmux can auto-clean stale pills if the process crashes.

#### `set_agent_pid` — Register

```
set_agent_pid <key> <pid> [--tab=<workspace_id>]
```

```typescript
socket.fire(cmd.setAgentPid("claude_code", process.pid));
```

#### `clear_agent_pid` — Unregister

```
clear_agent_pid <key> [--tab=<workspace_id>]
```

**How crash recovery works:**

cmux's `TabManager` runs a timer every **30 seconds** that calls `kill(pid, 0)` (signal 0 = liveness check) on every registered PID. If `ESRCH` is returned (process doesn't exist), cmux automatically:

1. Removes the status pill for that key
2. Removes the PID registration
3. Clears stale notifications for that workspace

**Always register on session start, clear on session end:**

```typescript
// SessionStart:
socket.fire(cmd.setAgentPid("my_agent", process.pid));

// SessionEnd:
socket.fire(cmd.clearAgentPid("my_agent"));
socket.fire(cmd.clearStatus("my_agent"));
socket.fire(cmd.clearNotifications());
```

---

### 7. Workspace & Surface Control

For multi-agent orchestration — split panes, send keystrokes, read screens.

#### Split a Pane

```
# V1 text (via cmux-claude-pro)
new_pane --direction=<right|down>

# CLI
cmux new-split <right|down> [--surface <ref>]
```

Returns the new surface reference (e.g., `surface:43`).

#### Send Text / Keystrokes

```bash
cmux send --surface <ref> "echo hello"
cmux send-key --surface <ref> Return
```

#### Read Screen Content

```bash
cmux read-screen --surface <ref> --lines 50
```

#### Focus a Surface

```bash
# Via pane lookup:
cmux list-pane-surfaces --pane <ref>
cmux focus-pane --pane <ref>

# Direct:
cmux focus-surface --surface <ref>
```

#### Rename Workspace Tab

```bash
cmux rename-workspace --workspace "$CMUX_WORKSPACE_ID" "my-project"
```

Common pattern — rename to git repo name on session start:

```bash
PROJECT=$(basename "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null || basename "$PWD")
cmux rename-workspace --workspace "$CMUX_WORKSPACE_ID" "$PROJECT"
```

#### Trigger Flash (Visual Attention)

```json
{"id":"1","method":"surface.trigger_flash","params":{"surface_id":"surface:42"}}
```

---

## Progress Estimation Algorithms

### Algorithm 1: Simple Asymptotic — `n/(n+K)`

The most common approach. Simple, predictable, works for any agent.

```typescript
function calculateProgress(toolCount: number): number {
  const K = 10; // higher K = slower curve
  if (toolCount <= 0) return 0;
  return Math.min(0.95, toolCount / (toolCount + K));
}
```

| Tools | Progress |
|---|---|
| 1 | 0.09 |
| 3 | 0.23 |
| 5 | 0.33 |
| 10 | 0.50 |
| 20 | 0.67 |
| 50 | 0.83 |

**Used by:** tslateman/cmux-claude-code (K=10 fixed)

### Algorithm 2: Adaptive Asymptotic — `n/(n+K)` with Learning

K adapts based on previous turns' tool counts. If your last 3 turns used ~20 tools each, K increases to ~16 so the bar moves slower (more realistic).

```typescript
function calculateProgress(toolCount: number, turnToolCounts: number[]): number {
  let K = 10; // default

  if (turnToolCounts.length > 0) {
    const recent = turnToolCounts.slice(-3);
    const avg = recent.reduce((sum, n) => sum + n, 0) / recent.length;
    if (avg > 0) K = avg * 0.8;
  }

  if (toolCount <= 0) return 0;
  return Math.min(0.95, toolCount / (toolCount + K));
}
```

**Used by:** cmux-claude-pro

### Algorithm 3: Sigmoid with Time Decay

Combines tool count (primary signal) with elapsed time (secondary signal). More aggressive curve.

```typescript
function calculateProgress(toolCount: number, elapsedMs: number): number {
  const BASE = 0.08;
  const TOOL_WEIGHT = 0.72;
  const TOOL_STEEPNESS = 0.2;
  const TIME_WEIGHT = 0.15;
  const TIME_HALF_LIFE_MS = 90_000;

  const toolProgress = 1 - 1 / (1 + toolCount * TOOL_STEEPNESS);
  const timeProgress = 1 - Math.exp((-Math.LN2 * elapsedMs) / TIME_HALF_LIFE_MS);
  const raw = BASE + TOOL_WEIGHT * toolProgress + TIME_WEIGHT * timeProgress;

  return Math.min(0.95, Math.max(0.08, raw));
}
```

**Used by:** Attamusc/copilot-cmux

### Algorithm 4: Sigmoid + Todo Blending + High-Water Mark

The most sophisticated. Uses todos (if available) for deterministic progress, and never allows progress to decrease.

```typescript
class ProgressTracker {
  private highWaterMark = 0;

  calculate(toolCount: number, elapsedMs: number, todosCompleted?: number, todosTotal?: number): number {
    let raw: number;

    if (todosTotal && todosTotal > 0) {
      // When todos present: 50% tool + 50% todo
      const toolSigmoid = 1 - 1 / (1 + toolCount * 0.15);
      const todoRatio = todosCompleted! / todosTotal;
      raw = 0.1 + 0.6 * (0.5 * toolSigmoid + 0.5 * todoRatio);
    } else {
      // Fallback: tool + time
      const toolSigmoid = 1 - 1 / (1 + toolCount * 0.15);
      const timeFactor = 1 - Math.exp((-Math.LN2 * elapsedMs) / 120_000);
      raw = 0.1 + 0.6 * toolSigmoid + 0.1 * timeFactor;
    }

    const capped = Math.min(0.95, raw);
    this.highWaterMark = Math.max(this.highWaterMark, capped);
    return this.highWaterMark;
  }

  complete(): number {
    this.highWaterMark = 0;
    return 1.0;
  }
}
```

**Used by:** Attamusc/opencode-cmux

### Algorithm 5: Task File Polling (Detached Watcher)

For multi-agent teams. A detached process polls task files independently of the main agent.

```typescript
// Spawned as detached Bun process
const POLL_INTERVAL_MS = 2000;
const MAX_STALE_POLLS = 300; // 10 minutes

let stalePollCount = 0;
let lastCompleted = 0;

setInterval(() => {
  const tasks = readTaskFiles(`~/.claude/tasks/${teamName}/`);
  const completed = tasks.filter((t) => t.status === "completed").length;
  const total = tasks.length;

  if (completed === lastCompleted) {
    stalePollCount++;
    if (stalePollCount >= MAX_STALE_POLLS) process.exit(0);
  } else {
    stalePollCount = 0;
    lastCompleted = completed;
  }

  cmux("set-progress", String(completed / total), "--label", `${completed}/${total} tasks done`);

  if (completed === total) {
    cmux("set-progress", "1.0", "--label", "All tasks done");
    cmux("notify", "--title", "Team", "--body", "All tasks complete");
    process.exit(0);
  }
}, POLL_INTERVAL_MS);
```

**Used by:** eduwass/cru

### Choosing an Algorithm

| Scenario | Recommended | Why |
|---|---|---|
| Simple plugin, few hooks | Algorithm 1 (`n/(n+10)`) | Dead simple, no state |
| Full-featured Claude Code plugin | Algorithm 2 (adaptive K) | Learns from your usage |
| Agent with elapsed time awareness | Algorithm 3 (sigmoid + time) | Better UX for long tasks |
| Agent with todo/task tracking | Algorithm 4 (todo blend) | Deterministic when possible |
| Multi-agent team orchestration | Algorithm 5 (file polling) | Independent of any agent |

---

## Status Priority System

When multiple events fire simultaneously (e.g., a tool starts while a permission is pending), use priority-based resolution to prevent lower-importance states from overwriting higher ones:

```typescript
type StatusPhase = "ready" | "thinking" | "working" | "waiting" | "done" | "error" | "compacting";

const PRIORITY: Record<StatusPhase, number> = {
  error:      100,
  waiting:     90,
  compacting:  70,
  working:     50,
  thinking:    40,
  done:        30,
  ready:       10,
};

function resolveStatus(current: StatusPhase, next: StatusPhase): StatusPhase {
  // Special case: working → working always passes (tool label changes)
  if (current === "working" && next === "working") return next;
  return PRIORITY[next] >= PRIORITY[current] ? next : current;
}
```

**Rule:** `error` > `waiting` > `compacting` > `working` > `thinking` > `done` > `ready`.

This prevents scenarios like:
- A tool firing during a permission request overwriting "Waiting" with "Working"
- A "Done" state overwriting an "Error" state

---

## State Management Patterns

### Pattern A: Atomic File State (for short-lived hook processes)

Each hook invocation is a separate process. State persists in a JSON file with mkdir-based locking.

```
/tmp/my-agent/
├── <session-id>.json      # SessionState
├── <session-id>.lock/     # Advisory lock (mkdir = atomic)
└── <session-id>.json.tmp  # Write target (rename = atomic)
```

```typescript
class StateManager {
  private stateFile: string;
  private lockDir: string;

  withState<T>(fn: (state: SessionState) => T): T {
    this.lock();
    try {
      const state = this.read();
      const result = fn(state);
      this.write(state);
      return result;
    } finally {
      this.unlock();
    }
  }

  private lock(): void {
    const deadline = Date.now() + 100;
    while (true) {
      try { mkdirSync(this.lockDir); return; } catch {}
      if (Date.now() >= deadline) { this.forceUnlock(); return; }
      // Spin wait 1ms
    }
  }

  private write(state: SessionState): void {
    const tmp = this.stateFile + ".tmp." + process.pid;
    writeFileSync(tmp, JSON.stringify(state));
    renameSync(tmp, this.stateFile); // POSIX-atomic
  }
}
```

**Used by:** cmux-claude-pro, Attamusc/copilot-cmux

### Pattern B: In-Memory State (for long-lived plugins)

Plugin stays running; state lives in closure variables.

```typescript
let currentStatus: StatusPhase = "ready";
let toolCount = 0;
let activeSubagents = 0;

agent.on("tool.start", () => { toolCount++; currentStatus = "working"; render(); });
agent.on("tool.end",   () => { render(); });
agent.on("agent.end",  () => { currentStatus = "done"; toolCount = 0; render(); });
```

**Used by:** HazAT/pi-config, sasha/pi-cmux, 0xCaso/opencode-cmux, Attamusc/opencode-cmux, block/cmux-amp, joelhooks/pi-cmux

### Pattern C: Temp File Counter (for shell scripts)

Simplest possible state — a single number in a temp file per surface.

```bash
COUNTER_FILE="/tmp/my-progress-$(echo $CMUX_SURFACE_ID)"
COUNT=$(cat "$COUNTER_FILE" 2>/dev/null || echo 0)
COUNT=$((COUNT + 1))
echo "$COUNT" > "$COUNTER_FILE"
```

**Used by:** tslateman/cmux-claude-code

---

## Best Practices

### 1. Never Block the Agent

Your plugin is cosmetic. It must **never** crash the agent or delay its work.

```typescript
// Every socket/CLI call must be wrapped:
try {
  socket.fire(cmd.setStatus("my_agent", "Working"));
} catch {
  // Swallow silently
}

// Process must always exit 0:
process.on("uncaughtException", () => process.exit(0));
process.on("unhandledRejection", () => process.exit(0));
```

For short-lived hook processes, add a **flush grace period** before exiting:

```typescript
await new Promise((resolve) => setTimeout(resolve, 50));
process.exit(0);
```

### 2. Clean Up on Exit

Stale pills confuse users. Always clean up:

```typescript
// Session end:
socket.fireAll([
  cmd.clearStatus("my_agent"),
  cmd.clearProgress(),
  cmd.clearLog(),
  cmd.clearAgentPid("my_agent"),
  cmd.clearNotifications(),
]);
```

For CLI-based plugins, also handle signals:

```typescript
const cleanup = () => {
  cmux("clear-status", "my_agent");
  cmux("clear-progress");
  cmux("clear-log");
};
process.on("SIGINT", cleanup);
process.on("SIGTERM", cleanup);
process.on("exit", cleanup);
```

### 3. Silent No-Op Outside cmux

Your plugin must be invisible when cmux is not running:

```typescript
export default function myPlugin(agent: AgentAPI) {
  if (!process.env.CMUX_SOCKET_PATH) return; // complete no-op
  // ... rest of plugin
}
```

### 4. Cap Progress at 0.95

Never show 100% until the agent explicitly finishes. Users learn to trust that the bar reflects actual completion.

```typescript
const progress = Math.min(0.95, calculateProgress(toolCount));
// Only set 1.0 on the actual Stop/Done event:
socket.fire(cmd.setProgress(1.0, "Complete"));
```

### 5. Render Throttle for Long-Lived Plugins

If your plugin receives many rapid events, coalesce renders:

```typescript
class RenderThrottle {
  private lastRenderTime = 0;
  private pendingTimer: ReturnType<typeof setTimeout> | null = null;
  private readonly THROTTLE_MS = 200;

  schedule(renderFn: () => void): void {
    const elapsed = Date.now() - this.lastRenderTime;
    if (elapsed >= this.THROTTLE_MS) {
      this.lastRenderTime = Date.now();
      renderFn();
    } else if (!this.pendingTimer) {
      this.pendingTimer = setTimeout(() => {
        this.pendingTimer = null;
        this.lastRenderTime = Date.now();
        renderFn();
      }, this.THROTTLE_MS - elapsed);
    }
    // If timer already pending, latest state will be rendered when it fires
  }
}
```

### 6. Avoid Conflicting with Built-in Integration

cmux ships with its own Claude Code integration under the `claude_code` status key. If you're replacing it:

```typescript
// Disable built-in via UserDefault:
// defaults write ai.manaflow.cmux claudeCodeHooksDisabled -bool YES

// Or actively suppress it:
function clearBuiltinStatus() {
  socket.fire(cmd.clearStatus("claude_code"));
}
```

### 7. Headless Subagent Guard

Skip all cmux operations for headless subagents:

```typescript
agent.on("session_start", (event, ctx) => {
  if (!ctx.hasUI) return; // headless subagent — no sidebar
  // ... proceed with UI updates
});
```

### 8. Stale State Cleanup

On session start, clean up state files from crashed sessions:

```typescript
function cleanStaleFiles(dir: string, maxAgeMs: number = 3600_000): void {
  const now = Date.now();
  for (const entry of readdirSync(dir)) {
    if (!entry.endsWith(".json")) continue;
    const stat = statSync(join(dir, entry));
    if (now - stat.mtimeMs > maxAgeMs) unlinkSync(join(dir, entry));
  }
}
```

---

## Complete Examples

### Example 1: Minimal Shell Plugin (6 hooks)

The simplest possible cmux integration for Claude Code.

**`hooks.json`** (register in `~/.claude/settings.json` or as a Claude Code plugin):

```json
{
  "hooks": {
    "SessionStart": [{"hooks": [{"type": "command", "command": "bash /path/to/hooks/session-start.sh", "timeout": 5}]}],
    "UserPromptSubmit": [{"hooks": [{"type": "command", "command": "bash /path/to/hooks/thinking.sh", "timeout": 3}]}],
    "PostToolUse": [{"hooks": [{"type": "command", "command": "bash /path/to/hooks/tool.sh", "timeout": 3}]}],
    "Stop": [{"hooks": [{"type": "command", "command": "bash /path/to/hooks/done.sh", "timeout": 5}]}],
    "Notification": [{"hooks": [{"type": "command", "command": "bash /path/to/hooks/notification.sh", "timeout": 5}]}],
    "SessionEnd": [{"hooks": [{"type": "command", "command": "bash /path/to/hooks/cleanup.sh", "timeout": 3}]}]
  }
}
```

**`common.sh`:**

```bash
#!/bin/bash
[ -n "$CMUX_SOCKET_PATH" ] || exit 0
command -v cmux &>/dev/null || exit 0
```

**`session-start.sh`:**

```bash
#!/bin/bash
source "$(dirname "$0")/common.sh"
cmux clear-status my_agent 2>/dev/null
cmux clear-progress 2>/dev/null
cmux set-status my_agent "Ready" --icon checkmark.circle --color "50C878" 2>/dev/null
rm -f "/tmp/my-progress-${CMUX_SURFACE_ID:-default}"
```

**`thinking.sh`:**

```bash
#!/bin/bash
source "$(dirname "$0")/common.sh"
cmux set-status my_agent "Thinking..." --icon brain --color "FFD700" 2>/dev/null
cmux clear-progress 2>/dev/null
echo 0 > "/tmp/my-progress-${CMUX_SURFACE_ID:-default}"
```

**`tool.sh`:**

```bash
#!/bin/bash
source "$(dirname "$0")/common.sh"
INPUT=$(cat 2>/dev/null)
TOOL=$(echo "$INPUT" | jq -r '.tool_name // empty' 2>/dev/null)
[ -z "$TOOL" ] && exit 0

cmux set-status my_agent "Working: $TOOL" --icon hammer.fill --color "4C8DFF" 2>/dev/null

# Progress: n/(n+10)
F="/tmp/my-progress-${CMUX_SURFACE_ID:-default}"
N=$(cat "$F" 2>/dev/null || echo 0)
N=$((N + 1))
echo "$N" > "$F"
P=$(awk "BEGIN { p=$N/($N+10); if(p>0.95) p=0.95; printf \"%.3f\", p }")
cmux set-progress "$P" --label "$N tools" 2>/dev/null
```

**`done.sh`:**

```bash
#!/bin/bash
source "$(dirname "$0")/common.sh"
cmux set-status my_agent "Done" --icon checkmark.seal --color "50C878" 2>/dev/null
cmux set-progress 1.0 --label "Complete" 2>/dev/null
cmux notify --title "Agent" --body "Done — check your terminal" 2>/dev/null
```

**`cleanup.sh`:**

```bash
#!/bin/bash
source "$(dirname "$0")/common.sh"
cmux clear-status my_agent 2>/dev/null
cmux clear-progress 2>/dev/null
rm -f "/tmp/my-progress-${CMUX_SURFACE_ID:-default}"
```

---

### Example 2: Full TypeScript Plugin (16 hooks, socket transport)

A production-grade template with adaptive progress, priority status, sidebar logs, and crash recovery.

**`src/cmux-client.ts`:**

```typescript
import { createConnection, type Socket } from "node:net";

export class CmuxClient {
  constructor(private socketPath: string, private workspaceId: string) {}

  /** Fire-and-forget — speed-critical path */
  fire(command: string): void {
    try {
      const s = createConnection({ path: this.socketPath }, () => {
        s.write(command + "\n", () => s.destroy());
      });
      s.on("error", () => s.destroy());
      s.setTimeout(1000, () => s.destroy());
    } catch {}
  }

  fireAll(commands: string[]): void {
    for (const c of commands) this.fire(c);
  }

  private t(): string { return ` --tab=${this.workspaceId}`; }
  private q(v: string): string {
    return v.includes(" ") || v.includes('"') || v.includes("|")
      ? `"${v.replace(/\\/g, "\\\\").replace(/"/g, '\\"')}"`
      : v;
  }

  setStatus(key: string, value: string, icon: string, color: string, pid?: number): string {
    let c = `set_status ${this.q(key)} ${this.q(value)} --icon=${this.q(icon)} --color=${color}`;
    if (pid) c += ` --pid=${pid}`;
    return c + this.t();
  }

  clearStatus(key: string): string { return `clear_status ${this.q(key)}${this.t()}`; }

  setProgress(value: number, label?: string): string {
    let c = `set_progress ${value.toFixed(2)}`;
    if (label) c += ` --label=${this.q(label)}`;
    return c + this.t();
  }

  clearProgress(): string { return `clear_progress${this.t()}`; }

  log(message: string, level: string = "info"): string {
    return `log --level=${level} --source=my_agent${this.t()} -- ${this.q(message)}`;
  }

  clearLog(): string { return `clear_log${this.t()}`; }

  notifyTarget(title: string, subtitle: string, body: string, surfaceId: string): string {
    return `notify_target ${this.workspaceId} ${surfaceId} ${this.q([title, subtitle, body].join("|"))}`;
  }

  setAgentPid(key: string, pid: number): string {
    return `set_agent_pid ${this.q(key)} ${pid}${this.t()}`;
  }

  clearAgentPid(key: string): string { return `clear_agent_pid ${this.q(key)}${this.t()}`; }
  clearNotifications(): string { return `clear_notifications${this.t()}`; }

  reportGitBranch(branch: string, dirty: boolean): string {
    let c = `report_git_branch ${this.q(branch)}`;
    if (dirty) c += " --status=dirty";
    return c + this.t();
  }

  reportMeta(key: string, value: string, icon: string, color: string): string {
    return `report_meta ${this.q(key)} ${this.q(value)} --icon=${this.q(icon)} --color=${color}${this.t()}`;
  }
}
```

**`src/handler.ts`:**

```typescript
import { CmuxClient } from "./cmux-client.js";

// --- Types ---
type StatusPhase = "ready" | "thinking" | "working" | "waiting" | "done" | "error" | "compacting";

interface SessionState {
  currentStatus: StatusPhase;
  toolUseCount: number;
  turnToolCounts: number[];  // last 5
  activeSubagents: number;
}

// --- Priority system ---
const PRIORITY: Record<StatusPhase, number> = {
  error: 100, waiting: 90, compacting: 70, working: 50,
  thinking: 40, done: 30, ready: 10,
};

const DISPLAY: Record<StatusPhase, { icon: string; color: string }> = {
  ready:      { icon: "checkmark.circle",           color: "#50C878" },
  thinking:   { icon: "brain",                      color: "#FFD700" },
  working:    { icon: "hammer.fill",                color: "#4C8DFF" },
  waiting:    { icon: "hand.raised.fill",           color: "#FF6B35" },
  done:       { icon: "checkmark.seal",             color: "#50C878" },
  error:      { icon: "xmark.circle",               color: "#FF4444" },
  compacting: { icon: "arrow.triangle.2.circlepath", color: "#9B59B6" },
};

// --- Adaptive progress ---
function calculateProgress(toolCount: number, turnToolCounts: number[]): number {
  let K = 10;
  if (turnToolCounts.length > 0) {
    const recent = turnToolCounts.slice(-3);
    const avg = recent.reduce((a, b) => a + b, 0) / recent.length;
    if (avg > 0) K = avg * 0.8;
  }
  if (toolCount <= 0) return 0;
  return Math.min(0.95, toolCount / (toolCount + K));
}

// --- Main handler ---
async function main(): Promise<void> {
  const socketPath = process.env.CMUX_SOCKET_PATH;
  const workspaceId = process.env.CMUX_WORKSPACE_ID;
  const surfaceId = process.env.CMUX_SURFACE_ID;
  if (!socketPath || !workspaceId) process.exit(0);

  const raw = await readStdin(500);
  if (!raw) process.exit(0);

  const event = JSON.parse(raw);
  const eventName = event.hook_event_name;

  const cmux = new CmuxClient(socketPath, workspaceId);
  const state = loadState(event.session_id); // your state manager

  switch (eventName) {
    case "SessionStart":
      state.currentStatus = "ready";
      state.toolUseCount = 0;
      cmux.fire(cmux.setAgentPid("my_agent", process.pid));
      cmux.fire(cmux.setStatus("my_agent", "Ready", DISPLAY.ready.icon, DISPLAY.ready.color));
      break;

    case "UserPromptSubmit":
      if (state.toolUseCount > 0) {
        state.turnToolCounts.push(state.toolUseCount);
        if (state.turnToolCounts.length > 5) state.turnToolCounts = state.turnToolCounts.slice(-5);
      }
      state.toolUseCount = 0;
      state.currentStatus = "thinking";
      cmux.fireAll([
        cmux.clearNotifications(),
        cmux.setStatus("my_agent", "Thinking...", DISPLAY.thinking.icon, DISPLAY.thinking.color),
        cmux.clearProgress(),
      ]);
      break;

    case "PreToolUse": {
      state.toolUseCount++;
      const resolved = resolveStatus(state.currentStatus, "working");
      state.currentStatus = resolved;
      const toolLabel = formatToolLabel(event.tool_name, event.tool_input);
      cmux.fire(cmux.setStatus("my_agent", `Working: ${toolLabel}`, DISPLAY.working.icon, DISPLAY.working.color));
      const progress = calculateProgress(state.toolUseCount, state.turnToolCounts);
      cmux.fire(cmux.setProgress(progress, `${state.toolUseCount} tools`));
      break;
    }

    case "PostToolUse":
      cmux.fire(cmux.log(formatToolLog(event.tool_name, event.tool_input), "info"));
      break;

    case "PostToolUseFailure":
      cmux.fire(cmux.log(`FAIL ${event.tool_name}: ${(event.error || "").slice(0, 60)}`, "warning"));
      break;

    case "Stop":
      state.currentStatus = "done";
      cmux.fireAll([
        cmux.setStatus("my_agent", "Done", DISPLAY.done.icon, DISPLAY.done.color),
        cmux.setProgress(1.0, "Complete"),
        cmux.notifyTarget("Agent", "Done", (event.last_assistant_message || "").slice(0, 100), surfaceId!),
      ]);
      break;

    case "StopFailure":
      state.currentStatus = "error";
      cmux.fire(cmux.setStatus("my_agent", "Error", DISPLAY.error.icon, DISPLAY.error.color));
      break;

    case "SessionEnd":
      cmux.fireAll([
        cmux.clearStatus("my_agent"),
        cmux.clearProgress(),
        cmux.clearLog(),
        cmux.clearAgentPid("my_agent"),
        cmux.clearNotifications(),
      ]);
      deleteState(event.session_id);
      break;
  }

  saveState(event.session_id, state);
  await new Promise((r) => setTimeout(r, 50)); // flush grace
  process.exit(0);
}

function resolveStatus(current: StatusPhase, next: StatusPhase): StatusPhase {
  if (current === "working" && next === "working") return next;
  return PRIORITY[next] >= PRIORITY[current] ? next : current;
}

// helpers omitted for brevity: readStdin, formatToolLabel, formatToolLog, loadState, saveState, deleteState

process.on("uncaughtException", () => process.exit(0));
process.on("unhandledRejection", () => process.exit(0));
main().catch(() => process.exit(0));
```

---

## Quick Reference Card

```
# ── STATUS PILLS ──────────────────────────────────────────
set_status <key> <value> [--icon=<sf>] [--color=<hex>] [--tab=<wid>]
clear_status <key> [--tab=<wid>]

# ── PROGRESS BAR ──────────────────────────────────────────
set_progress <0.00-1.00> [--label=<text>] [--tab=<wid>]
clear_progress [--tab=<wid>]

# ── SIDEBAR LOGS ──────────────────────────────────────────
log [--level=info|success|warning|error|progress] [--source=<name>] [--tab=<wid>] -- <message>
clear_log [--tab=<wid>]

# ── NOTIFICATIONS ─────────────────────────────────────────
notify "title|subtitle|body"
notify_target <wid> <sid> "title|subtitle|body"
clear_notifications [--tab=<wid>]

# ── METADATA ──────────────────────────────────────────────
report_git_branch <branch> [--status=dirty] [--tab=<wid>]
report_meta <key> <value> [--icon=<sf>] [--color=<hex>] [--tab=<wid>]
clear_meta <key> [--tab=<wid>]

# ── AGENT PID ─────────────────────────────────────────────
set_agent_pid <key> <pid> [--tab=<wid>]
clear_agent_pid <key> [--tab=<wid>]

# ── WORKSPACE / SURFACE ──────────────────────────────────
rename_tab <title> --surface=<sid>
new_pane --direction=<right|down>
send --surface=<ref> <text>
send_key --surface=<ref> <key>
```

---

## Appendix: V2 JSON-RPC Methods for Notifications

```json
// Create notification (broadcast):
{"id":"1","method":"notification.create","params":{"title":"T","subtitle":"S","body":"B","workspace_id":"ws:..."}}

// Create notification (surface-targeted):
{"id":"1","method":"notification.create_for_surface","params":{"surface_id":"surface:42","title":"T","subtitle":"S","body":"B"}}

// List notifications:
{"id":"2","method":"notification.list","params":{}}

// Clear notifications:
{"id":"3","method":"notification.clear","params":{"workspace_id":"ws:..."}}

// Flash a surface (visual attention):
{"id":"4","method":"surface.trigger_flash","params":{"surface_id":"surface:42"}}
```

---

*Built from analyzing 12 production integrations: cmux built-in, cmux-claude-pro, HazAT/pi-config, sasha-computer/pi-cmux, tslateman/cmux-claude-code, 0xCaso/opencode-cmux, Attamusc/copilot-cmux, Attamusc/opencode-cmux, block/cmux-amp, hopchouinard/cmux-plugin, joelhooks/pi-cmux, and eduwass/cru.*

# Awesome cmux [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of resources for **[cmux](https://github.com/manaflow-ai/cmux)** — the Ghostty-based macOS terminal built for coding agents.
> [!IMPORTANT]
> This list is for **`manaflow-ai/cmux`** only. Not the Go connection multiplexer by soheilhy.

## Contents

- [Getting Started](#getting-started)
- [Ghostty Config for cmux](#ghostty-config-for-cmux)
- [Automation & Scripting](#automation--scripting)
- [Community Extensions](#community-extensions)
- [Community](#community)
- [Articles & Coverage](#articles--coverage)
- [Related Projects](#related-projects)

---

## Getting Started

**Install**

```sh
brew install --cask cmux          # stable
brew install --cask cmux-nightly  # nightly
```

Or grab the DMG directly: [stable](https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg) | [nightly](https://github.com/manaflow-ai/cmux/releases/download/nightly/cmux-nightly-macos.dmg)

**Official Resources**

| Resource | Link |
|----------|------|
| Website | [cmux.dev](https://www.cmux.dev/) |
| Source Code | [github.com/manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) |
| Docs | [Getting Started](https://www.cmux.dev/docs/getting-started) · [Concepts](https://www.cmux.dev/docs/concepts) · [Configuration](https://www.cmux.dev/docs/configuration) · [Keyboard Shortcuts](https://www.cmux.dev/docs/keyboard-shortcuts) |
| API | [API Reference](https://www.cmux.dev/docs/api) · [Browser Automation](https://www.cmux.dev/docs/browser-automation) · [Notifications](https://www.cmux.dev/docs/notifications) |
| Blog | [Introducing cmux](https://www.cmux.dev/blog/introducing-cmux) · [Show HN Launch](https://www.cmux.dev/blog/show-hn-launch) · [The Zen of cmux](https://www.cmux.dev/blog/zen-of-cmux) |
| Changelog | [changelog](https://www.cmux.dev/docs/changelog) |

---

## Ghostty Config for cmux

cmux reads your `~/.config/ghostty/config` automatically — themes, fonts, colors all carry over. Below is a production-tested config optimized for cmux's multi-agent workflow.

**Why this matters:** cmux inherits *everything* from Ghostty, but not every default works well with vertical tabs, split panes, and agent output. This config tunes the settings that matter most.

<details>
<summary><strong>Full config (click to expand)</strong></summary>

```ini
# ============================================================================
#  ghostty config — cmux-optimized, productivity-first
# ============================================================================

# --- theme & colors --------------------------------------------------------
# catppuccin mocha: high-contrast dark palette, easy on the eyes.
# background deepened slightly for better contrast with cmux sidebar.
theme = Catppuccin Mocha
background = 1e1e2e
foreground = cdd6f4

# --- cursor ----------------------------------------------------------------
# solid block, no blink — less distraction, easier to spot across splits.
cursor-color = f5e0dc
cursor-text = 1e1e2e
cursor-style = block
cursor-style-blink = false
cursor-opacity = 0.9

# --- selection -------------------------------------------------------------
selection-background = 585b70
selection-foreground = cdd6f4

# --- fonts -----------------------------------------------------------------
# jetbrainsmono nerd font at 16pt for retina readability.
# thickened glyphs stay legible at lower opacity with blur.
font-family = JetBrainsMono Nerd Font
font-family-bold = JetBrainsMono Nerd Font
font-family-italic = JetBrainsMono Nerd Font
font-family-bold-italic = JetBrainsMono Nerd Font
font-size = 16
font-thicken = true
font-thicken-strength = 64

# coding ligatures (=> != === etc.)
font-feature = calt
font-feature = liga

# pixel-perfect box-drawing for tui apps and borders
font-codepoint-map = U+2500-U+259F=Menlo

# --- transparency & blur ---------------------------------------------------
# subtle frosted glass. 0.95 keeps text sharp while adding depth.
background-opacity = 0.95
background-blur = macos-glass-regular

# --- window & padding ------------------------------------------------------
# generous padding so text doesn't crowd cmux's vertical tab sidebar.
window-padding-x = 16
window-padding-y = 12
window-padding-balance = true
window-padding-color = extend

# comfortable default size for 2 side-by-side splits
window-height = 35
window-width = 120

# transparent titlebar blends with cmux's own chrome
macos-titlebar-style = transparent
window-decoration = auto
window-theme = dark
window-colorspace = display-p3
window-save-state = always

# IMPORTANT: hide ghostty's tab bar — cmux has its own vertical tabs
window-show-tab-bar = never

# --- split panes -----------------------------------------------------------
# dimmed unfocused panes make it obvious which agent you're talking to.
unfocused-split-opacity = 0.65
unfocused-split-fill = 181825
split-divider-color = 45475a

# new splits inherit working directory
split-inherit-working-directory = true
tab-inherit-working-directory = true
window-inherit-working-directory = true
window-inherit-font-size = true

# --- scrollback ------------------------------------------------------------
# 50k lines — agent output gets verbose (claude code tool traces etc.)
scrollback-limit = 50000

# --- clipboard -------------------------------------------------------------
clipboard-read = allow
clipboard-write = allow
clipboard-trim-trailing-spaces = true
clipboard-paste-protection = true
clipboard-paste-bracketed-safe = true
copy-on-select = clipboard

# --- shell integration -----------------------------------------------------
shell-integration = zsh
shell-integration-features = no-cursor
term = xterm-256color
confirm-close-surface = false

# --- macos specific --------------------------------------------------------
# option-as-alt enables word nav keybindings below.
# caveat: breaks option+key chars on non-us keyboards (e.g. @ on turkish).
macos-option-as-alt = true
macos-non-native-fullscreen = true
focus-follows-mouse = false

# --- resize overlay --------------------------------------------------------
resize-overlay = after-first
resize-overlay-position = bottom-right
resize-overlay-duration = 500ms

# --- mouse & interaction ---------------------------------------------------
cursor-click-to-move = true
scroll-to-bottom = keystroke, no-output

# --- keybindings -----------------------------------------------------------

# word navigation (option+arrow)
keybind = alt+left=esc:b
keybind = alt+right=esc:f

# line navigation (cmd+arrow)
keybind = cmd+left=text:\x01
keybind = cmd+right=text:\x05

# delete word backward
keybind = alt+backspace=text:\x17

# clear terminal
keybind = cmd+k=clear_screen

# splits: create
keybind = cmd+d=new_split:right
keybind = cmd+shift+d=new_split:down

# splits: navigate
keybind = cmd+alt+left=goto_split:left
keybind = cmd+alt+right=goto_split:right
keybind = cmd+alt+up=goto_split:top
keybind = cmd+alt+down=goto_split:bottom

# splits: resize
keybind = cmd+ctrl+left=resize_split:left,20
keybind = cmd+ctrl+right=resize_split:right,20
keybind = cmd+ctrl+up=resize_split:up,10
keybind = cmd+ctrl+down=resize_split:down,10

# splits: layout
keybind = cmd+shift+e=equalize_splits
keybind = cmd+shift+z=toggle_split_zoom

# font size (screen sharing / pairing)
keybind = cmd+equal=increase_font_size:2
keybind = cmd+minus=decrease_font_size:2
keybind = cmd+0=reset_font_size

# config & window
keybind = cmd+shift+comma=reload_config
keybind = cmd+enter=toggle_fullscreen

# --- palette (catppuccin mocha) --------------------------------------------
palette = 0=#45475a
palette = 8=#585b70
palette = 1=#f38ba8
palette = 9=#f38ba8
palette = 2=#a6e3a1
palette = 10=#a6e3a1
palette = 3=#f9e2af
palette = 11=#f9e2af
palette = 4=#89b4fa
palette = 12=#89b4fa
palette = 5=#f5c2e7
palette = 13=#f5c2e7
palette = 6=#94e2d5
palette = 14=#94e2d5
palette = 7=#bac2de
palette = 15=#a6adc8
```

</details>

**Key decisions explained:**

| Setting | Why |
|---------|-----|
| `window-show-tab-bar = never` | cmux has its own vertical tabs — ghostty's native tab bar just wastes space |
| `unfocused-split-opacity = 0.65` | instantly see which agent pane is active when running 3-4 side by side |
| `background-opacity = 0.95` | frosted glass effect adds depth without hurting readability |
| `font-size = 16` + `font-thicken` | stays legible through blur and at lower opacity on retina |
| `scrollback-limit = 50000` | agent output is verbose — 50k lines covers long sessions without eating ram |
| `macos-option-as-alt = true` | enables word-jump keybindings (opt+arrow) — but [breaks @ on turkish keyboards](https://github.com/manaflow-ai/cmux/issues/1653) |
| `window-padding-x = 16` | breathing room between text and cmux's sidebar |

---

## Automation & Scripting

### Blog post

- [How to Scriptize cmux: The Full Automation Surface (CLI, AppleScript, Raw Sockets)](https://notes.yigitkonur.com/j7ohBAkoc651DC) — deep dive into every automation method cmux supports.

### AppleScript & Raw Socket Docs

Rewritten automation docs from the cmux source, organized as a 10-part guide:

| # | Topic |
|---|-------|
| 00 | [Index](./docs/applescript/README.md) |
| 01 | [Overview](./docs/applescript/01-overview.md) |
| 02 | [Setup, Permissions & Verification](./docs/applescript/02-setup-permissions-and-verification.md) |
| 03 | [AppleScript Wrapper Pattern](./docs/applescript/03-applescript-cli-wrapper-pattern.md) |
| 04 | [Command Catalog](./docs/applescript/04-command-catalog-practical-index.md) |
| 05 | [Browser Command Surface](./docs/applescript/05-browser-command-surface.md) |
| 06 | [Socket v2 Protocol](./docs/applescript/06-socket-v2-protocol.md) |
| 07 | [Runtime v2 Method Inventory](./docs/applescript/07-runtime-v2-method-inventory.md) |
| 08 | [CLI to v2 Mapping](./docs/applescript/08-cli-to-v2-mapping.md) |
| 09 | [Automation Recipe Playbook](./docs/applescript/09-automation-recipe-playbook.md) |
| 10 | [Errors, Diagnostics & Triage](./docs/applescript/10-errors-diagnostics-triage.md) |

---

## Community Extensions

- [jasonraz/cmux-browser-mcp](https://github.com/jasonraz/cmux-browser-mcp) — Browser MCP server for cmux workflows.
- [webkaz/cmux-intel-builds](https://github.com/webkaz/cmux-intel-builds) — Intel Mac build/distribution helper.

**Upstream**

- [Ghostty](https://ghostty.org/) ([docs](https://ghostty.org/docs) · [config reference](https://ghostty.org/docs/config) · [source](https://github.com/ghostty-org/ghostty)) — the terminal engine under cmux.
- [agent-browser](https://github.com/vercel-labs/agent-browser) — Vercel's browser automation, ported into cmux.

---

## Community

| Channel | Link |
|---------|------|
| GitHub Discussions | [discussions](https://github.com/manaflow-ai/cmux/discussions) |
| GitHub Issues | [issues](https://github.com/manaflow-ai/cmux/issues) |
| Discord | [invite](https://discord.gg/xsgFEVrWCZ) |
| X / Twitter | [@manaflowai](https://x.com/manaflowai) |
| YouTube | [channel](https://www.youtube.com/channel/UCAa89_j-TWkrXfk9A3CbASw) |

**Notable threads:**
[Show HN](https://news.ycombinator.com/item?id=47079718) · [r/ClaudeCode intro](https://www.reddit.com/r/ClaudeCode/comments/1r43cdr/introducing_cmux_tmux_for_claude_code/) · [r/ClaudeCode vertical tabs](https://www.reddit.com/r/ClaudeCode/comments/1r9g45u/i_made_a_ghosttybased_terminal_with_vertical_tabs/)

---

## Articles & Coverage

- [Official Demo Video](https://www.youtube.com/watch?v=i-WxO5YUTOs)
- [Product Hunt](https://www.producthunt.com/products/cmux)
- [YC Company Page (Manaflow)](https://www.ycombinator.com/companies/manaflow)
- [UBOS: Introducing cmux](https://ubos.tech/news/introducing-cmux-a-ghostty%E2%80%91based-macos-terminal-with-vertical-tabs-and-ai%E2%80%91agent-notifications/)
- [Digg: cmux — The Terminal for Multitasking](https://digg.com/technology/QjlMUZ5/cmux-the-terminal-for-multitasking)
- [Microlaunch](https://microlaunch.net/p/cmux)

---

## Related Projects

- [coder/mux](https://github.com/coder/mux) — A different coding-agent multiplexer (not affiliated with `manaflow-ai/cmux`).

---

## Contributing

PRs welcome. Please read [CONTRIBUTING.md](./CONTRIBUTING.md) first.

## License

MIT — see [LICENSE](./LICENSE).

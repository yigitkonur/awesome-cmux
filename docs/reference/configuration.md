# Configuration

> **Source:** [cmux.com/docs/configuration](https://cmux.com/docs/configuration)

cmux reads terminal configuration from Ghostty config files. cmux-owned app settings live in `~/.config/cmux/settings.json`, including shortcuts, automation, sidebar behavior, notifications, and browser preferences.

---

## Ghostty Config File Locations

cmux looks for configuration in these locations (in order):

1. `~/.config/ghostty/config`
2. `~/Library/Application Support/com.mitchellh.ghostty/config`

Create the config file if it doesn't exist:

```sh
mkdir -p ~/.config/ghostty
touch ~/.config/ghostty/config
```

### Example Ghostty Config

```ini
# ~/.config/ghostty/config
font-family = SF Mono
font-size = 13
theme = One Dark
scrollback-limit = 50000
split-divider-color = #3e4451
working-directory = ~/code
```

---

## cmux settings.json

cmux keeps app-owned settings in a separate user file instead of mixing them into Ghostty config. On launch, if neither settings location exists, cmux writes a commented template to `~/.config/cmux/settings.json`.

### File Locations

1. `~/.config/cmux/settings.json` (preferred)
2. `~/Library/Application Support/com.cmuxterm.app/settings.json`

**Precedence:** `~/.config/cmux/settings.json` wins over the Application Support fallback. File-managed values override the value saved in the Settings window. Remove a key to fall back to the Settings value again.

**Reload:** Edit the file, then use `Cmd+Shift+,` or `cmux reload-config` to re-read it without restarting the app.

**Migrations:** Keep `schemaVersion` at `1` for now. Future cmux versions will use that field for upgrades.

The file accepts JSON with comments and trailing commas. The canonical schema is published at:
- [cmux-settings.schema.json](https://raw.githubusercontent.com/manaflow-ai/cmux/main/web/data/cmux-settings.schema.json)

### Example settings.json

```jsonc
// ~/.config/cmux/settings.json
{
  "$schema": "https://raw.githubusercontent.com/manaflow-ai/cmux/main/web/data/cmux-settings.schema.json",
  "schemaVersion": 1,

  "app": {
    "appearance": "dark",
    "newWorkspacePlacement": "afterCurrent"
  },

  "browser": {
    "openTerminalLinksInCmuxBrowser": true,
    "hostsToOpenInEmbeddedBrowser": ["localhost", "*.internal.example"]
  },

  "workspaceColors": {
    "colors": {
      "Red": "#C0392B",
      "Blue": "#1565C0",
      "Neon Mint": "#00F5D4"
    }
  },

  "shortcuts": {
    "bindings": {
      "toggleSidebar": "cmd+b",
      "newTab": ["ctrl+b", "c"]
    }
  }
}
```

---

## Schema Reference

### Metadata

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `$schema` | `string` | schema URL | Optional schema URL for editor completion and validation |
| `schemaVersion` | `integer` | `1` | Schema version for forward-compatible migrations |

### `app` — General App Preferences

| Key | Type | Default | Values | Description |
|-----|------|---------|--------|-------------|
| `app.language` | `string` | `"system"` | `system`, `en`, `ar`, `bs`, `zh-Hans`, `zh-Hant`, `da`, `de`, `es`, `fr`, `it`, `ja`, `ko`, `nb`, `pl`, `pt-BR`, `ru`, `th`, `tr` | Preferred app language |
| `app.appearance` | `string` | `"system"` | `system`, `light`, `dark` | App appearance mode |
| `app.appIcon` | `string` | `"automatic"` | `automatic`, `light`, `dark` | Dock and app switcher icon style |
| `app.newWorkspacePlacement` | `string` | `"afterCurrent"` | `top`, `afterCurrent`, `end` | Where new workspaces are inserted in the sidebar |
| `app.minimalMode` | `boolean` | `false` | — | Hide the workspace title bar and move controls into the sidebar |
| `app.keepWorkspaceOpenWhenClosingLastSurface` | `boolean` | `false` | — | When true, closing the last surface keeps the workspace open |
| `app.focusPaneOnFirstClick` | `boolean` | `true` | — | When cmux is inactive, the first click can activate and focus the clicked pane |
| `app.preferredEditor` | `string` | `""` | — | Custom editor command used by cmux where applicable |
| `app.reorderOnNotification` | `boolean` | `true` | — | Move workspaces with new notifications toward the top |
| `app.sendAnonymousTelemetry` | `boolean` | `true` | — | Allow anonymous telemetry |
| `app.warnBeforeQuit` | `boolean` | `true` | — | Show a confirmation before quitting cmux |
| `app.renameSelectsExistingName` | `boolean` | `true` | — | Select the current name when opening rename flows |
| `app.commandPaletteSearchesAllSurfaces` | `boolean` | `false` | — | Search every surface in the command palette switcher |

### `notifications` — Notification Behavior

| Key | Type | Default | Values | Description |
|-----|------|---------|--------|-------------|
| `notifications.dockBadge` | `boolean` | `true` | — | Show the unread count in the Dock tile |
| `notifications.showInMenuBar` | `boolean` | `true` | — | Show the menu bar extra |
| `notifications.unreadPaneRing` | `boolean` | `true` | — | Highlight panes with unread notifications |
| `notifications.paneFlash` | `boolean` | `true` | — | Flash the focused pane when requested |
| `notifications.sound` | `string` | `"default"` | `default`, `Basso`, `Blow`, `Bottle`, `Frog`, `Funk`, `Glass`, `Hero`, `Morse`, `Ping`, `Pop`, `Purr`, `Sosumi`, `Submarine`, `Tink`, `custom_file`, `none` | Notification sound preset |
| `notifications.customSoundFilePath` | `string` | `""` | — | Local path to the custom notification sound file |
| `notifications.command` | `string` | `""` | — | Optional shell command to run alongside notification delivery |

### `sidebar` — Sidebar Content & Metadata

| Key | Type | Default | Values | Description |
|-----|------|---------|--------|-------------|
| `sidebar.hideAllDetails` | `boolean` | `false` | — | Hide all per-workspace detail rows |
| `sidebar.branchLayout` | `string` | `"vertical"` | `vertical`, `inline` | Show git branch details stacked vertically or inline |
| `sidebar.showNotificationMessage` | `boolean` | `true` | — | Show the latest notification text in the sidebar |
| `sidebar.showBranchDirectory` | `boolean` | `true` | — | Show the workspace working directory |
| `sidebar.showPullRequests` | `boolean` | `true` | — | Show pull request metadata in the sidebar |
| `sidebar.openPullRequestLinksInCmuxBrowser` | `boolean` | `true` | — | Open sidebar pull request links in the embedded cmux browser |
| `sidebar.openPortLinksInCmuxBrowser` | `boolean` | `true` | — | Open sidebar port links in the embedded cmux browser |
| `sidebar.showSSH` | `boolean` | `true` | — | Show SSH connection details |
| `sidebar.showPorts` | `boolean` | `true` | — | Show listening ports |
| `sidebar.showLog` | `boolean` | `true` | — | Show recent log snippets |
| `sidebar.showProgress` | `boolean` | `true` | — | Show progress indicators |
| `sidebar.showCustomMetadata` | `boolean` | `true` | — | Show custom metadata pills |

### `workspaceColors` — Workspace Tab & Badge Colors

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `workspaceColors.indicatorStyle` | `string` | `"leftRail"` | Active workspace indicator style. Values: `leftRail`, `solidFill`, `rail`, `border`, `wash`, `lift`, `typography`, `washRail`, `blueWashColorRail` |
| `workspaceColors.selectionColor` | `string\|null` | `null` | Override the selected workspace background color |
| `workspaceColors.notificationBadgeColor` | `string\|null` | `null` | Override the unread notification badge color |
| `workspaceColors.colors` | `object` | *(16 built-in colors)* | Full named workspace color palette. Keep built-in keys you want, delete to remove, add to extend |

Default color palette:

```jsonc
{
  "Red": "#C0392B", "Crimson": "#922B21", "Orange": "#A04000",
  "Amber": "#7D6608", "Olive": "#4A5C18", "Green": "#196F3D",
  "Teal": "#006B6B", "Aqua": "#0E6B8C", "Blue": "#1565C0",
  "Navy": "#1A5276", "Indigo": "#283593", "Purple": "#6A1B9A",
  "Magenta": "#AD1457", "Rose": "#880E4F", "Brown": "#7B3F00",
  "Charcoal": "#3E4B5E"
}
```

### `sidebarAppearance` — Sidebar Tint Settings

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `sidebarAppearance.matchTerminalBackground` | `boolean` | `false` | Use the terminal background instead of the sidebar tint |
| `sidebarAppearance.tintColor` | `string` | `"#000000"` | Base sidebar tint color |
| `sidebarAppearance.lightModeTintColor` | `string\|null` | `null` | Sidebar tint override for light appearance |
| `sidebarAppearance.darkModeTintColor` | `string\|null` | `null` | Sidebar tint override for dark appearance |
| `sidebarAppearance.tintOpacity` | `number` | `0.03` | Sidebar tint opacity from 0 to 1 |

### `automation` — Socket Control & Automation

| Key | Type | Default | Values | Description |
|-----|------|---------|--------|-------------|
| `automation.socketControlMode` | `string` | `"cmuxOnly"` | `off`, `cmuxOnly`, `automation`, `password`, `allowAll`, `openAccess`, `fullOpenAccess`, `notifications`, `full` | Socket control mode |
| `automation.socketPassword` | `string\|null` | `""` | — | Password for password-mode socket access |
| `automation.claudeCodeIntegration` | `boolean` | `true` | — | Enable cmux integration hooks for Claude Code |
| `automation.claudeBinaryPath` | `string` | `""` | — | Custom path to the claude binary |
| `automation.portBase` | `integer` | `9100` | — | Starting value for workspace `CMUX_PORT` assignments |
| `automation.portRange` | `integer` | `10` | — | Number of ports reserved per workspace |

### `customCommands` — Command Trust Settings

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `customCommands.trustedDirectories` | `array<string>` | `[]` | Directories whose `cmux.json` commands can run without confirmation |

### `browser` — Embedded Browser Settings

| Key | Type | Default | Values | Description |
|-----|------|---------|--------|-------------|
| `browser.defaultSearchEngine` | `string` | `"google"` | `google`, `duckduckgo`, `bing`, `kagi`, `startpage` | Default search engine for non-URL queries |
| `browser.showSearchSuggestions` | `boolean` | `true` | — | Show omnibar search suggestions |
| `browser.theme` | `string` | `"system"` | `system`, `light`, `dark` | Embedded browser theme |
| `browser.openTerminalLinksInCmuxBrowser` | `boolean` | `true` | — | Open clicked terminal links in the embedded browser |
| `browser.interceptTerminalOpenCommandInCmuxBrowser` | `boolean` | `true` | — | Intercept terminal `open http(s)` commands and route through embedded browser |
| `browser.hostsToOpenInEmbeddedBrowser` | `array<string>` | `[]` | — | Allowlist of hosts that should stay inside the embedded browser |
| `browser.urlsToAlwaysOpenExternally` | `array<string>` | `[]` | — | Rules that always open matching URLs in the system browser |
| `browser.insecureHttpHostsAllowedInEmbeddedBrowser` | `array<string>` | `["localhost", "127.0.0.1", "::1", "0.0.0.0", "*.localtest.me"]` | — | HTTP hosts allowed without a warning prompt |
| `browser.showImportHintOnBlankTabs` | `boolean` | `true` | — | Show the browser import hint on blank tabs |
| `browser.reactGrabVersion` | `string` | `"0.1.29"` | — | Pinned react-grab version for the browser toolbar helper |

### `shortcuts` — Keyboard Shortcut Settings

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `shortcuts.showModifierHoldHints` | `boolean` | `true` | Show shortcut hint pills while holding Cmd or Ctrl |

See [Keyboard Shortcuts](./keyboard-shortcuts.md) for the full `shortcuts.bindings` reference.

# Getting Started

> **Source:** [cmux.com/docs/getting-started](https://cmux.com/docs/getting-started)

cmux is a lightweight, native macOS terminal built on [Ghostty](https://ghostty.org/) for managing multiple AI coding agents. It features vertical tabs, a notification panel, and a socket-based control API.

---

## Install

### DMG (recommended)

[Download for Mac](https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg)

Open the `.dmg` and drag cmux to your Applications folder. cmux auto-updates via Sparkle, so you only need to download once.

### Homebrew

```sh
brew tap manaflow-ai/cmux
brew install --cask cmux
```

To update later:

```sh
brew upgrade --cask cmux
```

On first launch, macOS may ask you to confirm opening an app from an identified developer. Click **Open** to proceed.

---

## Verify Installation

Open cmux and you should see:

- A terminal window with a vertical tab sidebar on the left
- One initial workspace already open
- The Ghostty-powered terminal ready for input

---

## CLI Setup

cmux includes a command-line tool for automation. Inside cmux terminals it works automatically. To use the CLI from outside cmux, create a symlink:

```sh
sudo ln -sf "/Applications/cmux.app/Contents/Resources/bin/cmux" /usr/local/bin/cmux
```

Then you can run commands like:

```sh
cmux list-workspaces
cmux notify --title "Build Complete" --body "Your build finished"
```

---

## Auto-Updates

cmux checks for updates automatically via Sparkle. When an update is available you'll see an update pill in the titlebar. You can also check manually via **cmux > Check for Updates** in the menu bar.

---

## Session Restore

After relaunch, cmux restores layout and metadata only:

- Window, workspace, and pane layout
- Working directories
- Terminal scrollback (best effort)
- Browser URL and navigation history

> **Note:** cmux does not restore live process state yet. Active terminal app sessions such as Claude Code, tmux, and vim are not resumed after app restart.

---

## Requirements

- macOS 14.0 or later
- Apple Silicon or Intel Mac

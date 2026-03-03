# Awesome cmux [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of high-quality resources for **[cmux](https://github.com/manaflow-ai/cmux)** — the Ghostty-based macOS terminal for running coding agents in parallel.

> [!IMPORTANT]
> This list is for **`manaflow-ai/cmux`**. Do not confuse it with other unrelated `cmux` projects (for example the Go library by soheilhy).

## Contents

- [Featured Blog Posts](#featured-blog-posts)
- [AppleScript & Raw Socket Docs (Rewritten)](#applescript--raw-socket-docs-rewritten)
- [Official](#official)
- [Install & Releases](#install--releases)
- [Documentation](#documentation)
- [Deep Technical References](#deep-technical-references)
- [Automation & Integration Ecosystem](#automation--integration-ecosystem)
- [Community & Discussions](#community--discussions)
- [Media, Launch, and Coverage](#media-launch-and-coverage)
- [Related Projects](#related-projects)

## Featured Blog Posts

### Start here

- [How to Scriptize cmux: The Full Automation Surface (CLI, AppleScript, Raw Sockets)](https://notes.yigitkonur.com/j7ohBAkoc651DC)

### Quick docs path (recommended order)

- [Getting Started](https://www.cmux.dev/docs/getting-started) — Install + first-run setup.
- [Concepts](https://www.cmux.dev/docs/concepts) — Understand windows/workspaces/panes/surfaces.
- [Configuration](https://www.cmux.dev/docs/configuration) — Tune behavior and defaults.
- [Keyboard Shortcuts](https://www.cmux.dev/docs/keyboard-shortcuts) — Daily key-driven workflow.
- [API Reference](https://www.cmux.dev/docs/api) — Full command surface.
- [Browser Automation](https://www.cmux.dev/docs/browser-automation) — Script browser actions from cmux.
- [Notifications](https://www.cmux.dev/docs/notifications) — Hook agent status into alerts.
- [Changelog](https://www.cmux.dev/docs/changelog) — Track recent changes.
- [Product Hunt](https://www.producthunt.com/products/cmux) — Launch page + community feedback.

### Official cmux posts

- [Introducing cmux](https://www.cmux.dev/blog/introducing-cmux) — Product launch and core philosophy.
- [Launching cmux on Show HN](https://www.cmux.dev/blog/show-hn-launch) — Launch story, feedback, and ecosystem momentum.
- [The Zen of cmux](https://www.cmux.dev/blog/zen-of-cmux) — Design principles behind cmux.

### External write-ups

- [Introducing cmux: A Ghostty-based macOS Terminal with Vertical Tabs and AI-agent Notifications](https://ubos.tech/news/introducing-cmux-a-ghostty%E2%80%91based-macos-terminal-with-vertical-tabs-and-ai%E2%80%91agent-notifications/) — Third-party overview article.
- [manaflow-ai/cmux: Ghostty-based macOS terminal…](https://news.radio-t.com/post/github-manaflow-ai-cmux-ghostty-based-macos-terminal-with-vertical-tabs-and-notifications-for-ai-coding-agents) — Community/news roundup mention.
- [cmux (ChatGate post)](https://chatgate.ai/post/cmux) — Short external explainer.
- [How to manage multiple AI agents in one workspace](https://microlaunch.net/h/how-to-manage-multiple-ai-agents-simultaneously-in-a-single-workspace-with-vertical-tabs-and-split-panes) — Tutorial-style listing.

## AppleScript & Raw Socket Docs (Rewritten)

Rewritten automation docs added to this awesome repo from the cmux `apple-script-docs` source set:

- [Docs Index](./docs/applescript/README.md)
- [01 — Overview](./docs/applescript/01-overview.md)
- [02 — Setup, Permissions, and Verification](./docs/applescript/02-setup-permissions-and-verification.md)
- [03 — AppleScript Wrapper Pattern](./docs/applescript/03-applescript-cli-wrapper-pattern.md)
- [04 — Command Catalog (Practical Index)](./docs/applescript/04-command-catalog-practical-index.md)
- [05 — Browser Command Surface](./docs/applescript/05-browser-command-surface.md)
- [06 — Socket v2 Protocol](./docs/applescript/06-socket-v2-protocol.md)
- [07 — Runtime v2 Method Inventory](./docs/applescript/07-runtime-v2-method-inventory.md)
- [08 — CLI to v2 Mapping](./docs/applescript/08-cli-to-v2-mapping.md)
- [09 — Automation Recipe Playbook](./docs/applescript/09-automation-recipe-playbook.md)
- [10 — Errors, Diagnostics, and Triage](./docs/applescript/10-errors-diagnostics-triage.md)

## Official

- [cmux.dev](https://www.cmux.dev/) — Official site.
- [GitHub Repository](https://github.com/manaflow-ai/cmux) — Source code.
- [README](https://github.com/manaflow-ai/cmux/blob/main/README.md) — Product overview and feature guide.
- [CHANGELOG.md](https://github.com/manaflow-ai/cmux/blob/main/CHANGELOG.md) — Release notes.
- [Contributing Guide](https://github.com/manaflow-ai/cmux/blob/main/CONTRIBUTING.md) — Contributor workflow.
- [Community Page](https://www.cmux.dev/community) — Official community links.

## Install & Releases

- [Latest DMG (Stable)](https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg)
- [Nightly DMG](https://github.com/manaflow-ai/cmux/releases/download/nightly/cmux-nightly-macos.dmg)
- [GitHub Releases](https://github.com/manaflow-ai/cmux/releases)
- [Nightly Release Tag](https://github.com/manaflow-ai/cmux/releases/tag/nightly)
- [Stable Appcast](https://github.com/manaflow-ai/cmux/releases/latest/download/appcast.xml)
- [Nightly Appcast](https://github.com/manaflow-ai/cmux/releases/download/nightly/appcast.xml)
- [Homebrew Tap](https://github.com/manaflow-ai/homebrew-cmux)
- [Tap Cask File](https://github.com/manaflow-ai/homebrew-cmux/blob/main/Casks/cmux.rb)
- [Homebrew Cask Registry Page](https://formulae.brew.sh/cask/cmux)
- [Homebrew Cask API JSON](https://formulae.brew.sh/api/cask/cmux.json)
- [Homebrew Update Workflow](https://github.com/manaflow-ai/cmux/blob/main/.github/workflows/update-homebrew.yml)
- [NewReleases Feed Example](https://newreleases.io/project/github/manaflow-ai/cmux/release/v0.61.0)

## Documentation

- [Docs Home](https://www.cmux.dev/docs/getting-started)
- [Concepts](https://www.cmux.dev/docs/concepts)
- [Configuration](https://www.cmux.dev/docs/configuration)
- [Keyboard Shortcuts](https://www.cmux.dev/docs/keyboard-shortcuts)
- [API Reference](https://www.cmux.dev/docs/api)
- [Browser Automation](https://www.cmux.dev/docs/browser-automation)
- [Notifications](https://www.cmux.dev/docs/notifications)
- [Docs Changelog](https://www.cmux.dev/docs/changelog)

### Blog

- [Blog Home](https://www.cmux.dev/blog)
- [Introducing cmux](https://www.cmux.dev/blog/introducing-cmux)
- [Launching cmux on Show HN](https://www.cmux.dev/blog/show-hn-launch)
- [The Zen of cmux](https://www.cmux.dev/blog/zen-of-cmux)

## Deep Technical References

- [agent-browser Port Spec](https://github.com/manaflow-ai/cmux/blob/main/docs/agent-browser-port-spec.md)
- [v2 API Migration Notes](https://github.com/manaflow-ai/cmux/blob/main/docs/v2-api-migration.md)
- [Notification Protocol Notes](https://github.com/manaflow-ai/cmux/blob/main/docs/notifications.md)
- [Ghostty Fork Workflow Notes](https://github.com/manaflow-ai/cmux/blob/main/docs/ghostty-fork.md)
- [Skills Directory](https://github.com/manaflow-ai/cmux/tree/main/skills)
- [cmux Skill](https://github.com/manaflow-ai/cmux/tree/main/skills/cmux)
- [cmux-browser Skill](https://github.com/manaflow-ai/cmux/tree/main/skills/cmux-browser)
- [cmux Debug Windows Skill](https://github.com/manaflow-ai/cmux/tree/main/skills/cmux-debug-windows)
- [Release Skill](https://github.com/manaflow-ai/cmux/tree/main/skills/release)
- [Setup Script](https://github.com/manaflow-ai/cmux/blob/main/scripts/setup.sh)
- [Debug Reload Script](https://github.com/manaflow-ai/cmux/blob/main/scripts/reload.sh)
- [VM Test Runner v1](https://github.com/manaflow-ai/cmux/blob/main/scripts/run-tests-v1.sh)
- [VM Test Runner v2](https://github.com/manaflow-ai/cmux/blob/main/scripts/run-tests-v2.sh)
- [E2E Test Runner](https://github.com/manaflow-ai/cmux/blob/main/scripts/run-e2e.sh)
- [CI Workflow](https://github.com/manaflow-ai/cmux/blob/main/.github/workflows/ci.yml)
- [E2E Workflow](https://github.com/manaflow-ai/cmux/blob/main/.github/workflows/test-e2e.yml)
- [Release Workflow](https://github.com/manaflow-ai/cmux/blob/main/.github/workflows/release.yml)
- [Nightly Workflow](https://github.com/manaflow-ai/cmux/blob/main/.github/workflows/nightly.yml)

## Automation & Integration Ecosystem

### Core Dependencies / Upstream Projects

- [Ghostty Website](https://ghostty.org/)
- [Ghostty Docs](https://ghostty.org/docs)
- [Ghostty Config Docs](https://ghostty.org/docs/config)
- [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty)
- [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

### AI Agent Tooling Ecosystem

- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code)
- [Claude Code Hooks](https://docs.claude.com/en/docs/claude-code/hooks)
- [Claude Code MCP](https://docs.claude.com/en/docs/claude-code/mcp)
- [OpenAI Codex GitHub](https://github.com/openai/codex)
- [OpenAI Codex Docs](https://developers.openai.com/codex)
- [Codex IDE Integration](https://developers.openai.com/codex/ide)
- [Codex MCP Guide](https://developers.openai.com/codex/mcp)
- [OpenCode Docs](https://opencode.ai/docs)
- [OpenCode MCP Servers](https://opencode.ai/docs/mcp-servers)
- [OpenCode Plugins](https://opencode.ai/docs/plugins)
- [OpenCode GitHub Integration](https://opencode.ai/docs/github)
- [Model Context Protocol Intro](https://modelcontextprotocol.io/introduction)

### Community-built Extensions / Helpers

- [jasonraz/cmux-browser-mcp](https://github.com/jasonraz/cmux-browser-mcp) — Browser MCP server around cmux workflows.
- [webkaz/cmux-intel-builds](https://github.com/webkaz/cmux-intel-builds) — Intel-focused build/distribution helper.

## Community & Discussions

- [GitHub Discussions](https://github.com/manaflow-ai/cmux/discussions)
- [GitHub Issues](https://github.com/manaflow-ai/cmux/issues)
- [Discord](https://discord.gg/xsgFEVrWCZ)
- [X / Twitter](https://x.com/manaflowai)
- [YouTube Channel](https://www.youtube.com/channel/UCAa89_j-TWkrXfk9A3CbASw)
- [LinkedIn](https://www.linkedin.com/company/manaflow-ai/)
- [Star History](https://star-history.com/#manaflow-ai/cmux&Date)

### Key Community Threads

- [Show HN Thread](https://news.ycombinator.com/item?id=47079718)
- [HN Comment Highlight 1](https://news.ycombinator.com/item?id=47083596)
- [HN Comment Highlight 2](https://news.ycombinator.com/item?id=47079369)
- [Reddit: Introducing cmux (r/ClaudeCode)](https://www.reddit.com/r/ClaudeCode/comments/1r43cdr/introducing_cmux_tmux_for_claude_code/)
- [Reddit: Ghostty-based cmux thread (r/ClaudeCode)](https://www.reddit.com/r/ClaudeCode/comments/1r9g45u/i_made_a_ghosttybased_terminal_with_vertical_tabs/)
- [Reddit: devopsish thread](https://www.reddit.com/r/devopsish/comments/1rebemz/manaflowaicmux_ghosttybased_macos_terminal_with/)
- [Reddit: cmux launch (r/cmux)](https://www.reddit.com/r/cmux/comments/1rih6nq/introducing_cmux_the_opensource_terminal_built/)
- [Reddit: OpenCode plugin thread (r/cmux)](https://www.reddit.com/r/cmux/comments/1rih6h1/opencode_plugin_for_cmux/)

## Media, Launch, and Coverage

- [Official Demo Video](https://www.youtube.com/watch?v=i-WxO5YUTOs)
- [Product Hunt](https://www.producthunt.com/products/cmux)
- [YC Company Page (Manaflow)](https://www.ycombinator.com/companies/manaflow)
- [Manaflow Website](https://manaflow.com/)
- [HN Mirror (Brian Lovin)](https://brianlovin.com/hn/47079718)
- [Radio-T mention](https://news.radio-t.com/post/github-manaflow-ai-cmux-ghostty-based-macos-terminal-with-vertical-tabs-and-notifications-for-ai-coding-agents)
- [UBOS mention](https://ubos.tech/news/introducing-cmux-a-ghostty%E2%80%91based-macos-terminal-with-vertical-tabs-and-ai%E2%80%91agent-notifications/)
- [Digg mention](https://digg.com/technology/QjlMUZ5/cmux-the-terminal-for-multitasking)
- [Microlaunch listing](https://microlaunch.net/p/cmux)

### X posts embedded in official launch writeup

- [Tweet ID 2024913161238053296](https://x.com/i/status/2024913161238053296)
- [Tweet ID 2025129675262251026](https://x.com/i/status/2025129675262251026)
- [Tweet ID 2024867449947275444](https://x.com/i/status/2024867449947275444)
- [Tweet ID 2024978414822916358](https://x.com/i/status/2024978414822916358)

## Related Projects

- [coder/mux](https://github.com/coder/mux) — Another coding-agent multiplexer project (separate from `manaflow-ai/cmux`).

---

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](./CONTRIBUTING.md) before opening a PR.

## Notes

- Last verified: **March 3, 2026**.
- Some sites (e.g. Reddit, Product Hunt, X) may rate-limit automated requests but remain valid in browsers.

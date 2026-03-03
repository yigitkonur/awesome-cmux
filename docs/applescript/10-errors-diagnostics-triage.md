# 10 — Errors, Diagnostics, and Triage

## Common errors and fixes

### `Unsupported browser subcommand`
- Cause: CLI parser doesn’t accept that browser verb.
- Fix: check `cmux browser --help`; use raw socket v2 if method exists in capabilities.

### `browser requires a subcommand`
- Cause: bad positional ordering (token interpreted as surface handle).
- Fix: use `cmux browser --surface <surface> <subcommand>`.

### `Socket not found at /tmp/...sock`
- Cause: wrong socket path or app not running.
- Fix:
  ```bash
  cmux ping
  ls -l /tmp/cmux*.sock
  cmux --socket /tmp/<actual>.sock ping
  ```

### AppleScript `-1708` (command not understood)
- Cause: direct Apple event not implemented for that command.
- Fix: use CLI or socket bridge.

### Accessibility errors (for `System Events`)
- Cause: missing Accessibility permission.
- Fix: enable runner under **System Settings → Privacy & Security → Accessibility**.

## Diagnostic checklist

```bash
cmux ping
cmux capabilities --json | jq '.version, .protocol, (.methods|length)'
cmux identify --json
cmux browser --help
```

## Regression checklist

1. Capture fresh `capabilities.methods`
2. Diff method set vs previous snapshot
3. Re-run critical scripts (notify/send/workspace/browser)
4. Update automation docs when behavior changes

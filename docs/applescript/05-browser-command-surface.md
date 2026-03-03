# 05 — Browser Command Surface (CLI vs Runtime)

## Important behavior

`capabilities --json` exposes more `browser.*` runtime methods than the CLI parser accepts directly.

## Practical implication

- Supported CLI browser verbs should be used first.
- If runtime method exists but parser blocks the form, call the method through raw socket v2.

## Common parser errors

### `browser requires a subcommand`
Usually caused by invalid first positional token being treated as a surface handle.

### `Unsupported browser subcommand`
Parser-level verb not supported even if a runtime method exists.

## Examples

```bash
cmux browser --help
cmux browser open https://example.com
cmux browser --surface surface:1 snapshot --interactive
```

If unsupported through CLI, fallback to socket v2 (`browser.*` method call).

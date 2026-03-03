# 03 — AppleScript CLI Wrapper Pattern

Use a single wrapper so scripts remain portable across PATH/app-bundled CLI setups.

```applescript
property defaultCmuxCLI : "/Applications/cmux.app/Contents/Resources/bin/cmux"

on findCmuxCLI()
	try
		set p to do shell script "command -v cmux || true"
		if p is not "" then return p
	end try
	return defaultCmuxCLI
end findCmuxCLI

on runCmux(argsText)
	set cliPath to my findCmuxCLI()
	return do shell script quoted form of cliPath & " " & argsText
end runCmux

on runCmuxSafe(argsText)
	try
		return my runCmux(argsText)
	on error errMsg number errNum
		return "ERR " & errNum & ": " & errMsg
	end try
end runCmuxSafe
```

## Example calls

```applescript
set pong to my runCmux("ping")
set ws to my runCmux("current-workspace")
my runCmux("notify --title " & quoted form of "AppleScript" & " --body " & quoted form of "Done")
```

## Quoting rule

Always use `quoted form of` for dynamic input.

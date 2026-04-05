# Browser Automation

> **Source:** [cmux.com/docs/browser-automation](https://cmux.com/docs/browser-automation)

The `cmux browser` command group provides browser automation against cmux browser surfaces. Use it to navigate, interact with DOM elements, inspect page state, evaluate JavaScript, and manage browser session data.

---

## Command Index

| Category | Subcommands |
|----------|-------------|
| Navigation and targeting | `identify`, `open`, `open-split`, `navigate`, `back`, `forward`, `reload`, `url`, `focus-webview`, `is-webview-focused` |
| Waiting | `wait` |
| DOM interaction | `click`, `dblclick`, `hover`, `focus`, `check`, `uncheck`, `scroll-into-view`, `type`, `fill`, `press`, `keydown`, `keyup`, `select`, `scroll` |
| Inspection | `snapshot`, `screenshot`, `get`, `is`, `find`, `highlight` |
| JavaScript and injection | `eval`, `addinitscript`, `addscript`, `addstyle` |
| Frames, dialogs, downloads | `frame`, `dialog`, `download` |
| State and session data | `cookies`, `storage`, `state` |
| Tabs and logs | `tab`, `console`, `errors` |

---

## Targeting a Browser Surface

Most subcommands require a target surface. You can pass it positionally or with `--surface`.

```sh
# Open a new browser split
cmux browser open https://example.com

# Discover focused IDs and browser metadata
cmux browser identify
cmux browser identify --surface surface:2

# Positional vs flag targeting are equivalent
cmux browser surface:2 url
cmux browser --surface surface:2 url
```

---

## Navigation

```sh
cmux browser open https://example.com
cmux browser open-split https://news.ycombinator.com

cmux browser surface:2 navigate https://example.org/docs --snapshot-after
cmux browser surface:2 back
cmux browser surface:2 forward
cmux browser surface:2 reload --snapshot-after
cmux browser surface:2 url

cmux browser surface:2 focus-webview
cmux browser surface:2 is-webview-focused
```

---

## Waiting

Use `wait` to block until selectors, text, URL fragments, load state, or a JavaScript condition is satisfied.

```sh
cmux browser surface:2 wait --load-state complete --timeout-ms 15000
cmux browser surface:2 wait --selector "#checkout" --timeout-ms 10000
cmux browser surface:2 wait --text "Order confirmed"
cmux browser surface:2 wait --url-contains "/dashboard"
cmux browser surface:2 wait --function "window.__appReady === true"
```

---

## DOM Interaction

Mutating actions support `--snapshot-after` for fast verification in scripts.

```sh
# Clicking
cmux browser surface:2 click "button[type='submit']" --snapshot-after
cmux browser surface:2 dblclick ".item-row"
cmux browser surface:2 hover "#menu"
cmux browser surface:2 focus "#email"

# Checkboxes
cmux browser surface:2 check "#terms"
cmux browser surface:2 uncheck "#newsletter"
cmux browser surface:2 scroll-into-view "#pricing"

# Text input
cmux browser surface:2 type "#search" "cmux"
cmux browser surface:2 fill "#email" --text "ops@example.com"
cmux browser surface:2 fill "#email" --text ""

# Keys
cmux browser surface:2 press Enter
cmux browser surface:2 keydown Shift
cmux browser surface:2 keyup Shift

# Selection and scrolling
cmux browser surface:2 select "#region" "us-east"
cmux browser surface:2 scroll --dy 800 --snapshot-after
cmux browser surface:2 scroll --selector "#log-view" --dx 0 --dy 400
```

---

## Inspection

Use structured getters for scripts and snapshots/screenshots for human review.

### Snapshots & Screenshots

```sh
cmux browser surface:2 snapshot --interactive --compact
cmux browser surface:2 snapshot --selector "main" --max-depth 5
cmux browser surface:2 screenshot --out /tmp/cmux-page.png
```

### Getters

```sh
cmux browser surface:2 get title
cmux browser surface:2 get url
cmux browser surface:2 get text "h1"
cmux browser surface:2 get html "main"
cmux browser surface:2 get value "#email"
cmux browser surface:2 get attr "a.primary" --attr href
cmux browser surface:2 get count ".row"
cmux browser surface:2 get box "#checkout"
cmux browser surface:2 get styles "#total" --property color
```

### Boolean Checks

```sh
cmux browser surface:2 is visible "#checkout"
cmux browser surface:2 is enabled "button[type='submit']"
cmux browser surface:2 is checked "#terms"
```

### Finders

```sh
cmux browser surface:2 find role button --name "Continue"
cmux browser surface:2 find text "Order confirmed"
cmux browser surface:2 find label "Email"
cmux browser surface:2 find placeholder "Search"
cmux browser surface:2 find alt "Product image"
cmux browser surface:2 find title "Open settings"
cmux browser surface:2 find testid "save-btn"
cmux browser surface:2 find first ".row"
cmux browser surface:2 find last ".row"
cmux browser surface:2 find nth 2 ".row"
```

### Highlighting

```sh
cmux browser surface:2 highlight "#checkout"
```

---

## JavaScript Eval and Injection

```sh
cmux browser surface:2 eval "document.title"
cmux browser surface:2 eval --script "window.location.href"

cmux browser surface:2 addinitscript "window.__cmuxReady = true;"
cmux browser surface:2 addscript "document.querySelector('#name')?.focus()"
cmux browser surface:2 addstyle "#debug-banner { display: none !important; }"
```

---

## State Management

### Cookies

```sh
cmux browser surface:2 cookies get
cmux browser surface:2 cookies get --name session_id
cmux browser surface:2 cookies set session_id abc123 --domain example.com --path /
cmux browser surface:2 cookies clear --name session_id
cmux browser surface:2 cookies clear --all
```

### Local & Session Storage

```sh
cmux browser surface:2 storage local set theme dark
cmux browser surface:2 storage local get theme
cmux browser surface:2 storage local clear
cmux browser surface:2 storage session set flow onboarding
cmux browser surface:2 storage session get flow
```

### Full State Save/Load

```sh
cmux browser surface:2 state save /tmp/cmux-browser-state.json
cmux browser surface:2 state load /tmp/cmux-browser-state.json
```

---

## Tabs

Browser tab operations map to browser surfaces in the active browser tab group.

```sh
cmux browser surface:2 tab list
cmux browser surface:2 tab new https://example.com/pricing

# Switch by index or by target surface
cmux browser surface:2 tab switch 1
cmux browser surface:2 tab switch surface:7

# Close current tab or a specific target
cmux browser surface:2 tab close
cmux browser surface:2 tab close surface:7
```

---

## Console and Errors

```sh
cmux browser surface:2 console list
cmux browser surface:2 console clear

cmux browser surface:2 errors list
cmux browser surface:2 errors clear
```

---

## Dialogs

```sh
cmux browser surface:2 dialog accept
cmux browser surface:2 dialog accept "Confirmed by automation"
cmux browser surface:2 dialog dismiss
```

---

## Frames

```sh
# Enter an iframe context
cmux browser surface:2 frame "iframe[name='checkout']"
cmux browser surface:2 click "#pay-now"

# Return to the top-level document
cmux browser surface:2 frame main
```

---

## Downloads

```sh
cmux browser surface:2 click "a#download-report"
cmux browser surface:2 download --path /tmp/report.csv --timeout-ms 30000
```

---

## Common Patterns

### Navigate, Wait, Inspect

```sh
cmux browser open https://example.com/login
cmux browser surface:2 wait --load-state complete --timeout-ms 15000
cmux browser surface:2 snapshot --interactive --compact
cmux browser surface:2 get title
```

### Fill a Form and Verify

```sh
cmux browser surface:2 fill "#email" --text "ops@example.com"
cmux browser surface:2 fill "#password" --text "$PASSWORD"
cmux browser surface:2 click "button[type='submit']" --snapshot-after
cmux browser surface:2 wait --text "Welcome"
cmux browser surface:2 is visible "#dashboard"
```

### Capture Debug Artifacts on Failure

```sh
cmux browser surface:2 console list
cmux browser surface:2 errors list
cmux browser surface:2 screenshot --out /tmp/cmux-failure.png
cmux browser surface:2 snapshot --interactive --compact
```

### Persist and Restore Browser Session

```sh
cmux browser surface:2 state save /tmp/session.json
# ...later...
cmux browser surface:2 state load /tmp/session.json
cmux browser surface:2 reload
```

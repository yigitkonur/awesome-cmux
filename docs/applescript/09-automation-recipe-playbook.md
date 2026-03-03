# 09 — Automation Recipe Playbook

## 1) Health check

```applescript
set pong to do shell script "cmux ping"
set ws to do shell script "cmux current-workspace"
return "pong=" & pong & ", ws=" & ws
```

## 2) Notification

```applescript
do shell script "cmux notify --title " & quoted form of "Build" & " --body " & quoted form of "Completed"
```

## 3) Send command to current surface

```applescript
do shell script "cmux send " & quoted form of "echo hello from applescript"
```

## 4) Select workspace

```applescript
do shell script "cmux select-workspace --workspace workspace:2"
```

## 5) Open browser split

```applescript
do shell script "cmux browser open https://example.com"
```

## 6) Browser snapshot (explicit surface)

```applescript
do shell script "cmux browser --surface surface:1 snapshot --interactive"
```

## 7) Read screen output

```applescript
set txt to do shell script "cmux read-screen --lines 80"
return txt
```

## 8) Sidebar status/progress

```applescript
do shell script "cmux set-status build running --icon hammer"
do shell script "cmux set-progress 0.42 --label " & quoted form of "Compiling"
```

## 9) Raw socket call from AppleScript

```applescript
set py to "import socket,json; s=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM); s.connect('/tmp/cmux.sock'); req={'id':'1','method':'system.identify','params':{}}; s.sendall((json.dumps(req)+'\\n').encode()); print(s.recv(65535).decode()); s.close()"
set out to do shell script "/usr/bin/python3 -c " & quoted form of py
return out
```

## 10) Safe notification fallback

```applescript
try
	do shell script "cmux notify --title " & quoted form of "cmux" & " --body " & quoted form of "Task complete"
on error
	display notification "Task complete" with title "cmux"
end try
```

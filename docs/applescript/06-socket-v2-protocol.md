# 06 — Socket v2 Protocol

## Transport

- Unix domain socket (default: `/tmp/cmux.sock`)
- Newline-delimited JSON objects

## Request envelope

```json
{"id":"1","method":"system.identify","params":{}}
```

## Response envelope

```json
{"id":"1","ok":true,"result":{}}
```

Error envelope:

```json
{"id":"1","ok":false,"error":{"code":"invalid_params","message":"..."}}
```

## Probe example

```bash
python3 - <<'PY'
import socket, json
s=socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect('/tmp/cmux.sock')
req={"id":"1","method":"system.ping","params":{}}
s.sendall((json.dumps(req)+"\n").encode())
print(s.recv(65535).decode().strip())
s.close()
PY
```

## AppleScript bridge pattern

```applescript
set py to "import socket,json; s=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM); s.connect('/tmp/cmux.sock'); req={'id':'1','method':'system.ping','params':{}}; s.sendall((json.dumps(req)+'\\n').encode()); print(s.recv(65535).decode().strip()); s.close()"
do shell script "/usr/bin/python3 -c " & quoted form of py
```

## When to use raw v2

Use raw v2 when CLI command shape does not expose the runtime method you need.

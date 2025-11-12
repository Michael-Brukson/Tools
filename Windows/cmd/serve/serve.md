## serve.cmd

A 'simpler' way to serve the current directory's files to the local wifi.

Calls `python -m http.server` with a specified port and directory, binding it to `0.0.0.0` to broadcast to the local wifi. Then, calls `ipv4_qr` with the specified port to print a qr code to the http address of the served directory.

To close the server, either use `Ctrl + C` while focused on the window, or simply close the window itself.

_REQUIRES_ Python version 3.\* \
_REQUIRES_ That Windows/cmd/ip is set as a path environment variable. (will set up automation for this later)

### Accepts parameters:

- `-dir` / `-d` `<string>`: "Directory"; the directory to serve. Defaults to current directory.
- `-port` / `-p` `<integer>`: "Port"; the port of the address of the qr code and http address of the served directory. Defaults to 80.
- `-verbose` / `-v` `<boolean>`: "Verbose"; whether to print out info about port and served directory. Defaults to false.

### Examples:

No parameters, qr and hosted server for `http://192.168.1.220:80`:

```bash
C:\>serve
█████████████████████████████████
█████████████████████████████████
████ ▄▄▄▄▄ █ ██▀▀ ▄▀ █ ▄▄▄▄▄ ████
████ █   █ █  ▀█ ██▀██ █   █ ████
████ █▄▄▄█ █▀  █▄  ▀▄█ █▄▄▄█ ████
████▄▄▄▄▄▄▄█▄█ ▀▄█ █ █▄▄▄▄▄▄▄████
████  █▀▄▄▄▀██▄█▄  ██▀▀▄▀ ▄ ▄████
████▀ ██▀ ▄▀▄ ▄█▀██ ▀█ ▀▄▄ ▀█████
████ ▀  ▄▀▄▄▀█▀▄▀ ▀▄ ▀█  ▄▄ ▄████
██████▀█  ▄▄▄▄▀ ▄ ███▄██▄  ▀█████
████▄▄▄▄██▄▄▀ ██▄  █ ▄▄▄ █▄██████
████ ▄▄▄▄▄ █▀█▄█▀██▄ █▄█  ▄▀█████
████ █   █ █▄ █▄▀▄ ▄ ▄▄▄▄ ▀▄ ████
████ █▄▄▄█ █▀█▀ ▄ ▄▀█▀█  ██ █████
████▄▄▄▄▄▄▄█▄███▄▄█▄█▄▄█▄█▄▄▄████
█████████████████████████████████
█████████████████████████████████
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
```

With `-verbose` / `-v`:

```bash
C:\>serve -v
Port: 80
Serving directory: C:\
█████████████████████████████████
█████████████████████████████████
████ ▄▄▄▄▄ █ ██▀▀ ▄▀ █ ▄▄▄▄▄ ████
████ █   █ █  ▀█ ██▀██ █   █ ████
████ █▄▄▄█ █▀  █▄  ▀▄█ █▄▄▄█ ████
████▄▄▄▄▄▄▄█▄█ ▀▄█ █ █▄▄▄▄▄▄▄████
████  █▀▄▄▄▀██▄█▄  ██▀▀▄▀ ▄ ▄████
████▀ ██▀ ▄▀▄ ▄█▀██ ▀█ ▀▄▄ ▀█████
████ ▀  ▄▀▄▄▀█▀▄▀ ▀▄ ▀█  ▄▄ ▄████
██████▀█  ▄▄▄▄▀ ▄ ███▄██▄  ▀█████
████▄▄▄▄██▄▄▀ ██▄  █ ▄▄▄ █▄██████
████ ▄▄▄▄▄ █▀█▄█▀██▄ █▄█  ▄▀█████
████ █   █ █▄ █▄▀▄ ▄ ▄▄▄▄ ▀▄ ████
████ █▄▄▄█ █▀█▀ ▄ ▄▀█▀█  ██ █████
████▄▄▄▄▄▄▄█▄███▄▄█▄█▄▄█▄█▄▄▄████
█████████████████████████████████
█████████████████████████████████
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
```

With all parameters:

```bash
C:\>serve -v -p 3000 -d C:\Tools\Windows\ps
Port: 3000
Serving directory: C:\Tools\Windows\ps
█████████████████████████████████
█████████████████████████████████
████ ▄▄▄▄▄ █   █▄██ ▀█ ▄▄▄▄▄ ████
████ █   █ █ ▀▄ ██▄▀██ █   █ ████
████ █▄▄▄█ █▀██▀▀  ▀▄█ █▄▄▄█ ████
████▄▄▄▄▄▄▄█▄▀▄█ █▄█ █▄▄▄▄▄▄▄████
████▄▄█▀ ▄▄█▀▀▀▄▀  ██▀▀▄▀ ▄ ▄████
████▄█▄ ▀ ▄▄██▀ ▄██ ▀█ ▀▄▄ ▀█████
████▀▀▀█▄▀▄▀▀▀▄█▄▀ ▄ ▀█  ▄▄ ▄████
███████▄▀▀▄▄ █▀█▀████▄██▄  ▀█████
████▄▄▄██▄▄█ ▄ ▄▀▄ █ ▄▄▄ █▄██████
████ ▄▄▄▄▄ █▀▀▀ ▄██▄ █▄█  ▄▀█████
████ █   █ █▄█ █▄ █▄ ▄▄▄▄▀ ▄ ████
████ █▄▄▄█ █▀  █▀██▀█▀█  ██ █████
████▄▄▄▄▄▄▄█▄▄█▄▄▄▄▄█▄▄█▄█▄▄▄████
█████████████████████████████████
█████████████████████████████████
Serving HTTP on 0.0.0.0 port 3000 (http://0.0.0.0:3000/) ...
```

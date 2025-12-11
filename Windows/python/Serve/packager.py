import os
import sys
import tempfile
import shutil
import PyInstaller.__main__

root = os.path.abspath(os.path.dirname(__file__))
root = root[:root.rfind('\\Windows\\python\\Serve')]

helpers = [
    os.path.join(root, "Windows", "cmd", "serve", "serve.cmd"),
    os.path.join(root, "Windows", "cmd", "ip", "ipv4_qr.cmd"),
    os.path.join(root, "Windows", "cmd", "ip", "ipv4.cmd"),
    os.path.join(root, "Windows", "python", "Serve", "favicon.ico"),
]

data_args = []
for p in helpers:
    if os.path.exists(p):
        data_args += ["--add-data", f"{p}{os.pathsep}."]

entry = os.path.join(root, "Windows", "python", "Serve", "Serve.py")
icon = os.path.join(root, "Windows", "python", "Serve", "favicon.ico")

temp = tempfile.mkdtemp(prefix='pyi_')
name: str = "Serve"

pyi = [
    f"--name={name}",
    "--onefile",
    "--noconfirm",
    "--clean",
    "--windowed",
    f"--distpath={os.path.join(root, "Windows", "python", name)}",
    f"--workpath={os.path.join(temp, "work")}",
    f"--specpath={temp}",
    f"--icon={icon}",
] + data_args + [entry]

if __name__ == '__main__':
    try: 
        PyInstaller.__main__.run(pyi)
        build = os.path.join(root, "build")
        if os.path.isdir(build):
            try: shutil.rmtree(build)
            except Exception: pass
    finally:
        try: shutil.rmtree(temp)
        except Exception: pass
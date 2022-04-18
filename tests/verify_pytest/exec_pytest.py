import subprocess
import sys


def exec_pytest(file: str) -> int:
    args = ["pytest", file, "--import-mode=importlib"]
    try:
        subprocess.run(args, text=True, check=True, stdout=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(e, file=sys.stderr)
        return 1
    else:
        print("Hello World")
        return 0

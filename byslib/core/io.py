import sys
from functools import partial


def sinput() -> str:
    return sys.stdin.readline().rstrip("\r\n")


def int1(s: str) -> int:
    return int(s) - 1


debug = partial(print, file=sys.stdout)

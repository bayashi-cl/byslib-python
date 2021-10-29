# region template
import sys
import typing
from typing import Callable, Dict, List, Set, Tuple

sys.setrecursionlimit(10 ** 6)
Vec = List[int]
VecVec = List[Vec]
sinput: Callable[..., str] = sys.stdin.readline
MOD: int = 1000000007
INF: float = float("Inf")
IINF: int = sys.maxsize
# endregion


def make_adj(board: List[str]) -> VecVec:
    h = len(board)
    w = len(board[0])
    adj: VecVec = [[] for _ in range(h * w)]

    delta = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for i in range(h):
        for j in range(w):
            if board[i][j] == "#":
                continue
            now = i * w + j
            for di, dj in delta:
                if i + di < 0 or h <= i + di:
                    continue
                if j + dj < 0 or w <= j + dj:
                    continue
                adj[now].append((i + di) * w + j + dj)

    return adj


def main() -> None:
    ...


if __name__ == "__main__":
    main()

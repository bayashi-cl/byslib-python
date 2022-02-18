# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind
import sys
from typing import Callable

from byslib.data.union_find import UnionFindTree

sys.setrecursionlimit(10 ** 6)
sinput: Callable[..., str] = sys.stdin.readline


def main() -> None:
    n, q = map(int, sinput().split())
    uft = UnionFindTree(n)
    for _ in range(q):
        t, u, v = map(int, sinput().split())
        if t == 0:
            uft.union(u, v)
        else:
            print(1 if uft.same(u, v) else 0)


if __name__ == "__main__":
    main()

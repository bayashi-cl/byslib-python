"""
https://atcoder.jp/contests/typical90/tasks/typical90_u
"""

# region template
from __future__ import annotations

import sys
from typing import Callable, Final

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

sys.setrecursionlimit(10 ** 9)
sinput: Callable[..., str] = sys.stdin.readline
INF: Final[float] = float("inf")
MOD: Final[int] = 10 ** 9 + 7
# endregion


def main() -> None:
    n, m = map(int, sinput().split())
    edge = np.array([sinput().split() for _ in range(m)], dtype=np.int64).T
    cost = np.ones(m).T
    graph = csr_matrix((cost, edge - 1), (n, n))
    _, scc = connected_components(graph, directed=True, connection="strong")
    _, count = np.unique(scc, return_counts=True)
    ans = np.sum(count * (count - 1) // 2)
    print(ans)


if __name__ == "__main__":
    main()

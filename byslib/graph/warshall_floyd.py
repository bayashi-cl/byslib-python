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


class WarshallFloyd:
    Edge = Tuple[int, int]  # (cost, node)
    Adj = List[List[Edge]]

    def __init__(self, graph: Adj) -> None:
        self.n_node = len(graph)
        self.prev = [-1] * self.n_node
        self.cost = [[INF] * self.n_node for _ in range(self.n_node)]

        for dep, edge in enumerate(graph):
            for dist, arr in edge:
                self.cost[dep][arr] = dist

        for i in range(self.n_node):
            self.cost[i][i] = 0

    def search(self) -> None:
        for k in range(self.n_node):
            for i in range(self.n_node):
                for j in range(self.n_node):
                    if (dist := self.cost[i][k] + self.cost[k][j]) < self.cost[i][j]:
                        self.cost[i][j] = dist
                        self.prev[j] = k

    def path_finder(self, to: int) -> List[int]:
        assert to <= self.n_node

        path = []
        while to != -1:
            path.append(to)
            to = self.prev[to]

        return path[::-1]


def main() -> None:
    ...


if __name__ == "__main__":
    main()

# region template
import sys
import typing
from typing import List, Union
from collections import deque

sys.setrecursionlimit(10 ** 6)
Vec = typing.List[int]
VecVec = typing.List[Vec]
sinput: typing.Callable[..., str] = sys.stdin.readline
MOD: int = 1000000007
INF: float = float("Inf")
IINF: int = sys.maxsize
# endregion


def bfs(adj: VecVec, start: int, n_node: int) -> List[Union[int, float]]:
    q = deque([start])
    cost = [float("inf")] * n_node
    cost[start] = 0
    while q:
        node_from = q.popleft()
        for node_to in adj[node_from]:
            if cost[node_to] == float("inf"):
                cost[node_to] = cost[node_from] + 1
                q.append(node_to)
    return cost


class BreadthFirstSearch:
    def __init__(self, graph: VecVec) -> None:
        self.graph = graph
        self.n = len(graph)

    def search(self, start: int) -> typing.List[typing.Union[float, int]]:
        que = deque([start])
        self.cost = [INF] * self.n
        self.cost[start] = 0

        while que:
            dep = que.popleft()
            for arr in self.graph[dep]:
                if self.cost[arr] == INF:
                    self.cost[arr] = self.cost[dep] + 1
                    que.append(arr)

        return self.cost

# @title Depth First Search
from typing import Generator, List

from .graph import LilMatrix


class DepthFirstSearch:
    """DFS

    pre-order and post-order generator

    Notes
    -----
    Time complexity

    O(V + E)

    References
    ----------
    ..[1] 🐜 p.33
    """

    cost: List[int]

    def __init__(self, graph: LilMatrix) -> None:
        """Parameters
        ----------
        graph
            (Un)Weighted graph
        """
        self.n = len(graph)
        self.graph = graph
        self.prev = [-1] * self.n

    def pre_order(self, start: int) -> Generator[int, None, None]:
        self.cost = [-1] * self.n
        self.cost[start] = 0
        que = [start]
        while que:
            now = que.pop()
            if now >= 0:
                yield now
                for dest, _ in self.graph[now]:
                    if self.cost[dest] != -1:
                        continue
                    self.cost[dest] = self.cost[now] + 1
                    self.prev[dest] = now
                    que.append(dest)

    def post_order(self, start: int) -> Generator[int, None, None]:
        self.cost = [-1] * self.n
        self.cost[start] = 0
        que = [~start, start]
        while que:
            now = que.pop()
            if now >= 0:
                for dest, _ in self.graph[now]:
                    if self.cost[dest] != -1:
                        continue
                    self.cost[dest] = self.cost[now] + 1
                    self.prev[dest] = now
                    que.append(~dest)
                    que.append(dest)

            else:
                yield ~now

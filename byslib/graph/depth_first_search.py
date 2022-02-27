from typing import Generator, List

from .edge import AdjacencyList


class DepthFirstSearch:
    cost: List[int]

    def __init__(self, graph: AdjacencyList) -> None:
        self.n = len(graph)
        self.graph = graph
        self.prev = [-1] * self.n

    def pre_order(self, start: int) -> Generator[int, int, None]:
        self.cost = [-1] * self.n
        self.cost[start] = 0
        que = [start]
        while que:
            now = que.pop()
            if now >= 0:
                yield now
                for nxt in self.graph[now]:
                    if self.cost[nxt.dest] != -1:
                        continue
                    self.cost[nxt.dest] = self.cost[now] + 1
                    self.prev[nxt.dest] = now
                    que.append(nxt.dest)

    def post_order(self, start: int) -> Generator[int, int, None]:
        self.cost = [-1] * self.n
        self.cost[start] = 0
        que = [~start, start]
        while que:
            now = que.pop()
            if now >= 0:
                for nxt in self.graph[now]:
                    if self.cost[nxt.dest] != -1:
                        continue
                    self.cost[nxt.dest] = self.cost[now] + 1
                    self.prev[nxt.dest] = now
                    que.append(~nxt.dest)
                    que.append(nxt.dest)

            else:
                yield ~now

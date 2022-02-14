import sys
import typing
from collections import deque

from edge import DeWEdge, Edge, WEdge

T = typing.TypeVar("T", Edge, WEdge, DeWEdge)
Adj = typing.List[typing.List[T]]


class BreadthFirstSearch(typing.Generic[T]):
    INF = sys.maxsize // 2
    graph: Adj[T]
    n_node: int
    cost: typing.List[int]
    prev: typing.List[int]

    def __init__(self, graph: Adj[T], start: int = 0, err_val: int = -1) -> None:
        self.graph = graph
        self.n_node = len(graph)
        if start < 0 or self.n_node <= start:
            raise ValueError("start is out of graph")
        self.cost = [self.INF] * self.n_node
        self.cost = [-1] * self.n_node
        self.search(start)
        for i in range(self.n_node):
            if self.cost[i] == self.INF:
                self.cost[i] = err_val

    def search(self, start: int) -> None:
        que: typing.Deque[int] = deque()
        que.append(start)
        self.cost[start] = 0
        while que:
            now = que.popleft()
            for to in self.graph[now]:
                if self.cost[to.arr] == self.INF:
                    self.cost[to.arr] = self.cost[now] + 1
                    self.prev[to.arr] = now
                    que.append(to.arr)

    def path(self, to: int) -> typing.List[int]:
        if to < 0 or self.n_node <= to:
            raise ValueError("to is out of graph")
        res = []
        while to != -1:
            res.append(to)
            to = self.prev[to]
        return res[::-1]

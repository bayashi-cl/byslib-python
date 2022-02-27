from collections import deque
from typing import Deque

from ..core.const import IINF
from .edge import AdjacencyList
from .utility import SSSPResult


def breadth_first_search(graph: AdjacencyList, source: int) -> SSSPResult:
    n = len(graph)
    prev = [-1] * n
    cost = [IINF] * n
    cost[source] = 0
    que: Deque[int] = deque()
    que.append(source)
    while que:
        top = que.popleft()
        for nxt in graph[top]:
            if cost[nxt.dest] == IINF:
                cost[nxt.dest] = cost[top] + 1
                prev[nxt.dest] = top
                que.append(nxt.dest)

    return cost, prev


def zero_one_bfs(graph: AdjacencyList, source: int, one: int = 1) -> SSSPResult:
    n = len(graph)
    cost = [IINF] * n
    cost[source] = 0
    prev = [-1] * n
    que: Deque[int] = deque()
    que.append(source)
    while que:
        top = que.popleft()
        for nxt in graph[top]:
            nxt_cost = cost[top] + nxt.weight
            if nxt_cost < cost[nxt.dest]:
                cost[nxt.dest] = nxt_cost
                prev[nxt.dest] = top
                if nxt.weight == 0:
                    que.appendleft(nxt.dest)
                elif nxt.weight == one:
                    que.append(nxt.dest)
                else:
                    raise ValueError

    return cost, prev

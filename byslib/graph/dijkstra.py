import heapq
from typing import List, Tuple

from .edge import AdjacencyList
from ..core.const import IINF


def dijkstra(graph: AdjacencyList, source: int) -> Tuple[List[int], List[int]]:
    n = len(graph)
    cost = [IINF] * n
    cost[source] = 0
    prev = [-1] * n
    que: List[Tuple[int, int]] = [(0, source)]
    while que:
        top_cost, top = heapq.heappop(que)
        if cost[top] < top_cost:
            continue
        for nxt in graph[top]:
            nxt_cost = cost[top] + nxt.weight
            if nxt_cost < cost[nxt.dest]:
                cost[nxt.dest] = nxt_cost
                prev[nxt.dest] = top
                heapq.heappush(que, (nxt_cost, nxt.dest))
    return cost, prev

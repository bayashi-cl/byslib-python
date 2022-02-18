import heapq
from typing import List, Tuple

from .edge import AdjacencyList
from .result import SSSPResult


def dijkstra(graph: AdjacencyList, source: int) -> SSSPResult:
    n = len(graph)
    res = SSSPResult(n, source)
    res.cost[source] = 0
    que: List[Tuple[int, int]] = []
    heapq.heappush(que, (0, source))
    while que:
        top_cost, top = heapq.heappop(que)
        if res.cost[top] < top_cost:
            continue
        for nxt in graph[top]:
            nxt_cost = res.cost[top] + nxt.weight
            if nxt_cost < res.cost[nxt.dest]:
                res.cost[nxt.dest] = nxt_cost
                res.prev[nxt.dest] = top
                heapq.heappush(que, (nxt_cost, nxt.dest))
    return res

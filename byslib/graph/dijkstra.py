# @title Dijkstra
import heapq
from typing import Iterable, List, Tuple, Union

from ..core.const import IINF
from .graph import LilMatrix


def dijkstra(
    graph: LilMatrix, source: Union[int, Iterable[int]]
) -> Tuple[List[int], List[int]]:
    """Dijkstra

    Parameters
    ----------
    graph
        Weighted Graph
    source
        (list of) source

    Returns
    -------
        (cost, prev)

    Notes
    -----
    Time complexity

    O(V + Elog(V))

    References
    ----------
    ..[1] 🐜 p.96

    """
    n = len(graph)
    cost = [IINF] * n
    prev = [-1] * n
    que: List[Tuple[int, int]] = []

    if isinstance(source, int):
        que = [(0, source)]
        cost[source] = 0
    else:
        que = [(0, si) for si in source]
        for si in source:
            cost[si] = 0
    heapq.heapify(que)

    while que:
        top_cost, top = heapq.heappop(que)
        if cost[top] < top_cost:
            continue
        for dest, weight in graph[top]:
            nxt_cost = cost[top] + weight
            if nxt_cost < cost[dest]:
                cost[dest] = nxt_cost
                prev[dest] = top
                heapq.heappush(que, (nxt_cost, dest))

    return cost, prev

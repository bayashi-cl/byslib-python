# @title Breadth First Search
from collections import deque
from typing import Deque, Iterable, List, Tuple, Union

from ..core.const import IINF
from .graph import LilMatrix


def breadth_first_search(
    graph: LilMatrix, source: Union[int, Iterable[int]]
) -> Tuple[List[int], List[int]]:
    """BFS

    Parameters
    ----------
    graph
        (Un)Weighted graph
    source
        source or list of source

    Returns
    -------
        (cost, prev)

    Notes
    -----
    Time complexity

    O(V + E)

    References
    ----------
    ..[1] 🐜 p.36
    """
    n = len(graph)
    prev = [-1] * n
    cost = [IINF] * n

    if isinstance(source, int):
        cost[source] = 0
        que: Deque[int] = deque([source])
    else:
        for s in source:
            cost[s] = 0
        que = deque(source)

    while que:
        top = que.popleft()
        for dest, _ in graph[top]:
            if cost[dest] == IINF:
                cost[dest] = cost[top] + 1
                prev[dest] = top
                que.append(dest)

    return cost, prev


def zero_one_bfs(
    graph: LilMatrix, source: Union[int, Iterable[int]], one: int = 1
) -> Tuple[List[int], List[int]]:
    """01BFS

    Parameters
    ----------
    graph
        Weighted graph
    source
        source or list of source
    one
        cost of `one`

    Returns
    -------
        (cost, prev)

    Notes
    -----
    Time complexity

    O(V + E)
    """
    n = len(graph)
    cost = [IINF] * n
    prev = [-1] * n

    if isinstance(source, int):
        cost[source] = 0
        que: Deque[int] = deque([source])
    else:
        for s in source:
            cost[s] = 0
        que = deque(source)

    while que:
        top = que.popleft()
        for dest, weight in graph[top]:
            nxt_cost = cost[top] + weight
            if nxt_cost < cost[dest]:
                cost[dest] = nxt_cost
                prev[dest] = top
                if weight == 0:
                    que.appendleft(dest)
                elif weight == one:
                    que.append(dest)
                else:
                    raise ValueError

    return cost, prev

# @title Warshall Floyd
from typing import List

from ..core.const import IINF
from .edge import Edge


def warshall_floyd(elist: List[Edge], n: int) -> List[List[int]]:
    """warshall floyd

    Parameters
    ----------
    elist
        List of Edge
    n
        Vertex Size

    Returns
    -------
    Cost matrix

    Notes
    -----
    Time complexity

    O(N^3)

    References
    ----------
    ..[1] 🐜 p.98
    """
    cost = [[IINF] * n for _ in range(n)]
    for e in elist:
        cost[e.src][e.dest] = e.weight
    for i in range(n):
        cost[i][i] == 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if cost[i][k] == IINF or cost[k][j] == IINF:
                    continue
                tmp_cost = cost[i][k] + cost[k][j]
                if cost[i][j] > tmp_cost:
                    cost[i][j] = tmp_cost

    return cost

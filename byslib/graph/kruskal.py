# @title kruskal
from typing import List, Tuple

from ..data.union_find import UnionFindTree
from .edge import Edge


def kruskal(edges: List[Edge], n_node: int) -> Tuple[int, List[Edge]]:
    """Kruskal

    Parameters
    ----------
    edges
        List of Edges
    n_node
        Node size

    Returns
    -------
    Minimum (cost, Tree)

    Notes
    -----
    Time complexity

    O(E log(E))

    References
    ----------
    ..[1] 🐜 p.99
    """

    edges.sort()
    uft = UnionFindTree(n_node)
    mst: List[Edge] = []
    cost = 0
    for e in edges:
        if uft.union(e.src, e.dest):
            cost += e.weight
            mst.append(e)
    return cost, mst

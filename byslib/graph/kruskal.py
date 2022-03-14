from typing import List, Tuple

from ..data.union_find import UnionFindTree
from .edge import Edge


def kruskal(edges: List[Edge], n_node: int) -> Tuple[int, List[Edge]]:
    edges.sort()
    uft = UnionFindTree(n_node)
    mst: List[Edge] = []
    cost = 0
    for e in edges:
        if uft.union(e.src, e.dest):
            cost += e.weight
            mst.append(e)
    return cost, mst

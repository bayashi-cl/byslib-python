# @title Graph Utility
from typing import List, Tuple

from .depth_first_search import DepthFirstSearch
from .graph import LilMatrix


def restore_path(prev: List[int], to: int) -> List[int]:
    res = []
    while to != -1:
        res.append(to)
        to = prev[to]
    return res[::-1]


def rooted_tree(graph: LilMatrix, root: int) -> LilMatrix:
    dfs = DepthFirstSearch(graph)
    res = LilMatrix.empty(len(graph))
    for now in dfs.pre_order(root):
        for dest, weight in graph[now]:
            if dest != dfs.prev[now]:
                res.add_edge(now, dest, weight)
    return res

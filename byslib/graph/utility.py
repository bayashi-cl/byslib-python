from typing import List, Tuple


from .edge import AdjacencyList, Edge
from .depth_first_search import DepthFirstSearch

SSSPResult = Tuple[List[int], List[int]]


def restore_path(prev: List[int], to: int) -> List[int]:
    res = []
    while to != -1:
        res.append(to)
        to = prev[to]
    return res[::-1]


def rooted_tree(graph: AdjacencyList, root: int) -> AdjacencyList:
    dfs = DepthFirstSearch(graph)
    res = AdjacencyList.init(len(graph))
    for now in dfs.pre_order(root):
        for nxt in graph[now]:
            if nxt.dest != dfs.prev[now]:
                res.add_edge(nxt.src, nxt.dest, nxt.weight)
    return res

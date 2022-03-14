# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path
from byslib.core.const import IINF
from byslib.core.fastio import sinput
from byslib.graph.dijkstra import dijkstra
from byslib.graph.edge import AdjacencyList
from byslib.graph.utility import restore_path


def main() -> None:
    n, m, s, t = map(int, sinput().split())
    graph = AdjacencyList.init(n)
    for _ in range(m):
        a, b, c = map(int, sinput().split())
        graph.add_edge(a, b, c)

    cost, prev = dijkstra(graph, s)
    if cost[t] == IINF:
        print(-1)
    else:
        path = restore_path(prev, t)
        y = len(path) - 1
        print(cost[t], y)
        for i in range(y):
            print(path[i], path[i + 1])


if __name__ == "__main__":
    main()

# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path
from byslib.core import sinput, IINF
from byslib.graph.edge import AdjacencyList
from byslib.graph.dijkstra import dijkstra


def main() -> None:
    n, m, s, t = map(int, sinput().split())
    graph = AdjacencyList(n, m)
    for _ in range(m):
        a, b, c = map(int, sinput().split())
        graph.add_edge(a, b, c)

    res = dijkstra(graph, s)
    if res.cost[t] == IINF:
        print(-1)
    else:
        path = res.path(t)
        y = len(path) - 1
        print(res.cost[t], y)
        for i in range(y):
            print(path[i], path[i + 1])


if __name__ == "__main__":
    main()

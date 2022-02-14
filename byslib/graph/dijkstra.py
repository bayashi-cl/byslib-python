"""
https://judge.yosupo.jp/problem/shortest_path
"""

# region template
import sys
import typing

sys.setrecursionlimit(10 ** 6)
Vec = typing.List[int]
VecVec = typing.List[Vec]
sinput: typing.Callable[..., str] = sys.stdin.readline
MOD: int = 1000000007
INF: float = float("Inf")
IINF: int = sys.maxsize
# endregion


class Dijkstra:
    """ダイクストラ法による最短経路探索
    import heapq
    * O(N + M * logN)
    """

    # 隣接グラフ(cost, node)
    Edge = typing.Tuple[float, int]
    Adj = typing.List[typing.List[Edge]]
    INF = float("inf")
    sinput = sys.stdin.readline

    def __init__(self, graph: Adj):
        self.graph = graph
        self.n_node = len(graph)

    def search(self, start: int) -> typing.List[float]:
        import heapq

        self.cost = [Dijkstra.INF] * self.n_node
        self.cost[start] = 0
        que: typing.List[Dijkstra.Edge] = [(0, start)]
        self.prev = [-1] * self.n_node

        while que:
            top_cost, top_node = heapq.heappop(que)

            if top_cost > self.cost[top_node]:
                continue

            for adj_cost, adj_node in self.graph[top_node]:
                temp_cost = self.cost[top_node] + adj_cost

                if temp_cost < self.cost[adj_node]:
                    self.cost[adj_node] = temp_cost
                    self.prev[adj_node] = top_node
                    heapq.heappush(que, (temp_cost, adj_node))

        return self.cost

    def path_finder(self, to: int) -> typing.List[int]:
        assert to <= self.n_node

        path = []
        while to != -1:
            path.append(to)
            to = self.prev[to]

        return path[::-1]

    @classmethod
    def read(
        cls, n_node: int, n_edge: int, direction: bool = False, index: int = 1
    ) -> "Dijkstra":
        """
        (from, to, cost) の形式で標準入力から読み取り
        """

        adj: Dijkstra.Adj = [[] for _ in range(n_node)]

        for _ in range(n_edge):
            f, t, c = map(int, cls.sinput().split())
            f -= index
            t -= index

            adj[f].append((c, t))
            if not direction:
                adj[t].append((c, f))

        return cls(adj)


def main() -> None:
    n, m, s, t = map(int, sinput().split())
    dij = Dijkstra.read(n, m, direction=True, index=0)
    dij.search(s)

    if dij.cost[t] == INF:
        print(-1)
    else:
        path = dij.path_finder(t)
        print(dij.cost[t], len(path) - 1)
        for i in range(1, len(path)):
            print(path[i - 1], path[i])


if __name__ == "__main__":
    main()

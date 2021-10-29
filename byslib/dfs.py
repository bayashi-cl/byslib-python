# region template
import sys
import typing
from collections import deque

sys.setrecursionlimit(10 ** 9)
Vec = typing.List[int]
VecVec = typing.List[Vec]
sinput: typing.Callable[..., str] = sys.stdin.readline
MOD: int = 1000000007
INF: float = float("Inf")
IINF: int = sys.maxsize
# endregion


class DepthFirstSearchM:
    """
    from collections import deque
    """

    def __init__(self, graph: VecVec):
        self.graph = graph
        self.pre_order: Vec = []
        self.seen = [False] * len(graph)
        self.post_orfer: Vec = []

    def search(self, start: int):
        que = deque([start])
        self.seen[start] = True

        while que:
            now = que.pop()
            self.pre_order.append(now)

            for to in self.graph[now]:
                if self.seen[to]:
                    continue
                self.seen[to] = True
                que.append(to)

            self.post_orfer.append(now)


class DepthFirstSearch:
    def __init__(self, graph: VecVec):
        self.graph = graph
        self.pre_order: Vec = []
        self.seen = [False] * len(graph)
        self.post_orfer: Vec = []

    def search(self, now: int):
        self.seen[now] = True
        self.pre_order.append(now)
        for to in self.graph[now]:
            if self.seen[to]:
                continue
            self.search(to)
        self.post_orfer.append(now)


def main() -> None:
    pass


if __name__ == "__main__":
    main()

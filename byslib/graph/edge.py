from typing import List, Tuple


class Edge:
    src: int
    dest: int
    weight: int

    def __init__(self, src: int, dest: int, weight: int = 1) -> None:
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self) -> str:
        return f"{{{self.src} -> {self.dest}: {self.weight}}}"


class AdjacencyList:
    n_node: int
    n_edge: int
    buf: List[Edge]
    data: List[Edge]
    index: List[int]

    def __init__(self, n_node: int, n_edge: int) -> None:
        self.n_node = n_node
        self.n_edge = n_edge
        self.index = [0] * (n_node + 1)
        self.data = [Edge(-1, -1)] * n_edge
        self.buf = []

    def __len__(self) -> int:
        return self.n_node

    def __getitem__(self, key: int) -> List[Edge]:
        return self.data[self.index[key] : self.index[key + 1]]

    def add_edge(self, src: int, dest: int, weight: int = 1) -> None:
        self.index[src] += 1
        self.buf.append(Edge(src, dest, weight))
        if len(self.buf) == self.n_edge:
            self.build()

    def build(self) -> None:
        for i in range(1, self.n_node + 1):
            self.index[i] += self.index[i - 1]
        for e in self.buf:
            self.index[e.src] -= 1
            self.data[self.index[e.src]] = e

from dataclasses import dataclass
import typing


@dataclass
class Edge:
    arr: int


@dataclass
class WEdge(Edge):
    arr: int
    cost: int


@dataclass
class DeWEdge(WEdge):
    dep: int
    arr: int
    cost: int

    def __lt__(self, rh: "DeWEdge") -> bool:
        if self.cost is None or rh.cost is None:
            raise ValueError
        return self.cost < rh.cost


if __name__ == "__main__":
    print(Edge(4))
    e = []
    e.append(DeWEdge(3, 1, 4))
    e.append(DeWEdge(1, 5, 1))
    print(e)
    e.sort()
    print(e)

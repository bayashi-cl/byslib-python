# @title Adjacency List
from typing import List, Tuple


class LilMatrix(List[List[Tuple[int, int]]]):
    """List in List Matrix"""

    @classmethod
    def empty(cls, n: int) -> "LilMatrix":
        return cls([[] for _ in range(n)])

    def add_edge(self, src: int, dest: int, weight: int = 1) -> None:
        self[src].append((dest, weight))

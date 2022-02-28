from typing import List
from itertools import accumulate


class CumulativeSum:
    def __init__(self, n: int) -> None:
        self.data = [0] * (n + 1)

    def update(self, i: int, x: int) -> None:
        self.data[i + 1] = x

    def add(self, i: int, x: int) -> None:
        self.data[i + 1] += x

    def construct(self) -> None:
        self.data = list(accumulate(self.data))

    def sum(self, l: int, r: int) -> int:
        return self.data[r] - self.data[l]

    @classmethod
    def from_list(cls, l: List[int]) -> "CumulativeSum":
        n = len(l)
        res = cls(n)
        res.data[1:] = l
        return res

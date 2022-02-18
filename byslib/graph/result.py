from typing import List

from byslib.core import IINF


class SSSPResult:
    source: int
    cost: List[int]
    prev: List[int]

    def __init__(self, n: int, source) -> None:
        self.source = source
        self.cost = [IINF] * n
        self.prev = [-1] * n

    def path(self, to: int) -> List[int]:
        res = []
        while to != -1:
            res.append(to)
            to = self.prev[to]
        return res[::-1]

# @title Bynary Indexed Tree
from typing import List


class BinaryIndexedTree:
    r"""Bynary Indexed Tree (Fenwick Tree)

    Notes
    -----
    Time complexity

    * Build : :math:`O(N)`
    * Point_append : :math:`O(\log(N))`
    * Fold : :math:`O(\log(N))`

    References
    ----------
    ..[1] 🐜 p.159
    ..[2] https://scrapbox.io/data-structures/Fenwick_Tree

    Examples
    --------
    >>> bit = BinaryIndexedTree.zeros(5)
    >>> bit.point_append(0, 3)
    >>> bit.point_append(2, -2)
    >>> print(bit.fold(1, 4))
    -2
    """

    def __init__(self, array: List[int]) -> None:
        self.size = len(array)
        self.data = [0] * (self.size + 1)
        for i, ai in enumerate(array):
            self.point_append(i, ai)

    def point_append(self, index: int, value: int) -> None:
        index += 1
        while index <= self.size:
            self.data[index] += value
            index += index & -index

    def prefix_fold(self, right: int) -> int:
        s = 0
        while right > 0:
            s += self.data[right]
            right -= right & -right
        return s

    def fold(self, left: int, right: int) -> int:
        return self.prefix_fold(right) - self.prefix_fold(left)

    @classmethod
    def zeros(cls, n: int) -> "BinaryIndexedTree":
        return cls([0] * n)

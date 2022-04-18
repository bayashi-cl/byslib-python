# @title Cumulative Sum
from itertools import chain
from typing import List


class CumulativeSum:
    """Cumulative Sum
    Notes
    -----
    Get sum of semi-open interval [left, right)

    Time complexity

    * Build : :math:`O(N)`
    * fold : :math:`O(1)`

    Examples
    --------
    >>> cs = CumulativeSum([3, 1, 4, 1, 5])
    >>> print(cs.fold(0, 3))
    8
    """

    def __init__(self, data: List[int]) -> None:
        n = len(data)
        self.__data = [0] * (n + 1)
        for i in range(n):
            self.__data[i + 1] = self.__data[i] + data[i]

    def fold(self, left: int, right: int) -> int:
        return self.__data[right] - self.__data[left]


class CumulativeSum2D:
    """Cumulative Sum 2D
    Notes
    -----
    Get sum of range

    Time complexity

    * Build : :math:`O(N * M)`
    * fold : :math:`O(1)`

    Examples
    --------
    >>> cs = CumulativeSum([3, 1, 4, 1, 5])
    >>> print(cs.fold(0, 3))
    8
    """

    def __init__(self, data: List[List[int]]) -> None:
        n = len(data)
        m = len(data[0])
        self.__data = [[0] + row for row in chain([[0] * m], data)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.__data[i][j] += (
                    self.__data[i][j - 1]
                    + self.__data[i - 1][j]
                    - self.__data[i - 1][j - 1]
                )

    def fold(self, up: int, left: int, down: int, right: int) -> int:
        return (
            self.__data[down][right]
            - self.__data[up][right]
            - self.__data[down][left]
            + self.__data[up][left]
        )

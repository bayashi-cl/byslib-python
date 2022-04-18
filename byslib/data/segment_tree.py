# @title Segment Tree
from typing import Callable, Generic, List, TypeVar

T = TypeVar("T")


class SegmentTree(Generic[T]):
    r"""Segment Tree

    Parameters
    ----------
    Generic[T]
        Set type of Monoid

    Notes
    -----
    Time complexity

    * build : :math:`O(N)`
    * Point set : :math:`O(\log(N))`
    * Range fold : :math:`O(\log(N))`

    References
    ----------
    ..[1] 🐜 p.153
    ..[2] https://scrapbox.io/data-structures/Segment_Tree
    ..[3] https://ikatakos.com/pot/programming_algorithm/data_structure/segment_tree

    Examples
    --------
    >>> seg = SegmentTree(max, 0, [1] * 10)
    >>> seg.set(3, 4)
    >>> seg.set(8, 9)
    >>> print(seg.fold(0,5))
    4
    >>> len(seg)
    10
    >>> print(seg.fold_all())
    9
    >>> print(seg[3])
    4
    """

    def __init__(
        self, operation: Callable[[T, T], T], identity: T, array: List[T]
    ) -> None:
        """build

        Parameters
        ----------
        operation
            Binary operation of Monoid
        identity
            Identity of Monoid
        array
            Init array
        """
        self.__operation = operation
        self.__identity = identity
        self.__n = len(array)
        self.__n_leaf = 1 << (self.__n - 1).bit_length()
        self.__data = [self.__identity] * (self.__n_leaf * 2)
        self.__data[self.__n_leaf : self.__n_leaf + self.__n] = array
        for i in range(self.__n_leaf - 1, 0, -1):
            self.__data[i] = self.__operation(
                self.__data[i * 2], self.__data[i * 2 + 1]
            )

    def set(self, index: int, value: T) -> None:
        index += self.__n_leaf
        self.__data[index] = value
        index >>= 1
        while index > 0:
            self.__data[index] = self.__operation(
                self.__data[index * 2], self.__data[index * 2 + 1]
            )
            index >>= 1

    def fold(self, left: int, right: int) -> T:
        left_fold = self.__identity
        right_fold = self.__identity
        left += self.__n_leaf
        right += self.__n_leaf
        while left < right:
            if left & 1:
                left_fold = self.__operation(left_fold, self.__data[left])
                left += 1
            if right & 1:
                right -= 1
                right_fold = self.__operation(self.__data[right], right_fold)
            left >>= 1
            right >>= 1
        return self.__operation(left_fold, right_fold)

    def fold_all(self) -> T:
        return self.__data[1]

    def __getitem__(self, key: int) -> T:
        return self.__data[key + self.__n_leaf]

    def __len__(self) -> int:
        return self.__n

    @classmethod
    def zeros(cls, op: Callable[[T, T], T], ident: T, n: int) -> "SegmentTree":
        return cls(op, ident, [ident] * n)

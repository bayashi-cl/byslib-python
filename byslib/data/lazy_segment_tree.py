# @brief Lazy Segment Tree
from typing import Callable, Generic, Sequence, TypeVar

S = TypeVar("S")
F = TypeVar("F")


class LazySegmentTree(Generic[S, F]):
    r"""Lazy Segment Tree

    Parameters
    ----------
    Generic[T]
        Set type of Monoid
    Generic[F]
        Set type of Operator Monoid

    Notes
    -----
    Time complexity

    * build : :math:`O(N)`
    * Point set : :math:`O(\log(N))`
    * Range fold : :math:`O(\log(N))`
    * Range effect : :math:`O(\log(N))`

    References
    ----------
    ..[1] https://ikatakos.com/pot/programming_algorithm/data_structure/segment_tree/lazy_segment_tree
    ..[2] https://scrapbox.io/data-structures/Lazy_Segment_Tree

    Examples
    --------
    """
    __slots__ = (
        "_op",
        "_ident_S",
        "_mapping",
        "_composition",
        "_ident_F",
        "_n",
        "_logsize",
        "_n_leaf",
        "_data",
        "_lazy",
    )

    def __init__(
        self,
        op: Callable[[S, S], S],
        ident_S: S,
        mapping: Callable[[F, S], S],
        composition: Callable[[F, F], F],
        ident_F: F,
        val: Sequence[S],
    ) -> None:
        """build

        Parameters
        ----------
        op
            Binary Operation of Monoid
        ident_S
            identity of Monoid
        mapping
            Effect from Operator monoid to Monoid
        composition
            Binary Operation of Operator Monoid
        ident_F
            identity of Operator Monoid
        val
            init value
        """
        self._op = op
        self._ident_S = ident_S
        self._mapping = mapping
        self._composition = composition
        self._ident_F = ident_F

        self._n = len(val)
        self._logsize = (self._n - 1).bit_length()
        self._n_leaf = 1 << self._logsize
        self._data = [ident_S for _ in range(2 * self._n_leaf)]
        self._data[self._n_leaf : self._n_leaf + self._n] = val
        self._lazy = [ident_F for _ in range(self._n_leaf)]
        for i in range(self._n_leaf - 1, 0, -1):
            self._update(i)

    @classmethod
    def idents(
        cls,
        op: Callable[[S, S], S],
        ident_S: S,
        mapping: Callable[[F, S], S],
        composition: Callable[[F, F], F],
        ident_F: F,
        n: int,
    ) -> "LazySegmentTree":
        return cls(op, ident_S, mapping, composition, ident_F, [ident_S] * n)

    def update(self, p: int, x: S) -> None:
        assert 0 <= p < self._n
        p += self._n_leaf
        for i in range(self._logsize, 0, -1):
            self._push(p >> i)
        self._data[p] = x
        for i in range(1, self._logsize + 1):
            self._update(p >> i)

    def query(self, l: int, r: int) -> S:
        assert 0 <= l <= r <= self._n
        if l == r:
            return self._ident_S
        l += self._n_leaf
        r += self._n_leaf

        (*indices,) = self._get_indices(l, r)
        for i in reversed(indices):
            self._push(i)

        left = self._ident_S
        right = self._ident_S
        while l < r:
            if l & 1:
                left = self._op(left, self._data[l])
                l += 1
            if r & 1:
                r -= 1
                right = self._op(self._data[r], right)
            l >>= 1
            r >>= 1

        return self._op(left, right)

    def query_all(self) -> S:
        return self._data[1]

    def apply_point(self, p: int, f: F) -> None:
        assert 0 <= p < self._n
        p += self._n_leaf
        for i in range(self._logsize, 0, -1):
            self._push(p >> i)
        self._data[p] = self._mapping(f, self._data[p])
        for i in range(1, self._logsize + 1):
            self._update(p >> i)

    def apply(self, l: int, r: int, f: F) -> None:
        assert 0 <= l <= r <= self._n
        if l == r:
            return
        l += self._n_leaf
        r += self._n_leaf

        (*indices,) = self._get_indices(l, r)
        for i in reversed(indices):
            self._push(i)

        l2 = l
        r2 = r
        while l2 < r2:
            if l2 & 1:
                self._apply(l2, f)
                l2 += 1
            if r2 & 1:
                r2 -= 1
                self._apply(r2, f)
            l2 >>= 1
            r2 >>= 1

        for i in indices:
            self._update(i)

    def bisect_from_left(self, l: int, fn: Callable[[S], bool]) -> int:
        raise NotImplementedError

    def bisect_from_right(self, r: int, fn: Callable[[S], bool]) -> int:
        raise NotImplementedError

    def __getitem__(self, p: int) -> S:
        assert 0 <= p < self._n
        p += self._n_leaf
        for i in range(self._logsize, 0, -1):
            self._push(p >> i)
        return self._data[p]

    def __len__(self) -> int:
        return self._n

    def _get_indices(self, l, r):
        l0 = (l // (l & -l)) >> 1
        r0 = (r // (r & -r)) >> 1
        while l0 != r0:
            if l0 > r0:
                yield l0
                l0 >>= 1
            else:
                yield r0
                r0 >>= 1
        while l0:
            yield l0
            l0 >>= 1

    def _update(self, k: int) -> None:
        self._data[k] = self._op(self._data[k * 2], self._data[k * 2 + 1])

    def _apply(self, k: int, f: F) -> None:
        self._data[k] = self._mapping(f, self._data[k])
        if k < self._n_leaf:
            self._lazy[k] = self._composition(f, self._lazy[k])

    def _push(self, k: int) -> None:
        self._apply(2 * k, self._lazy[k])
        self._apply(2 * k + 1, self._lazy[k])
        self._lazy[k] = self._ident_F

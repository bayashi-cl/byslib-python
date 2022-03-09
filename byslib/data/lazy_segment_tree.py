from typing import Callable, Generic, Sequence, TypeVar

S = TypeVar("S")
F = TypeVar("F")


class LazySegmentTree(Generic[S, F]):
    """Lazy Segment Tree

    Args:
        S: モノイドの型
        F: 写像の型
    """

    __slots__ = (
        "op",
        "ident_S",
        "mapping",
        "composition",
        "ident_F",
        "n",
        "logsize",
        "n_leaf",
        "data",
        "lazy",
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
        """コンストラクタ

        Args:
            op (Callable[[S, S], S]): 演算 S * S -> S
            ident_S (S): S の単位元
            mapping (Callable[[F, S, int], S]): 作用 f(F, S, width) -> S
            composition (Callable[[F, F], F]): 写像の合成 f(g(x)) -> F
            ident_F (F): 恒等写像
            val (Sequence[S]): もととなる配列
        """
        self.op = op
        self.ident_S = ident_S
        self.mapping = mapping
        self.composition = composition
        self.ident_F = ident_F

        self.n = len(val)
        self.logsize = (self.n - 1).bit_length()
        self.n_leaf = 1 << self.logsize
        self.data = [ident_S for _ in range(2 * self.n_leaf)]
        self.data[self.n_leaf : self.n_leaf + self.n] = val
        self.lazy = [ident_F for _ in range(self.n_leaf)]
        for i in range(self.n_leaf - 1, 0, -1):
            self.__update(i)

    @classmethod
    def init(
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
        assert 0 <= p < self.n
        p += self.n_leaf
        for i in range(self.logsize, 0, -1):
            self.__push(p >> i)
        self.data[p] = x
        for i in range(1, self.logsize + 1):
            self.__update(p >> i)

    def get(self, p: int) -> S:
        assert 0 <= p < self.n
        p += self.n_leaf
        for i in range(self.logsize, 0, -1):
            self.__push(p >> i)
        return self.data[p]

    def query(self, l: int, r: int) -> S:
        assert 0 <= l <= r <= self.n
        if l == r:
            return self.ident_S
        l += self.n_leaf
        r += self.n_leaf

        (*indices,) = self.__get_indices(l, r)
        for i in reversed(indices):
            self.__push(i)

        left = self.ident_S
        right = self.ident_S
        while l < r:
            if l & 1:
                left = self.op(left, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                right = self.op(self.data[r], right)
            l >>= 1
            r >>= 1

        return self.op(left, right)

    def query_all(self) -> S:
        return self.data[1]

    def apply_point(self, p: int, f: F) -> None:
        assert 0 <= p < self.n
        p += self.n_leaf
        for i in range(self.logsize, 0, -1):
            self.__push(p >> i)
        self.data[p] = self.mapping(f, self.data[p])
        for i in range(1, self.logsize + 1):
            self.__update(p >> i)

    def apply(self, l: int, r: int, f: F) -> None:
        assert 0 <= l <= r <= self.n
        if l == r:
            return
        l += self.n_leaf
        r += self.n_leaf

        (*indices,) = self.__get_indices(l, r)
        for i in reversed(indices):
            self.__push(i)

        l2 = l
        r2 = r
        while l2 < r2:
            if l2 & 1:
                self.__apply(l2, f)
                l2 += 1
            if r2 & 1:
                r2 -= 1
                self.__apply(r2, f)
            l2 >>= 1
            r2 >>= 1

        for i in indices:
            self.__update(i)

    def bisect_from_left(self, l: int, fn: Callable[[S], bool]) -> int:
        raise NotImplementedError

    def bisect_from_right(self, r: int, fn: Callable[[S], bool]) -> int:
        raise NotImplementedError

    def __get_indices(self, l, r):
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

    def __update(self, k: int) -> None:
        self.data[k] = self.op(self.data[k * 2], self.data[k * 2 + 1])

    def __apply(self, k: int, f: F) -> None:
        self.data[k] = self.mapping(f, self.data[k])
        if k < self.n_leaf:
            self.lazy[k] = self.composition(f, self.lazy[k])

    def __push(self, k: int) -> None:
        self.__apply(2 * k, self.lazy[k])
        self.__apply(2 * k + 1, self.lazy[k])
        self.lazy[k] = self.ident_F

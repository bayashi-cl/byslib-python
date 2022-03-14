from typing import Callable, Generic, List, TypeVar

T = TypeVar("T")


class SegmentTree(Generic[T]):
    def __init__(self, op: Callable[[T, T], T], ident: T, val: List[T]) -> None:
        self.op = op
        self.ident = ident
        self.n = len(val)
        self.n_leaf = 1 << (self.n - 1).bit_length()
        self.data = [self.ident] * (self.n_leaf * 2)
        self.data[self.n_leaf : self.n_leaf + self.n] = val
        for i in range(self.n_leaf - 1, 0, -1):
            self.data[i] = self.op(self.data[i * 2], self.data[i * 2 + 1])

    def update(self, i: int, v: T) -> None:
        i += self.n_leaf
        self.data[i] = v
        i >>= 1
        while i > 0:
            self.data[i] = self.op(self.data[i * 2], self.data[i * 2 + 1])
            i >>= 1

    def query(self, l: int, r: int) -> T:
        left = self.ident
        right = self.ident
        l += self.n_leaf
        r += self.n_leaf
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

    def query_all(self) -> T:
        return self.data[1]

    def __getitem__(self, key: int) -> T:
        return self.data[key + self.n_leaf]

    @classmethod
    def empty(cls, op: Callable[[T, T], T], ident: T, n: int) -> "SegmentTree":
        return cls(op, ident, [ident] * n)

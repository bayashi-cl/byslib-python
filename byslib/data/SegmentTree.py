import typing


class SegmentTree:
    """非再帰セグメント木
    0-index
    """

    def __init__(
        self,
        val: typing.Union[typing.List[int], typing.List[float]],
        func: typing.Callable,
        indent: float = 0,
    ) -> None:
        import operator

        self.n = len(val)
        self.n_leaf = 1 << (self.n - 1).bit_length()

        assert self.n > 0
        self.inf = float("inf")

        self.func = func
        if self.func == max:
            self.ident = -self.inf
        elif self.func == min:
            self.ident = self.inf
        elif self.func == operator.add:
            self.ident = 0
        elif self.func == operator.mul:
            self.ident = 1
        elif self.func == operator.xor:
            self.ident = 0
        else:
            self.ident = indent

        self.tree = [self.ident] * (2 * self.n_leaf)
        self.tree[self.n_leaf : self.n_leaf + self.n] = val
        for i in range(self.n_leaf - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, l: int, r: int) -> float:
        l += self.n_leaf
        r += self.n_leaf
        res = self.ident
        while l < r:
            if l & 1:
                res = self.func(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.func(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res

    def query_all(self) -> float:
        return self.tree[1]

    def add(self, i: int, val: float) -> None:
        i += self.n_leaf
        self.tree[i] = self.func(self.tree[i], val)
        while i > 0:
            i >>= 1
            self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, i: int, val: float) -> None:
        i += self.n_leaf
        self.tree[i] = val
        while i > 0:
            i >>= 1
            self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])

    @property
    def leaf(self):
        return self.tree[self.n_leaf : self.n_leaf + self.n]


class LazySegmentTree(SegmentTree):
    """遅延評価セグメント木"""

    def __init__(self, val: typing.List[float], func: typing.Callable):
        super().__init__(val, func)
        self.lazy = [None] * (2 * self.n_leaf)

    def gindex(self, l: int, r: int) -> typing.Generator[float, None, None]:
        l += self.n_leaf
        r += self.n_leaf
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()
        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self, ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.tree[2 * i] = v
            self.tree[2 * i + 1] = v
            self.lazy[i] = None

    def update(self, l, r, x):
        (*ids,) = self.gindex(l, r)
        self.propagates(ids)
        l += self.n_leaf
        r += self.n_leaf
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.tree[r - 1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        (*ids,) = self.gindex(l, r)
        self.propagates(ids)

        res = self.ident

        l += self.n_leaf
        r += self.n_leaf
        while l < r:
            if l & 1:
                res = self.func(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.func(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res
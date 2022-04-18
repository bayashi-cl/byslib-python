---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/data/lazysegtree/range_update_query.test.py
    title: tests/data/lazysegtree/range_update_query.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    document_title: Lazy Segment Tree
    links:
    - https://ikatakos.com/pot/programming_algorithm/data_structure/segment_tree/lazy_segment_tree
    - https://scrapbox.io/data-structures/Lazy_Segment_Tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @brief Lazy Segment Tree\nfrom typing import Callable, Generic, Sequence,\
    \ TypeVar\n\nS = TypeVar(\"S\")\nF = TypeVar(\"F\")\n\n\nclass LazySegmentTree(Generic[S,\
    \ F]):\n    r\"\"\"Lazy Segment Tree\n\n    Parameters\n    ----------\n    Generic[T]\n\
    \        Set type of Monoid\n    Generic[F]\n        Set type of Operator Monoid\n\
    \n    Notes\n    -----\n    Time complexity\n\n    * build : :math:`O(N)`\n  \
    \  * Point set : :math:`O(\\log(N))`\n    * Range fold : :math:`O(\\log(N))`\n\
    \    * Range effect : :math:`O(\\log(N))`\n\n    References\n    ----------\n\
    \    ..[1] https://ikatakos.com/pot/programming_algorithm/data_structure/segment_tree/lazy_segment_tree\n\
    \    ..[2] https://scrapbox.io/data-structures/Lazy_Segment_Tree\n\n    Examples\n\
    \    --------\n    \"\"\"\n    __slots__ = (\n        \"_op\",\n        \"_ident_S\"\
    ,\n        \"_mapping\",\n        \"_composition\",\n        \"_ident_F\",\n \
    \       \"_n\",\n        \"_logsize\",\n        \"_n_leaf\",\n        \"_data\"\
    ,\n        \"_lazy\",\n    )\n\n    def __init__(\n        self,\n        op:\
    \ Callable[[S, S], S],\n        ident_S: S,\n        mapping: Callable[[F, S],\
    \ S],\n        composition: Callable[[F, F], F],\n        ident_F: F,\n      \
    \  val: Sequence[S],\n    ) -> None:\n        \"\"\"build\n\n        Parameters\n\
    \        ----------\n        op\n            Binary Operation of Monoid\n    \
    \    ident_S\n            identity of Monoid\n        mapping\n            Effect\
    \ from Operator monoid to Monoid\n        composition\n            Binary Operation\
    \ of Operator Monoid\n        ident_F\n            identity of Operator Monoid\n\
    \        val\n            init value\n        \"\"\"\n        self._op = op\n\
    \        self._ident_S = ident_S\n        self._mapping = mapping\n        self._composition\
    \ = composition\n        self._ident_F = ident_F\n\n        self._n = len(val)\n\
    \        self._logsize = (self._n - 1).bit_length()\n        self._n_leaf = 1\
    \ << self._logsize\n        self._data = [ident_S for _ in range(2 * self._n_leaf)]\n\
    \        self._data[self._n_leaf : self._n_leaf + self._n] = val\n        self._lazy\
    \ = [ident_F for _ in range(self._n_leaf)]\n        for i in range(self._n_leaf\
    \ - 1, 0, -1):\n            self._update(i)\n\n    @classmethod\n    def idents(\n\
    \        cls,\n        op: Callable[[S, S], S],\n        ident_S: S,\n       \
    \ mapping: Callable[[F, S], S],\n        composition: Callable[[F, F], F],\n \
    \       ident_F: F,\n        n: int,\n    ) -> \"LazySegmentTree\":\n        return\
    \ cls(op, ident_S, mapping, composition, ident_F, [ident_S] * n)\n\n    def update(self,\
    \ p: int, x: S) -> None:\n        assert 0 <= p < self._n\n        p += self._n_leaf\n\
    \        for i in range(self._logsize, 0, -1):\n            self._push(p >> i)\n\
    \        self._data[p] = x\n        for i in range(1, self._logsize + 1):\n  \
    \          self._update(p >> i)\n\n    def query(self, l: int, r: int) -> S:\n\
    \        assert 0 <= l <= r <= self._n\n        if l == r:\n            return\
    \ self._ident_S\n        l += self._n_leaf\n        r += self._n_leaf\n\n    \
    \    (*indices,) = self._get_indices(l, r)\n        for i in reversed(indices):\n\
    \            self._push(i)\n\n        left = self._ident_S\n        right = self._ident_S\n\
    \        while l < r:\n            if l & 1:\n                left = self._op(left,\
    \ self._data[l])\n                l += 1\n            if r & 1:\n            \
    \    r -= 1\n                right = self._op(self._data[r], right)\n        \
    \    l >>= 1\n            r >>= 1\n\n        return self._op(left, right)\n\n\
    \    def query_all(self) -> S:\n        return self._data[1]\n\n    def apply_point(self,\
    \ p: int, f: F) -> None:\n        assert 0 <= p < self._n\n        p += self._n_leaf\n\
    \        for i in range(self._logsize, 0, -1):\n            self._push(p >> i)\n\
    \        self._data[p] = self._mapping(f, self._data[p])\n        for i in range(1,\
    \ self._logsize + 1):\n            self._update(p >> i)\n\n    def apply(self,\
    \ l: int, r: int, f: F) -> None:\n        assert 0 <= l <= r <= self._n\n    \
    \    if l == r:\n            return\n        l += self._n_leaf\n        r += self._n_leaf\n\
    \n        (*indices,) = self._get_indices(l, r)\n        for i in reversed(indices):\n\
    \            self._push(i)\n\n        l2 = l\n        r2 = r\n        while l2\
    \ < r2:\n            if l2 & 1:\n                self._apply(l2, f)\n        \
    \        l2 += 1\n            if r2 & 1:\n                r2 -= 1\n          \
    \      self._apply(r2, f)\n            l2 >>= 1\n            r2 >>= 1\n\n    \
    \    for i in indices:\n            self._update(i)\n\n    def bisect_from_left(self,\
    \ l: int, fn: Callable[[S], bool]) -> int:\n        raise NotImplementedError\n\
    \n    def bisect_from_right(self, r: int, fn: Callable[[S], bool]) -> int:\n \
    \       raise NotImplementedError\n\n    def __getitem__(self, p: int) -> S:\n\
    \        assert 0 <= p < self._n\n        p += self._n_leaf\n        for i in\
    \ range(self._logsize, 0, -1):\n            self._push(p >> i)\n        return\
    \ self._data[p]\n\n    def __len__(self) -> int:\n        return self._n\n\n \
    \   def _get_indices(self, l, r):\n        l0 = (l // (l & -l)) >> 1\n       \
    \ r0 = (r // (r & -r)) >> 1\n        while l0 != r0:\n            if l0 > r0:\n\
    \                yield l0\n                l0 >>= 1\n            else:\n     \
    \           yield r0\n                r0 >>= 1\n        while l0:\n          \
    \  yield l0\n            l0 >>= 1\n\n    def _update(self, k: int) -> None:\n\
    \        self._data[k] = self._op(self._data[k * 2], self._data[k * 2 + 1])\n\n\
    \    def _apply(self, k: int, f: F) -> None:\n        self._data[k] = self._mapping(f,\
    \ self._data[k])\n        if k < self._n_leaf:\n            self._lazy[k] = self._composition(f,\
    \ self._lazy[k])\n\n    def _push(self, k: int) -> None:\n        self._apply(2\
    \ * k, self._lazy[k])\n        self._apply(2 * k + 1, self._lazy[k])\n       \
    \ self._lazy[k] = self._ident_F\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/data/lazy_segment_tree.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/data/lazysegtree/range_update_query.test.py
documentation_of: byslib/data/lazy_segment_tree.py
layout: document
redirect_from:
- /library/byslib/data/lazy_segment_tree.py
- /library/byslib/data/lazy_segment_tree.py.html
title: Lazy Segment Tree
---

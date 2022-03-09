---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/lazysegtree/range_update_query.test.py
    title: tests/lazysegtree/range_update_query.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable, Generic, Sequence, TypeVar\n\nS = TypeVar(\"\
    S\")\nF = TypeVar(\"F\")\n\n\nclass LazySegmentTree(Generic[S, F]):\n    \"\"\"\
    Lazy Segment Tree\n\n    Args:\n        S: \u30E2\u30CE\u30A4\u30C9\u306E\u578B\
    \n        F: \u5199\u50CF\u306E\u578B\n    \"\"\"\n\n    __slots__ = (\n     \
    \   \"op\",\n        \"ident_S\",\n        \"mapping\",\n        \"composition\"\
    ,\n        \"ident_F\",\n        \"n\",\n        \"logsize\",\n        \"n_leaf\"\
    ,\n        \"data\",\n        \"lazy\",\n    )\n\n    def __init__(\n        self,\n\
    \        op: Callable[[S, S], S],\n        ident_S: S,\n        mapping: Callable[[F,\
    \ S], S],\n        composition: Callable[[F, F], F],\n        ident_F: F,\n  \
    \      val: Sequence[S],\n    ) -> None:\n        \"\"\"\u30B3\u30F3\u30B9\u30C8\
    \u30E9\u30AF\u30BF\n\n        Args:\n            op (Callable[[S, S], S]): \u6F14\
    \u7B97 S * S -> S\n            ident_S (S): S \u306E\u5358\u4F4D\u5143\n     \
    \       mapping (Callable[[F, S, int], S]): \u4F5C\u7528 f(F, S, width) -> S\n\
    \            composition (Callable[[F, F], F]): \u5199\u50CF\u306E\u5408\u6210\
    \ f(g(x)) -> F\n            ident_F (F): \u6052\u7B49\u5199\u50CF\n          \
    \  val (Sequence[S]): \u3082\u3068\u3068\u306A\u308B\u914D\u5217\n        \"\"\
    \"\n        self.op = op\n        self.ident_S = ident_S\n        self.mapping\
    \ = mapping\n        self.composition = composition\n        self.ident_F = ident_F\n\
    \n        self.n = len(val)\n        self.logsize = (self.n - 1).bit_length()\n\
    \        self.n_leaf = 1 << self.logsize\n        self.data = [ident_S for _ in\
    \ range(2 * self.n_leaf)]\n        self.data[self.n_leaf : self.n_leaf + self.n]\
    \ = val\n        self.lazy = [ident_F for _ in range(self.n_leaf)]\n        for\
    \ i in range(self.n_leaf - 1, 0, -1):\n            self.__update(i)\n\n    @classmethod\n\
    \    def init(\n        cls,\n        op: Callable[[S, S], S],\n        ident_S:\
    \ S,\n        mapping: Callable[[F, S], S],\n        composition: Callable[[F,\
    \ F], F],\n        ident_F: F,\n        n: int,\n    ) -> \"LazySegmentTree\"\
    :\n        return cls(op, ident_S, mapping, composition, ident_F, [ident_S] *\
    \ n)\n\n    def update(self, p: int, x: S) -> None:\n        assert 0 <= p < self.n\n\
    \        p += self.n_leaf\n        for i in range(self.logsize, 0, -1):\n    \
    \        self.__push(p >> i)\n        self.data[p] = x\n        for i in range(1,\
    \ self.logsize + 1):\n            self.__update(p >> i)\n\n    def get(self, p:\
    \ int) -> S:\n        assert 0 <= p < self.n\n        p += self.n_leaf\n     \
    \   for i in range(self.logsize, 0, -1):\n            self.__push(p >> i)\n  \
    \      return self.data[p]\n\n    def query(self, l: int, r: int) -> S:\n    \
    \    assert 0 <= l <= r <= self.n\n        if l == r:\n            return self.ident_S\n\
    \        l += self.n_leaf\n        r += self.n_leaf\n\n        (*indices,) = self.__get_indices(l,\
    \ r)\n        for i in reversed(indices):\n            self.__push(i)\n\n    \
    \    left = self.ident_S\n        right = self.ident_S\n        while l < r:\n\
    \            if l & 1:\n                left = self.op(left, self.data[l])\n \
    \               l += 1\n            if r & 1:\n                r -= 1\n      \
    \          right = self.op(self.data[r], right)\n            l >>= 1\n       \
    \     r >>= 1\n\n        return self.op(left, right)\n\n    def query_all(self)\
    \ -> S:\n        return self.data[1]\n\n    def apply_point(self, p: int, f: F)\
    \ -> None:\n        assert 0 <= p < self.n\n        p += self.n_leaf\n       \
    \ for i in range(self.logsize, 0, -1):\n            self.__push(p >> i)\n    \
    \    self.data[p] = self.mapping(f, self.data[p])\n        for i in range(1, self.logsize\
    \ + 1):\n            self.__update(p >> i)\n\n    def apply(self, l: int, r: int,\
    \ f: F) -> None:\n        assert 0 <= l <= r <= self.n\n        if l == r:\n \
    \           return\n        l += self.n_leaf\n        r += self.n_leaf\n\n   \
    \     (*indices,) = self.__get_indices(l, r)\n        for i in reversed(indices):\n\
    \            self.__push(i)\n\n        l2 = l\n        r2 = r\n        while l2\
    \ < r2:\n            if l2 & 1:\n                self.__apply(l2, f)\n       \
    \         l2 += 1\n            if r2 & 1:\n                r2 -= 1\n         \
    \       self.__apply(r2, f)\n            l2 >>= 1\n            r2 >>= 1\n\n  \
    \      for i in indices:\n            self.__update(i)\n\n    def bisect_from_left(self,\
    \ l: int, fn: Callable[[S], bool]) -> int:\n        raise NotImplementedError\n\
    \n    def bisect_from_right(self, r: int, fn: Callable[[S], bool]) -> int:\n \
    \       raise NotImplementedError\n\n    def __get_indices(self, l, r):\n    \
    \    l0 = (l // (l & -l)) >> 1\n        r0 = (r // (r & -r)) >> 1\n        while\
    \ l0 != r0:\n            if l0 > r0:\n                yield l0\n             \
    \   l0 >>= 1\n            else:\n                yield r0\n                r0\
    \ >>= 1\n        while l0:\n            yield l0\n            l0 >>= 1\n\n   \
    \ def __update(self, k: int) -> None:\n        self.data[k] = self.op(self.data[k\
    \ * 2], self.data[k * 2 + 1])\n\n    def __apply(self, k: int, f: F) -> None:\n\
    \        self.data[k] = self.mapping(f, self.data[k])\n        if k < self.n_leaf:\n\
    \            self.lazy[k] = self.composition(f, self.lazy[k])\n\n    def __push(self,\
    \ k: int) -> None:\n        self.__apply(2 * k, self.lazy[k])\n        self.__apply(2\
    \ * k + 1, self.lazy[k])\n        self.lazy[k] = self.ident_F\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/data/lazy_segment_tree.py
  requiredBy: []
  timestamp: '2022-03-10 05:04:56+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/lazysegtree/range_update_query.test.py
documentation_of: byslib/data/lazy_segment_tree.py
layout: document
redirect_from:
- /library/byslib/data/lazy_segment_tree.py
- /library/byslib/data/lazy_segment_tree.py.html
title: byslib/data/lazy_segment_tree.py
---

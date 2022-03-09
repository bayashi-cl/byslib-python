---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/segment_tree.test.py
    title: tests/segment_tree.test.py
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
  code: "from typing import List, TypeVar, Generic, Callable\n\nT = TypeVar(\"T\"\
    )\n\n\nclass SegmentTree(Generic[T]):\n    def __init__(self, op: Callable[[T,\
    \ T], T], ident: T, val: List[T]) -> None:\n        self.op = op\n        self.ident\
    \ = ident\n        self.n = len(val)\n        self.n_leaf = 1 << (self.n - 1).bit_length()\n\
    \        self.data = [self.ident] * (self.n_leaf * 2)\n        self.data[self.n_leaf\
    \ : self.n_leaf + self.n] = val\n        for i in range(self.n_leaf - 1, 0, -1):\n\
    \            self.data[i] = self.op(self.data[i * 2], self.data[i * 2 + 1])\n\n\
    \    def update(self, i: int, v: T) -> None:\n        i += self.n_leaf\n     \
    \   self.data[i] = v\n        i >>= 1\n        while i > 0:\n            self.data[i]\
    \ = self.op(self.data[i * 2], self.data[i * 2 + 1])\n            i >>= 1\n\n \
    \   def query(self, l: int, r: int) -> T:\n        left = self.ident\n       \
    \ right = self.ident\n        l += self.n_leaf\n        r += self.n_leaf\n   \
    \     while l < r:\n            if l & 1:\n                left = self.op(left,\
    \ self.data[l])\n                l += 1\n            if r & 1:\n             \
    \   r -= 1\n                right = self.op(self.data[r], right)\n           \
    \ l >>= 1\n            r >>= 1\n        return self.op(left, right)\n\n    def\
    \ query_all(self) -> T:\n        return self.data[1]\n\n    def __getitem__(self,\
    \ key: int) -> T:\n        return self.data[key + self.n_leaf]\n\n    @classmethod\n\
    \    def empty(cls, op: Callable[[T, T], T], ident: T, n: int) -> \"SegmentTree\"\
    :\n        return cls(op, ident, [ident] * n)\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/data/segment_tree.py
  requiredBy: []
  timestamp: '2022-03-10 05:04:56+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/segment_tree.test.py
documentation_of: byslib/data/segment_tree.py
layout: document
redirect_from:
- /library/byslib/data/segment_tree.py
- /library/byslib/data/segment_tree.py.html
title: byslib/data/segment_tree.py
---

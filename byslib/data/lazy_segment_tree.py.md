---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import typing\nfrom .segment_tree import SegmentTree\n\n\nclass LazySegmentTree(SegmentTree):\n\
    \    \"\"\"\u9045\u5EF6\u8A55\u4FA1\u30BB\u30B0\u30E1\u30F3\u30C8\u6728\"\"\"\n\
    \n    def __init__(self, val: typing.List[float], func: typing.Callable):\n  \
    \      super().__init__(val, func)\n        self.lazy = [None] * (2 * self.n_leaf)\n\
    \n    def gindex(self, l: int, r: int) -> typing.Generator[float, None, None]:\n\
    \        l += self.n_leaf\n        r += self.n_leaf\n        lm = l >> (l & -l).bit_length()\n\
    \        rm = r >> (r & -r).bit_length()\n        while r > l:\n            if\
    \ l <= lm:\n                yield l\n            if r <= rm:\n               \
    \ yield r\n            r >>= 1\n            l >>= 1\n        while l:\n      \
    \      yield l\n            l >>= 1\n\n    def propagates(self, ids):\n      \
    \  for i in reversed(ids):\n            v = self.lazy[i]\n            if v is\
    \ None:\n                continue\n            self.lazy[2 * i] = v\n        \
    \    self.lazy[2 * i + 1] = v\n            self.tree[2 * i] = v\n            self.tree[2\
    \ * i + 1] = v\n            self.lazy[i] = None\n\n    def update(self, l, r,\
    \ x):\n        (*ids,) = self.gindex(l, r)\n        self.propagates(ids)\n   \
    \     l += self.n_leaf\n        r += self.n_leaf\n        while l < r:\n     \
    \       if l & 1:\n                self.lazy[l] = x\n                self.tree[l]\
    \ = x\n                l += 1\n            if r & 1:\n                self.lazy[r\
    \ - 1] = x\n                self.tree[r - 1] = x\n            r >>= 1\n      \
    \      l >>= 1\n        for i in ids:\n            self.tree[i] = self.func(self.tree[2\
    \ * i], self.tree[2 * i + 1])\n\n    def query(self, l, r):\n        (*ids,) =\
    \ self.gindex(l, r)\n        self.propagates(ids)\n\n        res = self.ident\n\
    \n        l += self.n_leaf\n        r += self.n_leaf\n        while l < r:\n \
    \           if l & 1:\n                res = self.func(res, self.tree[l])\n  \
    \              l += 1\n            if r & 1:\n                res = self.func(res,\
    \ self.tree[r - 1])\n            l >>= 1\n            r >>= 1\n        return\
    \ res\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/data/lazy_segment_tree.py
  requiredBy: []
  timestamp: '2022-02-28 04:59:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/data/lazy_segment_tree.py
layout: document
redirect_from:
- /library/byslib/data/lazy_segment_tree.py
- /library/byslib/data/lazy_segment_tree.py.html
title: byslib/data/lazy_segment_tree.py
---

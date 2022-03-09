---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/binary_indexed_tree.test.py
    title: tests/binary_indexed_tree.test.py
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
  code: "import typing\n\n\nclass BinaryIndexedTree:\n    \"\"\"\u30D5\u30A7\u30CB\
    \u30C3\u30AF\u6728\n    **0-index**\n    \"\"\"\n\n    def __init__(self, size:\
    \ int) -> None:\n        self.size = size\n        self.tree = [0] * (size + 1)\n\
    \n    def add(self, i: int, x: int) -> None:\n        i += 1\n        while i\
    \ <= self.size:\n            self.tree[i] += x\n            i += i & -i\n\n  \
    \  def cumsum(self, r: int) -> int:\n        \"\"\"\u7D2F\u7A4D\u548C\n      \
    \  [0, r)\u306E\u548C\u3092\u6C42\u3081\u308B\u3002\n        \"\"\"\n        s\
    \ = 0\n        while r:\n            s += self.tree[r]\n            r -= r & -r\n\
    \        return s\n\n    def range_sum(self, l: int, r: int) -> int:\n       \
    \ \"\"\"\u90E8\u5206\u548C\n        [l, r)\u306E\u548C\u3092\u6C42\u3081\u308B\
    \u3002\n        \"\"\"\n        return self.cumsum(r) - self.cumsum(l)\n\n   \
    \ @classmethod\n    def construct(cls, array: typing.List[int]) -> \"BinaryIndexedTree\"\
    :\n        res = cls(len(array))\n        for ele in enumerate(array):\n     \
    \       res.add(*ele)\n\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/data/binary_indexed_tree.py
  requiredBy: []
  timestamp: '2022-02-14 17:11:18+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/binary_indexed_tree.test.py
documentation_of: byslib/data/binary_indexed_tree.py
layout: document
redirect_from:
- /library/byslib/data/binary_indexed_tree.py
- /library/byslib/data/binary_indexed_tree.py.html
title: byslib/data/binary_indexed_tree.py
---

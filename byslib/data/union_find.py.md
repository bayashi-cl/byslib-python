---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/kruskal.test.py
    title: tests/kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: tests/union_find.test.py
    title: tests/union_find.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Dict\n\n\nclass UnionFindTree:\n    \"\"\"Union-Find\u6728\
    \"\"\"\n\n    def __init__(self, n: int) -> None:\n        self.n = n\n      \
    \  self.n_tree = n\n        self.parent = [-1] * self.n  # \u8CA0\u306A\u3089\u89AA\
    \u3067\u3042\u308A\u305D\u306E\u5024\u306F(-\u5B50\u306E\u6570)\n\n    def find(self,\
    \ a: int) -> int:\n        now = a\n        path = []\n        while self.parent[now]\
    \ >= 0:\n            path.append(now)\n            now = self.parent[now]\n  \
    \      else:\n            root = now\n\n        for p in path:\n            self.parent[p]\
    \ = root\n\n        return root\n\n    def union(self, a: int, b: int) -> bool:\n\
    \        root_a = self.find(a)\n        root_b = self.find(b)\n\n        if root_a\
    \ == root_b:\n            return False\n\n        if -self.parent[root_a] > -self.parent[root_b]:\n\
    \            root_a, root_b = root_b, root_a\n        self.parent[root_b] += self.parent[root_a]\n\
    \        self.parent[root_a] = root_b\n\n        self.n_tree -= 1\n        return\
    \ True\n\n    def same(self, a: int, b: int) -> bool:\n        return self.find(a)\
    \ == self.find(b)\n\n    def size(self, a: int) -> int:\n        return -self.parent[self.find(a)]\n\
    \n    def group(self) -> Dict[int, List[int]]:\n        res: Dict[int, List[int]]\
    \ = dict()\n        for i in range(self.n):\n            leader = self.find(i)\n\
    \            if leader in res:\n                res[leader].append(i)\n      \
    \      else:\n                res[leader] = [i]\n\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/data/union_find.py
  requiredBy: []
  timestamp: '2022-02-28 04:59:03+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/union_find.test.py
  - tests/kruskal.test.py
documentation_of: byslib/data/union_find.py
layout: document
redirect_from:
- /library/byslib/data/union_find.py
- /library/byslib/data/union_find.py.html
title: byslib/data/union_find.py
---

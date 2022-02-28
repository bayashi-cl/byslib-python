---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/dijkstra.test.py
    title: tests/dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: tests/kruskal.test.py
    title: tests/kruskal.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List\n\n\nclass Edge:\n    __slots__ = (\"src\", \"dest\"\
    , \"weight\")\n\n    def __init__(self, src: int, dest: int, weight: int = 1)\
    \ -> None:\n        self.src = src\n        self.dest = dest\n        self.weight\
    \ = weight\n\n    def __lt__(self, rh: \"Edge\") -> bool:\n        return self.weight\
    \ < rh.weight\n\n    def __repr__(self) -> str:\n        return f\"{{{self.src}\
    \ -> {self.dest}: {self.weight}}}\"\n\n\nclass AdjacencyList(List[List[Edge]]):\n\
    \    def add_edge(self, src: int, dest: int, weight: int = -1) -> None:\n    \
    \    self[src].append(Edge(src, dest, weight))\n\n    @classmethod\n    def init(cls,\
    \ n: int) -> \"AdjacencyList\":\n        return cls([[] for _ in range(n)])\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/edge.py
  requiredBy: []
  timestamp: '2022-02-28 04:59:03+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/dijkstra.test.py
  - tests/kruskal.test.py
documentation_of: byslib/graph/edge.py
layout: document
redirect_from:
- /library/byslib/graph/edge.py
- /library/byslib/graph/edge.py.html
title: byslib/graph/edge.py
---

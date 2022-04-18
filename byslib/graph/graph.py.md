---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/graph/dijkstra.test.py
    title: tests/graph/dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: tests/graph/kruskal.test.py
    title: tests/graph/kruskal.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    document_title: Adjacency List
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Adjacency List\nfrom typing import List, Tuple\n\n\nclass LilMatrix(List[List[Tuple[int,\
    \ int]]]):\n    \"\"\"List in List Matrix\"\"\"\n\n    @classmethod\n    def empty(cls,\
    \ n: int) -> \"LilMatrix\":\n        return cls([[] for _ in range(n)])\n\n  \
    \  def add_edge(self, src: int, dest: int, weight: int = 1) -> None:\n       \
    \ self[src].append((dest, weight))\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/graph.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/graph/dijkstra.test.py
  - tests/graph/kruskal.test.py
documentation_of: byslib/graph/graph.py
layout: document
redirect_from:
- /library/byslib/graph/graph.py
- /library/byslib/graph/graph.py.html
title: Adjacency List
---

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
    document_title: Edge
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Edge\nfrom typing import List\n\n\nclass Edge:\n    __slots__ =\
    \ (\"src\", \"dest\", \"weight\")\n\n    def __init__(self, src: int, dest: int,\
    \ weight: int = 1) -> None:\n        self.src = src\n        self.dest = dest\n\
    \        self.weight = weight\n\n    def __lt__(self, rh: \"Edge\") -> bool:\n\
    \        return self.weight < rh.weight\n\n    def __repr__(self) -> str:\n  \
    \      return f\"{{{self.src} -> {self.dest}: {self.weight}}}\"\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/edge.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/graph/dijkstra.test.py
  - tests/graph/kruskal.test.py
documentation_of: byslib/graph/edge.py
layout: document
redirect_from:
- /library/byslib/graph/edge.py
- /library/byslib/graph/edge.py.html
title: Edge
---
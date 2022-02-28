---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
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
  code: "from typing import List, Tuple\n\nfrom .edge import Edge\nfrom ..data.union_find\
    \ import UnionFindTree\n\n\ndef kruskal(edges: List[Edge], n_node: int) -> Tuple[int,\
    \ List[Edge]]:\n    edges.sort()\n    uft = UnionFindTree(n_node)\n    mst: List[Edge]\
    \ = []\n    cost = 0\n    for e in edges:\n        if uft.union(e.src, e.dest):\n\
    \            cost += e.weight\n            mst.append(e)\n    return cost, mst\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/kruskal.py
  requiredBy: []
  timestamp: '2022-02-28 04:59:03+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/kruskal.test.py
documentation_of: byslib/graph/kruskal.py
layout: document
redirect_from:
- /library/byslib/graph/kruskal.py
- /library/byslib/graph/kruskal.py.html
title: byslib/graph/kruskal.py
---

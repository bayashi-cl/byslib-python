---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/graph/kruskal.test.py
    title: tests/graph/kruskal.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    document_title: kruskal
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title kruskal\nfrom typing import List, Tuple\n\nfrom ..data.union_find\
    \ import UnionFindTree\nfrom .edge import Edge\n\n\ndef kruskal(edges: List[Edge],\
    \ n_node: int) -> Tuple[int, List[Edge]]:\n    \"\"\"Kruskal\n\n    Parameters\n\
    \    ----------\n    edges\n        List of Edges\n    n_node\n        Node size\n\
    \n    Returns\n    -------\n    Minimum (cost, Tree)\n\n    Notes\n    -----\n\
    \    Time complexity\n\n    O(E log(E))\n\n    References\n    ----------\n  \
    \  ..[1] \U0001F41C p.99\n    \"\"\"\n\n    edges.sort()\n    uft = UnionFindTree(n_node)\n\
    \    mst: List[Edge] = []\n    cost = 0\n    for e in edges:\n        if uft.union(e.src,\
    \ e.dest):\n            cost += e.weight\n            mst.append(e)\n    return\
    \ cost, mst\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/kruskal.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/graph/kruskal.test.py
documentation_of: byslib/graph/kruskal.py
layout: document
redirect_from:
- /library/byslib/graph/kruskal.py
- /library/byslib/graph/kruskal.py.html
title: kruskal
---

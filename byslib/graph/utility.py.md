---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/dijkstra.test.py
    title: tests/dijkstra.test.py
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
  code: "from typing import List, Tuple\n\n\nfrom .edge import AdjacencyList, Edge\n\
    from .depth_first_search import DepthFirstSearch\n\nSSSPResult = Tuple[List[int],\
    \ List[int]]\n\n\ndef restore_path(prev: List[int], to: int) -> List[int]:\n \
    \   res = []\n    while to != -1:\n        res.append(to)\n        to = prev[to]\n\
    \    return res[::-1]\n\n\ndef rooted_tree(graph: AdjacencyList, root: int) ->\
    \ AdjacencyList:\n    dfs = DepthFirstSearch(graph)\n    res = AdjacencyList.init(len(graph))\n\
    \    for now in dfs.pre_order(root):\n        for nxt in graph[now]:\n       \
    \     if nxt.dest != dfs.prev[now]:\n                res.add_edge(nxt.src, nxt.dest,\
    \ nxt.weight)\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/utility.py
  requiredBy: []
  timestamp: '2022-02-28 04:59:03+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/dijkstra.test.py
documentation_of: byslib/graph/utility.py
layout: document
redirect_from:
- /library/byslib/graph/utility.py
- /library/byslib/graph/utility.py.html
title: byslib/graph/utility.py
---

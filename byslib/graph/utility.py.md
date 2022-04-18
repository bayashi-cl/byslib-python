---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/graph/dijkstra.test.py
    title: tests/graph/dijkstra.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    document_title: Graph Utility
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Graph Utility\nfrom typing import List, Tuple\n\nfrom .depth_first_search\
    \ import DepthFirstSearch\nfrom .graph import LilMatrix\n\n\ndef restore_path(prev:\
    \ List[int], to: int) -> List[int]:\n    res = []\n    while to != -1:\n     \
    \   res.append(to)\n        to = prev[to]\n    return res[::-1]\n\n\ndef rooted_tree(graph:\
    \ LilMatrix, root: int) -> LilMatrix:\n    dfs = DepthFirstSearch(graph)\n   \
    \ res = LilMatrix.empty(len(graph))\n    for now in dfs.pre_order(root):\n   \
    \     for dest, weight in graph[now]:\n            if dest != dfs.prev[now]:\n\
    \                res.add_edge(now, dest, weight)\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/utility.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/graph/dijkstra.test.py
documentation_of: byslib/graph/utility.py
layout: document
redirect_from:
- /library/byslib/graph/utility.py
- /library/byslib/graph/utility.py.html
title: Graph Utility
---

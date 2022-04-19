---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: byslib/__init__.py
    title: byslib/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/core/__init__.py
    title: Core Featule
  - icon: ':heavy_check_mark:'
    path: byslib/core/const.py
    title: Const
  - icon: ':heavy_check_mark:'
    path: byslib/core/fastio.py
    title: Fast I/O
  - icon: ':heavy_check_mark:'
    path: byslib/graph/__init__.py
    title: Graph
  - icon: ':heavy_check_mark:'
    path: byslib/graph/depth_first_search.py
    title: Depth First Search
  - icon: ':heavy_check_mark:'
    path: byslib/graph/dijkstra.py
    title: Dijkstra
  - icon: ':heavy_check_mark:'
    path: byslib/graph/edge.py
    title: Edge
  - icon: ':heavy_check_mark:'
    path: byslib/graph/graph.py
    title: Adjacency List
  - icon: ':heavy_check_mark:'
    path: byslib/graph/utility.py
    title: Graph Utility
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/shortest_path
    links:
    - https://judge.yosupo.jp/problem/shortest_path
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path\n\
    from byslib.core.const import IINF\nfrom byslib.core.fastio import readline\n\
    from byslib.graph import LilMatrix\nfrom byslib.graph.dijkstra import dijkstra\n\
    from byslib.graph.utility import restore_path\n\n\ndef main() -> None:\n    n,\
    \ m, s, t = map(int, readline().split())\n    graph = LilMatrix.empty(n)\n   \
    \ for _ in range(m):\n        a, b, c = map(int, readline().split())\n       \
    \ graph.add_edge(a, b, c)\n\n    cost, prev = dijkstra(graph, s)\n    if cost[t]\
    \ == IINF:\n        print(-1)\n    else:\n        path = restore_path(prev, t)\n\
    \        y = len(path) - 1\n        print(cost[t], y)\n        for i in range(y):\n\
    \            print(path[i], path[i + 1])\n\n\nif __name__ == \"__main__\":\n \
    \   main()\n"
  dependsOn:
  - byslib/__init__.py
  - byslib/graph/depth_first_search.py
  - byslib/graph/utility.py
  - byslib/graph/dijkstra.py
  - byslib/graph/edge.py
  - byslib/core/const.py
  - byslib/graph/graph.py
  - byslib/core/__init__.py
  - byslib/core/fastio.py
  - byslib/graph/__init__.py
  isVerificationFile: true
  path: tests/graph/dijkstra.test.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/graph/dijkstra.test.py
layout: document
redirect_from:
- /verify/tests/graph/dijkstra.test.py
- /verify/tests/graph/dijkstra.test.py.html
title: tests/graph/dijkstra.test.py
---

---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: byslib/__init__.py
    title: byslib/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/core/__init__.py
    title: byslib/core/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/core/const.py
    title: byslib/core/const.py
  - icon: ':heavy_check_mark:'
    path: byslib/core/io.py
    title: byslib/core/io.py
  - icon: ':heavy_check_mark:'
    path: byslib/graph/__init__.py
    title: byslib/graph/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/graph/depth_first_search.py
    title: byslib/graph/depth_first_search.py
  - icon: ':heavy_check_mark:'
    path: byslib/graph/dijkstra.py
    title: byslib/graph/dijkstra.py
  - icon: ':heavy_check_mark:'
    path: byslib/graph/edge.py
    title: byslib/graph/edge.py
  - icon: ':heavy_check_mark:'
    path: byslib/graph/utility.py
    title: byslib/graph/utility.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/shortest_path
    links:
    - https://judge.yosupo.jp/problem/shortest_path
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path\n\
    from byslib.core.io import sinput\nfrom byslib.core.const import IINF\nfrom byslib.graph.edge\
    \ import AdjacencyList\nfrom byslib.graph.dijkstra import dijkstra\nfrom byslib.graph.utility\
    \ import restore_path\n\n\ndef main() -> None:\n    n, m, s, t = map(int, sinput().split())\n\
    \    graph = AdjacencyList.init(n)\n    for _ in range(m):\n        a, b, c =\
    \ map(int, sinput().split())\n        graph.add_edge(a, b, c)\n\n    cost, prev\
    \ = dijkstra(graph, s)\n    if cost[t] == IINF:\n        print(-1)\n    else:\n\
    \        path = restore_path(prev, t)\n        y = len(path) - 1\n        print(cost[t],\
    \ y)\n        for i in range(y):\n            print(path[i], path[i + 1])\n\n\n\
    if __name__ == \"__main__\":\n    main()\n"
  dependsOn:
  - byslib/__init__.py
  - byslib/graph/edge.py
  - byslib/core/const.py
  - byslib/graph/dijkstra.py
  - byslib/graph/__init__.py
  - byslib/graph/utility.py
  - byslib/core/__init__.py
  - byslib/core/io.py
  - byslib/graph/depth_first_search.py
  isVerificationFile: true
  path: tests/dijkstra.test.py
  requiredBy: []
  timestamp: '2022-03-10 05:05:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/dijkstra.test.py
layout: document
redirect_from:
- /verify/tests/dijkstra.test.py
- /verify/tests/dijkstra.test.py.html
title: tests/dijkstra.test.py
---

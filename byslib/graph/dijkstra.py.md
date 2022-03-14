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
  code: "import heapq\r\nfrom typing import List, Tuple\r\n\r\nfrom ..core.const import\
    \ IINF\r\nfrom .edge import AdjacencyList\r\n\r\n\r\ndef dijkstra(graph: AdjacencyList,\
    \ source: int) -> Tuple[List[int], List[int]]:\r\n    n = len(graph)\r\n    cost\
    \ = [IINF] * n\r\n    cost[source] = 0\r\n    prev = [-1] * n\r\n    que: List[Tuple[int,\
    \ int]] = [(0, source)]\r\n    while que:\r\n        top_cost, top = heapq.heappop(que)\r\
    \n        if cost[top] < top_cost:\r\n            continue\r\n        for nxt\
    \ in graph[top]:\r\n            nxt_cost = cost[top] + nxt.weight\r\n        \
    \    if nxt_cost < cost[nxt.dest]:\r\n                cost[nxt.dest] = nxt_cost\r\
    \n                prev[nxt.dest] = top\r\n                heapq.heappush(que,\
    \ (nxt_cost, nxt.dest))\r\n    return cost, prev\r\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/dijkstra.py
  requiredBy: []
  timestamp: '2022-03-15 06:00:23+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/dijkstra.test.py
documentation_of: byslib/graph/dijkstra.py
layout: document
redirect_from:
- /library/byslib/graph/dijkstra.py
- /library/byslib/graph/dijkstra.py.html
title: byslib/graph/dijkstra.py
---

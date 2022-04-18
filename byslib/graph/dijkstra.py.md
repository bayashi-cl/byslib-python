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
    document_title: Dijkstra
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Dijkstra\r\nimport heapq\r\nfrom typing import Iterable, List, Tuple,\
    \ Union\r\n\r\nfrom ..core.const import IINF\r\nfrom .graph import LilMatrix\r\
    \n\r\n\r\ndef dijkstra(\r\n    graph: LilMatrix, source: Union[int, Iterable[int]]\r\
    \n) -> Tuple[List[int], List[int]]:\r\n    \"\"\"Dijkstra\r\n\r\n    Parameters\r\
    \n    ----------\r\n    graph\r\n        Weighted Graph\r\n    source\r\n    \
    \    (list of) source\r\n\r\n    Returns\r\n    -------\r\n        (cost, prev)\r\
    \n\r\n    Notes\r\n    -----\r\n    Time complexity\r\n\r\n    O(V + Elog(V))\r\
    \n\r\n    References\r\n    ----------\r\n    ..[1] \U0001F41C p.96\r\n\r\n  \
    \  \"\"\"\r\n    n = len(graph)\r\n    cost = [IINF] * n\r\n    prev = [-1] *\
    \ n\r\n    que: List[Tuple[int, int]] = []\r\n\r\n    if isinstance(source, int):\r\
    \n        que = [(0, source)]\r\n        cost[source] = 0\r\n    else:\r\n   \
    \     que = [(0, si) for si in source]\r\n        for si in source:\r\n      \
    \      cost[si] = 0\r\n    heapq.heapify(que)\r\n\r\n    while que:\r\n      \
    \  top_cost, top = heapq.heappop(que)\r\n        if cost[top] < top_cost:\r\n\
    \            continue\r\n        for dest, weight in graph[top]:\r\n         \
    \   nxt_cost = cost[top] + weight\r\n            if nxt_cost < cost[dest]:\r\n\
    \                cost[dest] = nxt_cost\r\n                prev[dest] = top\r\n\
    \                heapq.heappush(que, (nxt_cost, dest))\r\n\r\n    return cost,\
    \ prev\r\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/dijkstra.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/graph/dijkstra.test.py
documentation_of: byslib/graph/dijkstra.py
layout: document
redirect_from:
- /library/byslib/graph/dijkstra.py
- /library/byslib/graph/dijkstra.py.html
title: Dijkstra
---

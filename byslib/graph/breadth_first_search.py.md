---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\nfrom typing import Deque\n\nfrom ..core.const\
    \ import IINF\nfrom .edge import AdjacencyList\nfrom .utility import SSSPResult\n\
    \n\ndef breadth_first_search(graph: AdjacencyList, source: int) -> SSSPResult:\n\
    \    n = len(graph)\n    prev = [-1] * n\n    cost = [IINF] * n\n    cost[source]\
    \ = 0\n    que: Deque[int] = deque()\n    que.append(source)\n    while que:\n\
    \        top = que.popleft()\n        for nxt in graph[top]:\n            if cost[nxt.dest]\
    \ == IINF:\n                cost[nxt.dest] = cost[top] + 1\n                prev[nxt.dest]\
    \ = top\n                que.append(nxt.dest)\n\n    return cost, prev\n\n\ndef\
    \ zero_one_bfs(graph: AdjacencyList, source: int, one: int = 1) -> SSSPResult:\n\
    \    n = len(graph)\n    cost = [IINF] * n\n    cost[source] = 0\n    prev = [-1]\
    \ * n\n    que: Deque[int] = deque()\n    que.append(source)\n    while que:\n\
    \        top = que.popleft()\n        for nxt in graph[top]:\n            nxt_cost\
    \ = cost[top] + nxt.weight\n            if nxt_cost < cost[nxt.dest]:\n      \
    \          cost[nxt.dest] = nxt_cost\n                prev[nxt.dest] = top\n \
    \               if nxt.weight == 0:\n                    que.appendleft(nxt.dest)\n\
    \                elif nxt.weight == one:\n                    que.append(nxt.dest)\n\
    \                else:\n                    raise ValueError\n\n    return cost,\
    \ prev\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/breadth_first_search.py
  requiredBy: []
  timestamp: '2022-02-28 04:59:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/graph/breadth_first_search.py
layout: document
redirect_from:
- /library/byslib/graph/breadth_first_search.py
- /library/byslib/graph/breadth_first_search.py.html
title: byslib/graph/breadth_first_search.py
---

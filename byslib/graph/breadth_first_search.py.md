---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    document_title: Breadth First Search
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Breadth First Search\nfrom collections import deque\nfrom typing\
    \ import Deque, Iterable, List, Tuple, Union\n\nfrom ..core.const import IINF\n\
    from .graph import LilMatrix\n\n\ndef breadth_first_search(\n    graph: LilMatrix,\
    \ source: Union[int, Iterable[int]]\n) -> Tuple[List[int], List[int]]:\n    \"\
    \"\"BFS\n\n    Parameters\n    ----------\n    graph\n        (Un)Weighted graph\n\
    \    source\n        source or list of source\n\n    Returns\n    -------\n  \
    \      (cost, prev)\n\n    Notes\n    -----\n    Time complexity\n\n    O(V +\
    \ E)\n\n    References\n    ----------\n    ..[1] \U0001F41C p.36\n    \"\"\"\n\
    \    n = len(graph)\n    prev = [-1] * n\n    cost = [IINF] * n\n\n    if isinstance(source,\
    \ int):\n        cost[source] = 0\n        que: Deque[int] = deque([source])\n\
    \    else:\n        for s in source:\n            cost[s] = 0\n        que = deque(source)\n\
    \n    while que:\n        top = que.popleft()\n        for dest, _ in graph[top]:\n\
    \            if cost[dest] == IINF:\n                cost[dest] = cost[top] +\
    \ 1\n                prev[dest] = top\n                que.append(dest)\n\n  \
    \  return cost, prev\n\n\ndef zero_one_bfs(\n    graph: LilMatrix, source: Union[int,\
    \ Iterable[int]], one: int = 1\n) -> Tuple[List[int], List[int]]:\n    \"\"\"\
    01BFS\n\n    Parameters\n    ----------\n    graph\n        Weighted graph\n \
    \   source\n        source or list of source\n    one\n        cost of `one`\n\
    \n    Returns\n    -------\n        (cost, prev)\n\n    Notes\n    -----\n   \
    \ Time complexity\n\n    O(V + E)\n    \"\"\"\n    n = len(graph)\n    cost =\
    \ [IINF] * n\n    prev = [-1] * n\n\n    if isinstance(source, int):\n       \
    \ cost[source] = 0\n        que: Deque[int] = deque([source])\n    else:\n   \
    \     for s in source:\n            cost[s] = 0\n        que = deque(source)\n\
    \n    while que:\n        top = que.popleft()\n        for dest, weight in graph[top]:\n\
    \            nxt_cost = cost[top] + weight\n            if nxt_cost < cost[dest]:\n\
    \                cost[dest] = nxt_cost\n                prev[dest] = top\n   \
    \             if weight == 0:\n                    que.appendleft(dest)\n    \
    \            elif weight == one:\n                    que.append(dest)\n     \
    \           else:\n                    raise ValueError\n\n    return cost, prev\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/breadth_first_search.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/graph/breadth_first_search.py
layout: document
redirect_from:
- /library/byslib/graph/breadth_first_search.py
- /library/byslib/graph/breadth_first_search.py.html
title: Breadth First Search
---

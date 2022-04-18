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
    document_title: Depth First Search
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Depth First Search\nfrom typing import Generator, List\n\nfrom .graph\
    \ import LilMatrix\n\n\nclass DepthFirstSearch:\n    \"\"\"DFS\n\n    pre-order\
    \ and post-order generator\n\n    Notes\n    -----\n    Time complexity\n\n  \
    \  O(V + E)\n\n    References\n    ----------\n    ..[1] \U0001F41C p.33\n   \
    \ \"\"\"\n\n    cost: List[int]\n\n    def __init__(self, graph: LilMatrix) ->\
    \ None:\n        \"\"\"Parameters\n        ----------\n        graph\n       \
    \     (Un)Weighted graph\n        \"\"\"\n        self.n = len(graph)\n      \
    \  self.graph = graph\n        self.prev = [-1] * self.n\n\n    def pre_order(self,\
    \ start: int) -> Generator[int, None, None]:\n        self.cost = [-1] * self.n\n\
    \        self.cost[start] = 0\n        que = [start]\n        while que:\n   \
    \         now = que.pop()\n            if now >= 0:\n                yield now\n\
    \                for dest, _ in self.graph[now]:\n                    if self.cost[dest]\
    \ != -1:\n                        continue\n                    self.cost[dest]\
    \ = self.cost[now] + 1\n                    self.prev[dest] = now\n          \
    \          que.append(dest)\n\n    def post_order(self, start: int) -> Generator[int,\
    \ None, None]:\n        self.cost = [-1] * self.n\n        self.cost[start] =\
    \ 0\n        que = [~start, start]\n        while que:\n            now = que.pop()\n\
    \            if now >= 0:\n                for dest, _ in self.graph[now]:\n \
    \                   if self.cost[dest] != -1:\n                        continue\n\
    \                    self.cost[dest] = self.cost[now] + 1\n                  \
    \  self.prev[dest] = now\n                    que.append(~dest)\n            \
    \        que.append(dest)\n\n            else:\n                yield ~now\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/depth_first_search.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/graph/dijkstra.test.py
documentation_of: byslib/graph/depth_first_search.py
layout: document
redirect_from:
- /library/byslib/graph/depth_first_search.py
- /library/byslib/graph/depth_first_search.py.html
title: Depth First Search
---

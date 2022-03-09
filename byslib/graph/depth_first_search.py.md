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
  code: "from typing import Generator, List\n\nfrom .edge import AdjacencyList\n\n\
    \nclass DepthFirstSearch:\n    cost: List[int]\n\n    def __init__(self, graph:\
    \ AdjacencyList) -> None:\n        self.n = len(graph)\n        self.graph = graph\n\
    \        self.prev = [-1] * self.n\n\n    def pre_order(self, start: int) -> Generator[int,\
    \ None, None]:\n        self.cost = [-1] * self.n\n        self.cost[start] =\
    \ 0\n        que = [start]\n        while que:\n            now = que.pop()\n\
    \            if now >= 0:\n                yield now\n                for nxt\
    \ in self.graph[now]:\n                    if self.cost[nxt.dest] != -1:\n   \
    \                     continue\n                    self.cost[nxt.dest] = self.cost[now]\
    \ + 1\n                    self.prev[nxt.dest] = now\n                    que.append(nxt.dest)\n\
    \n    def post_order(self, start: int) -> Generator[int, None, None]:\n      \
    \  self.cost = [-1] * self.n\n        self.cost[start] = 0\n        que = [~start,\
    \ start]\n        while que:\n            now = que.pop()\n            if now\
    \ >= 0:\n                for nxt in self.graph[now]:\n                    if self.cost[nxt.dest]\
    \ != -1:\n                        continue\n                    self.cost[nxt.dest]\
    \ = self.cost[now] + 1\n                    self.prev[nxt.dest] = now\n      \
    \              que.append(~nxt.dest)\n                    que.append(nxt.dest)\n\
    \n            else:\n                yield ~now\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/depth_first_search.py
  requiredBy: []
  timestamp: '2022-03-10 05:05:05+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/dijkstra.test.py
documentation_of: byslib/graph/depth_first_search.py
layout: document
redirect_from:
- /library/byslib/graph/depth_first_search.py
- /library/byslib/graph/depth_first_search.py.html
title: byslib/graph/depth_first_search.py
---

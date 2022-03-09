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
  code: "# region template\nimport sys\nimport typing\nfrom typing import Callable,\
    \ Dict, List, Set, Tuple\n\nsys.setrecursionlimit(10 ** 6)\nVec = List[int]\n\
    VecVec = List[Vec]\nsinput: Callable[..., str] = sys.stdin.readline\nMOD: int\
    \ = 1000000007\nINF: float = float(\"Inf\")\nIINF: int = sys.maxsize\n# endregion\n\
    \n\nclass WarshallFloyd:\n    Edge = Tuple[int, int]  # (cost, node)\n    Adj\
    \ = List[List[Edge]]\n\n    def __init__(self, graph: Adj) -> None:\n        self.n_node\
    \ = len(graph)\n        self.prev = [-1] * self.n_node\n        self.cost = [[INF]\
    \ * self.n_node for _ in range(self.n_node)]\n\n        for dep, edge in enumerate(graph):\n\
    \            for dist, arr in edge:\n                self.cost[dep][arr] = dist\n\
    \n        for i in range(self.n_node):\n            self.cost[i][i] = 0\n\n  \
    \  def search(self) -> None:\n        for k in range(self.n_node):\n         \
    \   for i in range(self.n_node):\n                for j in range(self.n_node):\n\
    \                    if (dist := self.cost[i][k] + self.cost[k][j]) < self.cost[i][j]:\n\
    \                        self.cost[i][j] = dist\n                        self.prev[j]\
    \ = k\n\n    def path_finder(self, to: int) -> List[int]:\n        assert to <=\
    \ self.n_node\n\n        path = []\n        while to != -1:\n            path.append(to)\n\
    \            to = self.prev[to]\n\n        return path[::-1]\n\n\ndef main() ->\
    \ None:\n    ...\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/warshall_floyd.py
  requiredBy: []
  timestamp: '2022-02-14 17:11:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/graph/warshall_floyd.py
layout: document
redirect_from:
- /library/byslib/graph/warshall_floyd.py
- /library/byslib/graph/warshall_floyd.py.html
title: byslib/graph/warshall_floyd.py
---

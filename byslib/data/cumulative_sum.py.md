---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/data/cumulative_sum.test.py
    title: tests/data/cumulative_sum.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    document_title: Cumulative Sum
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Cumulative Sum\nfrom itertools import chain\nfrom typing import\
    \ List\n\n\nclass CumulativeSum:\n    \"\"\"Cumulative Sum\n    Notes\n    -----\n\
    \    Get sum of semi-open interval [left, right)\n\n    Time complexity\n\n  \
    \  * Build : :math:`O(N)`\n    * fold : :math:`O(1)`\n\n    Examples\n    --------\n\
    \    >>> cs = CumulativeSum([3, 1, 4, 1, 5])\n    >>> print(cs.fold(0, 3))\n \
    \   8\n    \"\"\"\n\n    def __init__(self, data: List[int]) -> None:\n      \
    \  n = len(data)\n        self.__data = [0] * (n + 1)\n        for i in range(n):\n\
    \            self.__data[i + 1] = self.__data[i] + data[i]\n\n    def fold(self,\
    \ left: int, right: int) -> int:\n        return self.__data[right] - self.__data[left]\n\
    \n\nclass CumulativeSum2D:\n    \"\"\"Cumulative Sum 2D\n    Notes\n    -----\n\
    \    Get sum of range\n\n    Time complexity\n\n    * Build : :math:`O(N * M)`\n\
    \    * fold : :math:`O(1)`\n\n    Examples\n    --------\n    >>> cs = CumulativeSum([3,\
    \ 1, 4, 1, 5])\n    >>> print(cs.fold(0, 3))\n    8\n    \"\"\"\n\n    def __init__(self,\
    \ data: List[List[int]]) -> None:\n        n = len(data)\n        m = len(data[0])\n\
    \        self.__data = [[0] + row for row in chain([[0] * m], data)]\n       \
    \ for i in range(1, n + 1):\n            for j in range(1, m + 1):\n         \
    \       self.__data[i][j] += (\n                    self.__data[i][j - 1]\n  \
    \                  + self.__data[i - 1][j]\n                    - self.__data[i\
    \ - 1][j - 1]\n                )\n\n    def fold(self, up: int, left: int, down:\
    \ int, right: int) -> int:\n        return (\n            self.__data[down][right]\n\
    \            - self.__data[up][right]\n            - self.__data[down][left]\n\
    \            + self.__data[up][left]\n        )\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/data/cumulative_sum.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/data/cumulative_sum.test.py
documentation_of: byslib/data/cumulative_sum.py
layout: document
redirect_from:
- /library/byslib/data/cumulative_sum.py
- /library/byslib/data/cumulative_sum.py.html
title: Cumulative Sum
---

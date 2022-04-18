---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/data/binary_indexed_tree.test.py
    title: tests/data/binary_indexed_tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    document_title: Bynary Indexed Tree
    links:
    - https://scrapbox.io/data-structures/Fenwick_Tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Bynary Indexed Tree\nfrom typing import List\n\n\nclass BinaryIndexedTree:\n\
    \    r\"\"\"Bynary Indexed Tree (Fenwick Tree)\n\n    Notes\n    -----\n    Time\
    \ complexity\n\n    * Build : :math:`O(N)`\n    * Point_append : :math:`O(\\log(N))`\n\
    \    * Fold : :math:`O(\\log(N))`\n\n    References\n    ----------\n    ..[1]\
    \ \U0001F41C p.159\n    ..[2] https://scrapbox.io/data-structures/Fenwick_Tree\n\
    \n    Examples\n    --------\n    >>> bit = BinaryIndexedTree.zeros(5)\n    >>>\
    \ bit.point_append(0, 3)\n    >>> bit.point_append(2, -2)\n    >>> print(bit.fold(1,\
    \ 4))\n    -2\n    \"\"\"\n\n    def __init__(self, array: List[int]) -> None:\n\
    \        self.size = len(array)\n        self.data = [0] * (self.size + 1)\n \
    \       for i, ai in enumerate(array):\n            self.point_append(i, ai)\n\
    \n    def point_append(self, index: int, value: int) -> None:\n        index +=\
    \ 1\n        while index <= self.size:\n            self.data[index] += value\n\
    \            index += index & -index\n\n    def prefix_fold(self, right: int)\
    \ -> int:\n        s = 0\n        while right > 0:\n            s += self.data[right]\n\
    \            right -= right & -right\n        return s\n\n    def fold(self, left:\
    \ int, right: int) -> int:\n        return self.prefix_fold(right) - self.prefix_fold(left)\n\
    \n    @classmethod\n    def zeros(cls, n: int) -> \"BinaryIndexedTree\":\n   \
    \     return cls([0] * n)\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/data/binary_indexed_tree.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/data/binary_indexed_tree.test.py
documentation_of: byslib/data/binary_indexed_tree.py
layout: document
redirect_from:
- /library/byslib/data/binary_indexed_tree.py
- /library/byslib/data/binary_indexed_tree.py.html
title: Bynary Indexed Tree
---

---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/data/segment_tree.test.py
    title: tests/data/segment_tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    document_title: Segment Tree
    links:
    - https://ikatakos.com/pot/programming_algorithm/data_structure/segment_tree
    - https://scrapbox.io/data-structures/Segment_Tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Segment Tree\nfrom typing import Callable, Generic, List, TypeVar\n\
    \nT = TypeVar(\"T\")\n\n\nclass SegmentTree(Generic[T]):\n    r\"\"\"Segment Tree\n\
    \n    Parameters\n    ----------\n    Generic[T]\n        Set type of Monoid\n\
    \n    Notes\n    -----\n    Time complexity\n\n    * build : :math:`O(N)`\n  \
    \  * Point set : :math:`O(\\log(N))`\n    * Range fold : :math:`O(\\log(N))`\n\
    \n    References\n    ----------\n    ..[1] \U0001F41C p.153\n    ..[2] https://scrapbox.io/data-structures/Segment_Tree\n\
    \    ..[3] https://ikatakos.com/pot/programming_algorithm/data_structure/segment_tree\n\
    \n    Examples\n    --------\n    >>> seg = SegmentTree(max, 0, [1] * 10)\n  \
    \  >>> seg.set(3, 4)\n    >>> seg.set(8, 9)\n    >>> print(seg.fold(0,5))\n  \
    \  4\n    >>> len(seg)\n    10\n    >>> print(seg.fold_all())\n    9\n    >>>\
    \ print(seg[3])\n    4\n    \"\"\"\n\n    def __init__(\n        self, operation:\
    \ Callable[[T, T], T], identity: T, array: List[T]\n    ) -> None:\n        \"\
    \"\"build\n\n        Parameters\n        ----------\n        operation\n     \
    \       Binary operation of Monoid\n        identity\n            Identity of\
    \ Monoid\n        array\n            Init array\n        \"\"\"\n        self.__operation\
    \ = operation\n        self.__identity = identity\n        self.__n = len(array)\n\
    \        self.__n_leaf = 1 << (self.__n - 1).bit_length()\n        self.__data\
    \ = [self.__identity] * (self.__n_leaf * 2)\n        self.__data[self.__n_leaf\
    \ : self.__n_leaf + self.__n] = array\n        for i in range(self.__n_leaf -\
    \ 1, 0, -1):\n            self.__data[i] = self.__operation(\n               \
    \ self.__data[i * 2], self.__data[i * 2 + 1]\n            )\n\n    def set(self,\
    \ index: int, value: T) -> None:\n        index += self.__n_leaf\n        self.__data[index]\
    \ = value\n        index >>= 1\n        while index > 0:\n            self.__data[index]\
    \ = self.__operation(\n                self.__data[index * 2], self.__data[index\
    \ * 2 + 1]\n            )\n            index >>= 1\n\n    def fold(self, left:\
    \ int, right: int) -> T:\n        left_fold = self.__identity\n        right_fold\
    \ = self.__identity\n        left += self.__n_leaf\n        right += self.__n_leaf\n\
    \        while left < right:\n            if left & 1:\n                left_fold\
    \ = self.__operation(left_fold, self.__data[left])\n                left += 1\n\
    \            if right & 1:\n                right -= 1\n                right_fold\
    \ = self.__operation(self.__data[right], right_fold)\n            left >>= 1\n\
    \            right >>= 1\n        return self.__operation(left_fold, right_fold)\n\
    \n    def fold_all(self) -> T:\n        return self.__data[1]\n\n    def __getitem__(self,\
    \ key: int) -> T:\n        return self.__data[key + self.__n_leaf]\n\n    def\
    \ __len__(self) -> int:\n        return self.__n\n\n    @classmethod\n    def\
    \ zeros(cls, op: Callable[[T, T], T], ident: T, n: int) -> \"SegmentTree\":\n\
    \        return cls(op, ident, [ident] * n)\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/data/segment_tree.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/data/segment_tree.test.py
documentation_of: byslib/data/segment_tree.py
layout: document
redirect_from:
- /library/byslib/data/segment_tree.py
- /library/byslib/data/segment_tree.py.html
title: Segment Tree
---

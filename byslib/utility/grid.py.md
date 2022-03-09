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
  code: "import typing\n\n\nclass Grid:\n    DeltaItr = typing.Iterable[typing.Tuple[int,\
    \ int]]\n    h: int\n    w: int\n\n    def __init__(self, h: int, w: int) -> None:\n\
    \        self.h = h\n        self.w = w\n\n    def __contains__(self, ij: typing.Tuple[int,\
    \ int]) -> bool:\n        return 0 <= ij[0] < self.h and 0 <= ij[1] < self.w\n\
    \n    def area(self) -> int:\n        return self.h * self.w\n\n    def index(self,\
    \ i: int, j: int) -> int:\n        if (i, j) not in self:\n            raise ValueError(\"\
    index out of grid\")\n        return self.w * i + j\n\n    def coord(self, ind:\
    \ int) -> typing.Tuple[int, int]:\n        if ind < 0 or self.area() <= ind:\n\
    \            raise ValueError(\"index out of grid\")\n        return divmod(ind,\
    \ self.w)\n\n    def delta(self, i: int, j: int, d: DeltaItr) -> DeltaItr:\n \
    \       if (i, j) not in self:\n            raise ValueError(\"index out of grid\"\
    )\n        for di, dj in d:\n            ni, nj = i + di, j + dj\n           \
    \ if (ni, nj) in self:\n                yield (ni, nj)\n\n    def delta2(self,\
    \ i: int, j: int) -> DeltaItr:\n        return self.delta(i, j, ((0, 1), (1, 0)))\n\
    \n    def delta4(self, i: int, j: int) -> DeltaItr:\n        return self.delta(i,\
    \ j, ((-1, 0), (0, 1), (1, 0), (0, -1)))\n\n    def delta8(self, i: int, j: int)\
    \ -> DeltaItr:\n        d = []\n        for di in range(-1, 2):\n            for\
    \ dj in range(-1, 2):\n                if di == 0 and dj == 0:\n             \
    \       continue\n                d.append((di, dj))\n        return self.delta(i,\
    \ j, d)\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/utility/grid.py
  requiredBy: []
  timestamp: '2022-02-18 18:18:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/utility/grid.py
layout: document
redirect_from:
- /library/byslib/utility/grid.py
- /library/byslib/utility/grid.py.html
title: byslib/utility/grid.py
---

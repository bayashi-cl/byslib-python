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
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List\nfrom itertools import accumulate\n\n\nclass CumulativeSum:\n\
    \    def __init__(self, n: int) -> None:\n        self.data = [0] * (n + 1)\n\n\
    \    def update(self, i: int, x: int) -> None:\n        self.data[i + 1] = x\n\
    \n    def add(self, i: int, x: int) -> None:\n        self.data[i + 1] += x\n\n\
    \    def construct(self) -> None:\n        self.data = list(accumulate(self.data))\n\
    \n    def sum(self, l: int, r: int) -> int:\n        return self.data[r] - self.data[l]\n\
    \n    @classmethod\n    def from_list(cls, l: List[int]) -> \"CumulativeSum\"\
    :\n        n = len(l)\n        res = cls(n)\n        res.data[1:] = l\n      \
    \  return res\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/data/cumulative_sum.py
  requiredBy: []
  timestamp: '2022-03-01 00:20:32+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/data/cumulative_sum.py
layout: document
redirect_from:
- /library/byslib/data/cumulative_sum.py
- /library/byslib/data/cumulative_sum.py.html
title: byslib/data/cumulative_sum.py
---

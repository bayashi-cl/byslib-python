---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/mod_comb.test.py
    title: tests/mod_comb.test.py
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
  code: "class MultiComb:\n    \"\"\"\u4E8C\u9805\u4FC2\u6570\n    **__init__: O(n)**\n\
    \    **comb: O(1)**\n    \"\"\"\n\n    def __init__(self, n: int, mod: int = 10**9\
    \ + 7) -> None:\n        self.n = n\n        self.mod = mod\n        self.fact\
    \ = [1, 1]\n        self.factinv = [1, 1]\n        self.inv = [0, 1]\n       \
    \ for i in range(2, self.n + 1):\n            self.fact.append((self.fact[-1]\
    \ * i) % self.mod)\n            self.inv.append((-self.inv[self.mod % i] * (self.mod\
    \ // i)) % self.mod)\n            self.factinv.append((self.factinv[-1] * self.inv[-1])\
    \ % self.mod)\n\n    def comb(self, n: int, r: int) -> int:\n        if r < 0\
    \ or n < r:\n            return 0\n        r = min(r, n - r)\n        return self.fact[n]\
    \ * self.factinv[r] * self.factinv[n - r] % self.mod\n\n    def perm(self, n:\
    \ int, r: int) -> int:\n        if r < 0 or n < r:\n            return 0\n   \
    \     return self.fact[n] * self.factinv[n - r] % self.mod\n\n    def hom(self,\
    \ n: int, r: int) -> int:\n        if n == r == 0:\n            return 1\n   \
    \     return self.comb(n + r - 1, r)\n\n\ndef mono_comb(n: int, r: int, mod: int\
    \ = 10**9 + 7) -> int:\n    \"\"\"\u4E8C\u9805\u4FC2\u6570\n    **O(min(r, n-r))**\n\
    \    python3.8 or later\n    \"\"\"\n    r = min(r, n - r)\n    numer = 1\n  \
    \  denom = 1\n    for i in range(r):\n        numer *= n - i\n        denom *=\
    \ r - i\n\n        numer %= mod\n        denom %= mod\n\n    denom_mod = pow(denom,\
    \ -1, mod)\n    return (numer * denom_mod) % mod\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/math/mod_comb.py
  requiredBy: []
  timestamp: '2022-03-10 05:05:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/mod_comb.test.py
documentation_of: byslib/math/mod_comb.py
layout: document
redirect_from:
- /library/byslib/math/mod_comb.py
- /library/byslib/math/mod_comb.py.html
title: byslib/math/mod_comb.py
---

---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/numeric/mod_comb.test.py
    title: tests/numeric/mod_comb.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    document_title: Binomial coefficient
    links:
    - https://drken1215.hatenablog.com/entry/2018/06/08/210000
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Binomial coefficient\nclass MultiComb:\n    \"\"\"Binomial coefficient\n\
    \n    Notes\n    -----\n    Time complexity\n\n    * construct: O(n)\n    * query:\
    \ O(1)\n\n    References\n    ----------\n    ..[1] https://drken1215.hatenablog.com/entry/2018/06/08/210000\n\
    \n    Examples\n    --------\n    >>> mc = MultiComb(10)\n    >>> print(mc.comb(5,\
    \ 3))\n    10\n    \"\"\"\n\n    def __init__(self, n: int, mod: int = 10**9 +\
    \ 7) -> None:\n        self.n = n\n        self.mod = mod\n        self.fact =\
    \ [1, 1]\n        self.factinv = [1, 1]\n        self.inv = [0, 1]\n        for\
    \ i in range(2, self.n + 1):\n            self.fact.append((self.fact[-1] * i)\
    \ % self.mod)\n            self.inv.append((-self.inv[self.mod % i] * (self.mod\
    \ // i)) % self.mod)\n            self.factinv.append((self.factinv[-1] * self.inv[-1])\
    \ % self.mod)\n\n    def comb(self, n: int, r: int) -> int:\n        \"\"\"nCr\"\
    \"\"\n        if r < 0 or n < r:\n            return 0\n        r = min(r, n -\
    \ r)\n        return self.fact[n] * self.factinv[r] * self.factinv[n - r] % self.mod\n\
    \n    def perm(self, n: int, r: int) -> int:\n        \"\"\"nPr\"\"\"\n      \
    \  if r < 0 or n < r:\n            return 0\n        return self.fact[n] * self.factinv[n\
    \ - r] % self.mod\n\n    def hom(self, n: int, r: int) -> int:\n        \"\"\"\
    nHr\"\"\"\n        if n == r == 0:\n            return 1\n        return self.comb(n\
    \ + r - 1, r)\n\n\ndef mono_comb(n: int, r: int, mod: int = 10**9 + 7) -> int:\n\
    \    \"\"\"Binomial coefficient\n\n    python 3.8 or later\n\n    Parameters\n\
    \    ----------\n    n\n        n\n    r\n        r\n    mod, optional\n     \
    \   mod, by default 10**9+7\n\n    Returns\n    -------\n        nCr\n\n    Notes\n\
    \    -----\n    Time complexity\n\n    O(min(r, n - r))\n\n    Examples\n    --------\n\
    \    Examples\n    --------\n    >>> print(mono_comb(5, 3))\n    10\n    \"\"\"\
    \n    r = min(r, n - r)\n    numer = 1\n    denom = 1\n    for i in range(r):\n\
    \        numer *= n - i\n        denom *= r - i\n\n        numer %= mod\n    \
    \    denom %= mod\n\n    denom_mod = pow(denom, -1, mod)\n    return (numer *\
    \ denom_mod) % mod\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/numeric/mod_comb.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/numeric/mod_comb.test.py
documentation_of: byslib/numeric/mod_comb.py
layout: document
redirect_from:
- /library/byslib/numeric/mod_comb.py
- /library/byslib/numeric/mod_comb.py.html
title: Binomial coefficient
---

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
  code: "import typing\n\n\ndef make_divisors(n):\n    lower_divisors, upper_divisors\
    \ = [], []\n    i = 1\n    while i * i <= n:\n        if n % i == 0:\n       \
    \     lower_divisors.append(i)\n            if i != n // i:\n                upper_divisors.append(n\
    \ // i)\n        i += 1\n    return lower_divisors + upper_divisors[::-1]\n\n\n\
    def prime_factorize(n: int) -> typing.List[int]:\n    res = []\n    while n %\
    \ 2 == 0:\n        res.append(2)\n        n //= 2\n    f = 3\n    while f * f\
    \ <= n:\n        if n % f == 0:\n            res.append(f)\n            n //=\
    \ f\n        else:\n            f += 2\n    if n != 1:\n        res.append(n)\n\
    \    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/math/make_divisor.py
  requiredBy: []
  timestamp: '2022-02-18 18:18:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/math/make_divisor.py
layout: document
redirect_from:
- /library/byslib/math/make_divisor.py
- /library/byslib/math/make_divisor.py.html
title: byslib/math/make_divisor.py
---

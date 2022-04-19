---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/verify_pytest/test_numeric.test.py
    title: tests/verify_pytest/test_numeric.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    document_title: Euclid
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Euclid\nfrom typing import Tuple\n\n\ndef ext_gcd(a: int, b: int)\
    \ -> Tuple[int, int, int]:\n    \"\"\"Extended Euclidean algorithm\n\n    solve\
    \ ax + by = gcd(a, b)\n\n    Parameters\n    ----------\n    a\n    b\n\n    Returns\n\
    \    -------\n        (d, x, y) s.t. ax + by = gcd(a, b)\n    \"\"\"\n\n    if\
    \ b == 0:\n        return a, 1, 0\n    d, y, x = ext_gcd(b, a % b)\n    return\
    \ d, x, y - (a // b) * x\n\n\ndef crt(a: int, b: int, mod1: int, mod2: int) ->\
    \ int:\n    g, k, _ = ext_gcd(mod1, mod2)\n    if (b - a) % g != 0:\n        return\
    \ -1\n    k *= (b - a) // g\n    ans = mod1 * k + a\n    lcm = mod1 * mod2 //\
    \ g\n    return ans % lcm\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/numeric/euclid.py
  requiredBy: []
  timestamp: '2022-04-19 13:16:57+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/verify_pytest/test_numeric.test.py
documentation_of: byslib/numeric/euclid.py
layout: document
redirect_from:
- /library/byslib/numeric/euclid.py
- /library/byslib/numeric/euclid.py.html
title: Euclid
---

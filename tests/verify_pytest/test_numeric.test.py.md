---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: byslib/__init__.py
    title: byslib/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/numeric/__init__.py
    title: byslib/numeric/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/numeric/divisor.py
    title: Divisor
  - icon: ':heavy_check_mark:'
    path: byslib/numeric/euclid.py
    title: Euclid
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    import pytest\nfrom byslib.numeric import divisor, euclid\n\n\nclass TestDivisor:\n\
    \    @pytest.mark.parametrize(\n        (\"x\", \"divs\"),\n        [\n      \
    \      (1, [1]),\n            (2, [1, 2]),\n            (12, [1, 2, 3, 4, 6, 12]),\n\
    \            (17, [1, 17]),\n            (57, [1, 3, 19, 57]),\n            (998244353,\
    \ [1, 998244353]),\n            (100003**2, [1, 100003, 100003**2]),\n       \
    \ ],\n    )\n    def test_make_divisor(self, x, divs):\n        assert divisor.make_divisors(x)\
    \ == divs\n\n    @pytest.mark.parametrize(\n        (\"x\", \"facts\"),\n    \
    \    [\n            (1, []),\n            (2, [2]),\n            (17, [17]),\n\
    \            (24, [2, 2, 2, 3]),\n            (998244353, [998244353]),\n    \
    \    ],\n    )\n    def test_prime_factorize(self, x, facts):\n        assert\
    \ divisor.prime_factorize(x) == facts\n\n\nclass TestEuclid:\n    @pytest.mark.parametrize(\n\
    \        (\"a\", \"b\"),\n        [\n            (3, 4),\n            (5, 8),\n\
    \            (-5, 4),\n            (-1, -8),\n            (998244353, 1000000007),\n\
    \        ],\n    )\n    def test_ext_gcd(self, a, b):\n        d, x, y = euclid.ext_gcd(a,\
    \ b)\n        assert a * x + b * y == d\n\n\nif __name__ == \"__main__\":\n  \
    \  import sys\n\n    from exec_pytest import exec_pytest\n\n    sys.exit(exec_pytest(__file__))\n"
  dependsOn:
  - byslib/__init__.py
  - byslib/numeric/euclid.py
  - byslib/numeric/divisor.py
  - byslib/numeric/__init__.py
  isVerificationFile: true
  path: tests/verify_pytest/test_numeric.test.py
  requiredBy: []
  timestamp: '2022-04-19 13:16:57+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/verify_pytest/test_numeric.test.py
layout: document
redirect_from:
- /verify/tests/verify_pytest/test_numeric.test.py
- /verify/tests/verify_pytest/test_numeric.test.py.html
title: tests/verify_pytest/test_numeric.test.py
---

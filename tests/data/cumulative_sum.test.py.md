---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: byslib/__init__.py
    title: byslib/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/core/__init__.py
    title: Core Featule
  - icon: ':heavy_check_mark:'
    path: byslib/core/fastio.py
    title: Fast I/O
  - icon: ':heavy_check_mark:'
    path: byslib/data/__init__.py
    title: Data Structure
  - icon: ':heavy_check_mark:'
    path: byslib/data/cumulative_sum.py
    title: Cumulative Sum
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_sum
    links:
    - https://judge.yosupo.jp/problem/static_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum\n\
    import sys\n\nfrom byslib.core.fastio import readline\nfrom byslib.data.cumulative_sum\
    \ import CumulativeSum\n\n\ndef main() -> None:\n    n, q = map(int, readline().split())\n\
    \    a = list(map(int, readline().split()))\n    cs = CumulativeSum(a)\n    for\
    \ _ in range(q):\n        l, r = map(int, readline().split())\n        print(cs.fold(l,\
    \ r))\n\n\nif __name__ == \"__main__\":\n    sys.setrecursionlimit(10**6)\n  \
    \  main()\n"
  dependsOn:
  - byslib/__init__.py
  - byslib/data/__init__.py
  - byslib/data/cumulative_sum.py
  - byslib/core/__init__.py
  - byslib/core/fastio.py
  isVerificationFile: true
  path: tests/data/cumulative_sum.test.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/data/cumulative_sum.test.py
layout: document
redirect_from:
- /verify/tests/data/cumulative_sum.test.py
- /verify/tests/data/cumulative_sum.test.py.html
title: tests/data/cumulative_sum.test.py
---

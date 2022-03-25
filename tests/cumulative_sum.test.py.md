---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: byslib/__init__.py
    title: byslib/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/core/__init__.py
    title: byslib/core/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/core/const.py
    title: byslib/core/const.py
  - icon: ':heavy_check_mark:'
    path: byslib/core/fastio.py
    title: byslib/core/fastio.py
  - icon: ':heavy_check_mark:'
    path: byslib/data/__init__.py
    title: byslib/data/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/data/cumulative_sum.py
    title: byslib/data/cumulative_sum.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_sum
    links:
    - https://judge.yosupo.jp/problem/static_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum\n\
    import sys\n\nfrom byslib.core.const import IINF, MOD\nfrom byslib.core.fastio\
    \ import debug, readline, sinput\nfrom byslib.data.cumulative_sum import CumulativeSum\n\
    \n\ndef main() -> None:\n    n, q = map(int, readline().split())\n    a = list(map(int,\
    \ readline().split()))\n    cs = CumulativeSum.from_list(a)\n    cs.construct()\n\
    \    for _ in range(q):\n        l, r = map(int, readline().split())\n       \
    \ print(cs.sum(l, r))\n\n\nif __name__ == \"__main__\":\n    sys.setrecursionlimit(10**6)\n\
    \    main()\n"
  dependsOn:
  - byslib/__init__.py
  - byslib/core/fastio.py
  - byslib/data/__init__.py
  - byslib/data/cumulative_sum.py
  - byslib/core/__init__.py
  - byslib/core/const.py
  isVerificationFile: true
  path: tests/cumulative_sum.test.py
  requiredBy: []
  timestamp: '2022-03-15 06:00:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/cumulative_sum.test.py
layout: document
redirect_from:
- /verify/tests/cumulative_sum.test.py
- /verify/tests/cumulative_sum.test.py.html
title: tests/cumulative_sum.test.py
---

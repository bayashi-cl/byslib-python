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
    path: byslib/core/const.py
    title: Const
  - icon: ':heavy_check_mark:'
    path: byslib/core/fastio.py
    title: Fast I/O
  - icon: ':heavy_check_mark:'
    path: byslib/data/__init__.py
    title: Data Structure
  - icon: ':heavy_check_mark:'
    path: byslib/data/lazy_segment_tree.py
    title: Lazy Segment Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_F
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_F
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_F\n\
    import sys\n\nfrom byslib.core.const import IINF, MOD\nfrom byslib.core.fastio\
    \ import debug, readline, sinput\nfrom byslib.data.lazy_segment_tree import LazySegmentTree\n\
    \n\ndef main() -> None:\n    id_S: int = 2**31 - 1\n    id_F = -1\n\n    def op(a:\
    \ int, b: int) -> int:\n        return min(a, b)\n\n    def mp(a: int, b: int)\
    \ -> int:\n        return b if a == -1 else a\n\n    def cp(f: int, g: int) ->\
    \ int:\n        return g if f == -1 else f\n\n    n, q = map(int, readline().split())\n\
    \    a = [id_S] * n\n    seg = LazySegmentTree(op, id_S, mp, cp, id_F, a)\n  \
    \  for _ in range(q):\n        head, *body = map(int, readline().split())\n  \
    \      if head == 0:\n            s, t, x = body\n            seg.apply(s, t +\
    \ 1, x)\n        else:\n            s, t = body\n            print(seg.query(s,\
    \ t + 1))\n\n\nif __name__ == \"__main__\":\n    sys.setrecursionlimit(10**6)\n\
    \    main()\n"
  dependsOn:
  - byslib/data/__init__.py
  - byslib/data/lazy_segment_tree.py
  - byslib/__init__.py
  - byslib/core/const.py
  - byslib/core/fastio.py
  - byslib/core/__init__.py
  isVerificationFile: true
  path: tests/data/lazysegtree/range_update_query.test.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/data/lazysegtree/range_update_query.test.py
layout: document
redirect_from:
- /verify/tests/data/lazysegtree/range_update_query.test.py
- /verify/tests/data/lazysegtree/range_update_query.test.py.html
title: tests/data/lazysegtree/range_update_query.test.py
---

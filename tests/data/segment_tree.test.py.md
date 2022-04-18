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
    path: byslib/data/segment_tree.py
    title: Segment Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    import sys\nfrom operator import add\n\nfrom byslib.core.const import IINF, MOD\n\
    from byslib.core.fastio import debug, readline, sinput\nfrom byslib.data.segment_tree\
    \ import SegmentTree\n\n\ndef main() -> None:\n    _, q = map(int, readline().split())\n\
    \    a = list(map(int, readline().split()))\n    seg = SegmentTree(add, 0, a)\n\
    \    for _ in range(q):\n        c, s, t = map(int, sinput().split())\n      \
    \  if c == 0:\n            ap = seg[s]\n            seg.set(s, ap + t)\n     \
    \   else:\n            print(seg.fold(s, t))\n\n\nif __name__ == \"__main__\"\
    :\n    sys.setrecursionlimit(10**6)\n    main()\n"
  dependsOn:
  - byslib/data/__init__.py
  - byslib/data/segment_tree.py
  - byslib/__init__.py
  - byslib/core/const.py
  - byslib/core/fastio.py
  - byslib/core/__init__.py
  isVerificationFile: true
  path: tests/data/segment_tree.test.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/data/segment_tree.test.py
layout: document
redirect_from:
- /verify/tests/data/segment_tree.test.py
- /verify/tests/data/segment_tree.test.py.html
title: tests/data/segment_tree.test.py
---

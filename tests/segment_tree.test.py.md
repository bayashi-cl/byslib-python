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
    path: byslib/data/segment_tree.py
    title: byslib/data/segment_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    import sys\nfrom operator import add\n\nfrom byslib.core.const import IINF, MOD\n\
    from byslib.core.fastio import debug, readline, sinput\nfrom byslib.data.segment_tree\
    \ import SegmentTree\n\n\ndef main() -> None:\n    _, q = map(int, readline().split())\n\
    \    a = list(map(int, readline().split()))\n    seg = SegmentTree(add, 0, a)\n\
    \    for _ in range(q):\n        c, s, t = map(int, sinput().split())\n      \
    \  if c == 0:\n            ap = seg[s]\n            seg.update(s, ap + t)\n  \
    \      else:\n            print(seg.query(s, t))\n\n\nif __name__ == \"__main__\"\
    :\n    sys.setrecursionlimit(10**6)\n    main()\n"
  dependsOn:
  - byslib/__init__.py
  - byslib/core/fastio.py
  - byslib/data/__init__.py
  - byslib/core/__init__.py
  - byslib/data/segment_tree.py
  - byslib/core/const.py
  isVerificationFile: true
  path: tests/segment_tree.test.py
  requiredBy: []
  timestamp: '2022-03-15 06:00:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/segment_tree.test.py
layout: document
redirect_from:
- /verify/tests/segment_tree.test.py
- /verify/tests/segment_tree.test.py.html
title: tests/segment_tree.test.py
---

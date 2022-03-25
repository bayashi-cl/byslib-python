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
    path: byslib/data/binary_indexed_tree.py
    title: byslib/data/binary_indexed_tree.py
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
    import sys\n\nfrom byslib.core.const import IINF, MOD\nfrom byslib.core.fastio\
    \ import debug, readline, sinput\nfrom byslib.data.binary_indexed_tree import\
    \ BinaryIndexedTree\n\n\ndef main() -> None:\n    _, q = map(int, readline().split())\n\
    \    a = list(map(int, readline().split()))\n    bit = BinaryIndexedTree.construct(a)\n\
    \    for _ in range(q):\n        t, *que = map(int, readline().split())\n    \
    \    if t == 0:\n            p, x = que\n            bit.add(p, x)\n        else:\n\
    \            l, r = que\n            print(bit.range_sum(l, r))\n\n\nif __name__\
    \ == \"__main__\":\n    sys.setrecursionlimit(10**6)\n    main()\n"
  dependsOn:
  - byslib/data/binary_indexed_tree.py
  - byslib/__init__.py
  - byslib/core/fastio.py
  - byslib/data/__init__.py
  - byslib/core/__init__.py
  - byslib/core/const.py
  isVerificationFile: true
  path: tests/binary_indexed_tree.test.py
  requiredBy: []
  timestamp: '2022-03-15 05:43:47+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/binary_indexed_tree.test.py
layout: document
redirect_from:
- /verify/tests/binary_indexed_tree.test.py
- /verify/tests/binary_indexed_tree.test.py.html
title: tests/binary_indexed_tree.test.py
---

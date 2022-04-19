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
    path: byslib/data/binary_indexed_tree.py
    title: Bynary Indexed Tree
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
    import sys\n\nfrom byslib.core.fastio import readline\nfrom byslib.data.binary_indexed_tree\
    \ import BinaryIndexedTree\n\n\ndef main() -> None:\n    _, q = map(int, readline().split())\n\
    \    a = list(map(int, readline().split()))\n    bit = BinaryIndexedTree(a)\n\
    \    for _ in range(q):\n        t, *que = map(int, readline().split())\n    \
    \    if t == 0:\n            p, x = que\n            bit.point_append(p, x)\n\
    \        else:\n            l, r = que\n            print(bit.fold(l, r))\n\n\n\
    if __name__ == \"__main__\":\n    sys.setrecursionlimit(10**6)\n    main()\n"
  dependsOn:
  - byslib/__init__.py
  - byslib/data/binary_indexed_tree.py
  - byslib/data/__init__.py
  - byslib/core/__init__.py
  - byslib/core/fastio.py
  isVerificationFile: true
  path: tests/data/binary_indexed_tree.test.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/data/binary_indexed_tree.test.py
layout: document
redirect_from:
- /verify/tests/data/binary_indexed_tree.test.py
- /verify/tests/data/binary_indexed_tree.test.py.html
title: tests/data/binary_indexed_tree.test.py
---

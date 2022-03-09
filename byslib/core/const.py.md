---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: template.py
    title: template.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/binary_indexed_tree.test.py
    title: tests/binary_indexed_tree.test.py
  - icon: ':heavy_check_mark:'
    path: tests/cumulative_sum.test.py
    title: tests/cumulative_sum.test.py
  - icon: ':heavy_check_mark:'
    path: tests/dijkstra.test.py
    title: tests/dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: tests/kruskal.test.py
    title: tests/kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: tests/lazysegtree/range_update_query.test.py
    title: tests/lazysegtree/range_update_query.test.py
  - icon: ':heavy_check_mark:'
    path: tests/mod_comb.test.py
    title: tests/mod_comb.test.py
  - icon: ':heavy_check_mark:'
    path: tests/segment_tree.test.py
    title: tests/segment_tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: 'import sys


    MOD: int = 998244353

    MOD7: int = 1000000007

    INF: float = float("Inf")

    IINF: int = sys.maxsize // 2

    '
  dependsOn: []
  isVerificationFile: false
  path: byslib/core/const.py
  requiredBy:
  - template.py
  timestamp: '2022-02-18 18:18:54+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/cumulative_sum.test.py
  - tests/dijkstra.test.py
  - tests/lazysegtree/range_update_query.test.py
  - tests/mod_comb.test.py
  - tests/segment_tree.test.py
  - tests/binary_indexed_tree.test.py
  - tests/kruskal.test.py
documentation_of: byslib/core/const.py
layout: document
redirect_from:
- /library/byslib/core/const.py
- /library/byslib/core/const.py.html
title: byslib/core/const.py
---

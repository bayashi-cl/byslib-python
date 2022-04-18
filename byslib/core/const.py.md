---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: template.py
    title: template.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/data/lazysegtree/range_update_query.test.py
    title: tests/data/lazysegtree/range_update_query.test.py
  - icon: ':heavy_check_mark:'
    path: tests/data/segment_tree.test.py
    title: tests/data/segment_tree.test.py
  - icon: ':heavy_check_mark:'
    path: tests/graph/dijkstra.test.py
    title: tests/graph/dijkstra.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    document_title: Const
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# @title Const

    import sys


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
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/graph/dijkstra.test.py
  - tests/data/segment_tree.test.py
  - tests/data/lazysegtree/range_update_query.test.py
documentation_of: byslib/core/const.py
layout: document
redirect_from:
- /library/byslib/core/const.py
- /library/byslib/core/const.py.html
title: Const
---

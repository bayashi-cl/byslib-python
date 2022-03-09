---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: template.py
    title: template.py
  - icon: ':warning:'
    path: tests/test_io.py
    title: tests/test_io.py
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
    path: tests/io.test.py
    title: tests/io.test.py
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
  code: "import sys\nfrom functools import partial\n\nreadline = sys.stdin.buffer.readline\n\
    debug = partial(print, file=sys.stderr)\n\n\ndef sinput() -> str:\n    return\
    \ readline().decode().rstrip()\n\n\ndef int1(s: str) -> int:\n    return int(s)\
    \ - 1\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/core/io.py
  requiredBy:
  - template.py
  - tests/test_io.py
  timestamp: '2022-02-28 04:59:03+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/cumulative_sum.test.py
  - tests/dijkstra.test.py
  - tests/lazysegtree/range_update_query.test.py
  - tests/io.test.py
  - tests/mod_comb.test.py
  - tests/segment_tree.test.py
  - tests/binary_indexed_tree.test.py
  - tests/kruskal.test.py
documentation_of: byslib/core/io.py
layout: document
redirect_from:
- /library/byslib/core/io.py
- /library/byslib/core/io.py.html
title: byslib/core/io.py
---

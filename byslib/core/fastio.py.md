---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: template.py
    title: template.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/core/io.test.py
    title: tests/core/io.test.py
  - icon: ':heavy_check_mark:'
    path: tests/data/binary_indexed_tree.test.py
    title: tests/data/binary_indexed_tree.test.py
  - icon: ':heavy_check_mark:'
    path: tests/data/cumulative_sum.test.py
    title: tests/data/cumulative_sum.test.py
  - icon: ':heavy_check_mark:'
    path: tests/data/lazysegtree/range_update_query.test.py
    title: tests/data/lazysegtree/range_update_query.test.py
  - icon: ':heavy_check_mark:'
    path: tests/data/segment_tree.test.py
    title: tests/data/segment_tree.test.py
  - icon: ':heavy_check_mark:'
    path: tests/graph/dijkstra.test.py
    title: tests/graph/dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: tests/graph/kruskal.test.py
    title: tests/graph/kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: tests/numeric/mod_comb.test.py
    title: tests/numeric/mod_comb.test.py
  - icon: ':heavy_check_mark:'
    path: tests/verify_pytest/test_io.test.py
    title: tests/verify_pytest/test_io.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    document_title: Fast I/O
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Fast I/O\nimport io\nimport os\nimport sys\nfrom functools import\
    \ partial\nfrom typing import Union\n\nreadline = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline\n\
    debug = partial(print, file=sys.stderr)\n\n\ndef sinput() -> str:\n    return\
    \ readline().decode().rstrip()\n\n\ndef int1(s: Union[str, bytes]) -> int:\n \
    \   return int(s) - 1\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/core/fastio.py
  requiredBy:
  - template.py
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/verify_pytest/test_io.test.py
  - tests/graph/dijkstra.test.py
  - tests/graph/kruskal.test.py
  - tests/data/cumulative_sum.test.py
  - tests/data/segment_tree.test.py
  - tests/data/binary_indexed_tree.test.py
  - tests/data/lazysegtree/range_update_query.test.py
  - tests/numeric/mod_comb.test.py
  - tests/core/io.test.py
documentation_of: byslib/core/fastio.py
layout: document
redirect_from:
- /library/byslib/core/fastio.py
- /library/byslib/core/fastio.py.html
title: Fast I/O
---

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
    path: byslib/core/io.py
    title: byslib/core/io.py
  - icon: ':heavy_check_mark:'
    path: byslib/data/__init__.py
    title: byslib/data/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/data/union_find.py
    title: byslib/data/union_find.py
  - icon: ':heavy_check_mark:'
    path: byslib/graph/__init__.py
    title: byslib/graph/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/graph/edge.py
    title: byslib/graph/edge.py
  - icon: ':heavy_check_mark:'
    path: byslib/graph/kruskal.py
    title: byslib/graph/kruskal.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_2_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_2_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_2_A\n\
    import sys\n\nfrom byslib.core.const import IINF, MOD\nfrom byslib.core.io import\
    \ debug, sinput, readline\nfrom byslib.graph.edge import Edge\nfrom byslib.graph.kruskal\
    \ import kruskal\n\n\ndef main() -> None:\n    v, e = map(int, sinput().split())\n\
    \    edges = [Edge(*map(int, sinput().split())) for _ in range(e)]\n    cost,\
    \ _ = kruskal(edges, v)\n    print(cost)\n\n\nif __name__ == \"__main__\":\n \
    \   sys.setrecursionlimit(10**6)\n    main()\n"
  dependsOn:
  - byslib/data/__init__.py
  - byslib/__init__.py
  - byslib/graph/edge.py
  - byslib/core/const.py
  - byslib/data/union_find.py
  - byslib/graph/__init__.py
  - byslib/graph/kruskal.py
  - byslib/core/__init__.py
  - byslib/core/io.py
  isVerificationFile: true
  path: tests/kruskal.test.py
  requiredBy: []
  timestamp: '2022-02-28 04:59:03+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/kruskal.test.py
layout: document
redirect_from:
- /verify/tests/kruskal.test.py
- /verify/tests/kruskal.test.py.html
title: tests/kruskal.test.py
---

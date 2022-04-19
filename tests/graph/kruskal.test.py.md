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
    path: byslib/data/union_find.py
    title: Union-Find Tree
  - icon: ':heavy_check_mark:'
    path: byslib/graph/__init__.py
    title: Graph
  - icon: ':heavy_check_mark:'
    path: byslib/graph/edge.py
    title: Edge
  - icon: ':heavy_check_mark:'
    path: byslib/graph/graph.py
    title: Adjacency List
  - icon: ':heavy_check_mark:'
    path: byslib/graph/kruskal.py
    title: kruskal
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_2_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_2_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_2_A\n\
    import sys\n\nfrom byslib.core.fastio import sinput\nfrom byslib.graph import\
    \ Edge\nfrom byslib.graph.kruskal import kruskal\n\n\ndef main() -> None:\n  \
    \  v, e = map(int, sinput().split())\n    edges = [Edge(*map(int, sinput().split()))\
    \ for _ in range(e)]\n    cost, _ = kruskal(edges, v)\n    print(cost)\n\n\nif\
    \ __name__ == \"__main__\":\n    sys.setrecursionlimit(10**6)\n    main()\n"
  dependsOn:
  - byslib/__init__.py
  - byslib/graph/edge.py
  - byslib/data/__init__.py
  - byslib/graph/graph.py
  - byslib/data/union_find.py
  - byslib/core/__init__.py
  - byslib/core/fastio.py
  - byslib/graph/__init__.py
  - byslib/graph/kruskal.py
  isVerificationFile: true
  path: tests/graph/kruskal.test.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/graph/kruskal.test.py
layout: document
redirect_from:
- /verify/tests/graph/kruskal.test.py
- /verify/tests/graph/kruskal.test.py.html
title: tests/graph/kruskal.test.py
---

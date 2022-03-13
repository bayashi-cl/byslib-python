---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: byslib/__init__.py
    title: byslib/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/data/__init__.py
    title: byslib/data/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/data/union_find.py
    title: byslib/data/union_find.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    import sys\nfrom typing import Callable\n\nfrom byslib.data.union_find import\
    \ UnionFindTree\n\nsys.setrecursionlimit(10 ** 6)\nsinput: Callable[..., str]\
    \ = sys.stdin.readline\n\n\ndef main() -> None:\n    n, q = map(int, sinput().split())\n\
    \    uft = UnionFindTree(n)\n    for _ in range(q):\n        t, u, v = map(int,\
    \ sinput().split())\n        if t == 0:\n            uft.union(u, v)\n       \
    \ else:\n            print(1 if uft.same(u, v) else 0)\n\n\nif __name__ == \"\
    __main__\":\n    main()\n"
  dependsOn:
  - byslib/__init__.py
  - byslib/data/union_find.py
  - byslib/data/__init__.py
  isVerificationFile: true
  path: tests/union_find.test.py
  requiredBy: []
  timestamp: '2022-02-28 04:59:03+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/union_find.test.py
layout: document
redirect_from:
- /verify/tests/union_find.test.py
- /verify/tests/union_find.test.py.html
title: tests/union_find.test.py
---

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
    path: byslib/core/io.py
    title: byslib/core/io.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/many_aplusb
    links:
    - https://judge.yosupo.jp/problem/many_aplusb
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/many_aplusb\n\
    from byslib.core.io import readline\n\n\ndef main() -> None:\n    t = int(readline())\n\
    \    for _ in range(t):\n        a, b = map(int, readline().split())\n       \
    \ print(a + b)\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn:
  - byslib/__init__.py
  - byslib/core/io.py
  - byslib/core/__init__.py
  isVerificationFile: true
  path: tests/io.test.py
  requiredBy: []
  timestamp: '2022-02-28 04:59:03+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/io.test.py
layout: document
redirect_from:
- /verify/tests/io.test.py
- /verify/tests/io.test.py.html
title: tests/io.test.py
---

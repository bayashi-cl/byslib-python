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
    path: byslib/core/config.py
    title: setup
  - icon: ':heavy_check_mark:'
    path: byslib/core/fastio.py
    title: Fast I/O
  - icon: ':heavy_check_mark:'
    path: byslib/numeric/__init__.py
    title: byslib/numeric/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/numeric/mod_comb.py
    title: Binomial coefficient
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/117
    links:
    - https://yukicoder.me/problems/no/117
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/117\nfrom\
    \ byslib.core.config import procon_setup\nfrom byslib.core.fastio import readline,\
    \ sinput\nfrom byslib.numeric.mod_comb import MultiComb\n\n\n@procon_setup\ndef\
    \ main(**kwargs) -> None:\n    t = int(readline())\n    mc = MultiComb(2_000_000)\n\
    \n    for _ in range(t):\n        s = sinput()\n        com = s[0]\n        n,\
    \ k = map(int, s[2:-1].split(\",\"))\n        if com == \"C\":\n            print(mc.comb(n,\
    \ k))\n        elif com == \"P\":\n            print(mc.perm(n, k))\n        elif\
    \ com == \"H\":\n            print(mc.hom(n, k))\n        else:\n            raise\
    \ ValueError\n\n\nif __name__ == \"__main__\":\n    t = 1\n    # t = int(readline())\n\
    \    main(t)\n"
  dependsOn:
  - byslib/__init__.py
  - byslib/core/config.py
  - byslib/numeric/__init__.py
  - byslib/numeric/mod_comb.py
  - byslib/core/__init__.py
  - byslib/core/fastio.py
  isVerificationFile: true
  path: tests/numeric/mod_comb.test.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/numeric/mod_comb.test.py
layout: document
redirect_from:
- /verify/tests/numeric/mod_comb.test.py
- /verify/tests/numeric/mod_comb.test.py.html
title: tests/numeric/mod_comb.test.py
---

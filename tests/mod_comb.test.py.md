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
    path: byslib/core/fastio.py
    title: byslib/core/fastio.py
  - icon: ':heavy_check_mark:'
    path: byslib/math/__init__.py
    title: byslib/math/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/math/mod_comb.py
    title: byslib/math/mod_comb.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/117
    links:
    - https://yukicoder.me/problems/no/117
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/117\nimport\
    \ sys\n\nfrom byslib.core.const import IINF, MOD\nfrom byslib.core.fastio import\
    \ debug, readline, sinput\nfrom byslib.math.mod_comb import MultiComb\n\n\ndef\
    \ main() -> None:\n    t = int(readline())\n    mc = MultiComb(2_000_000)\n\n\
    \    for _ in range(t):\n        s = sinput()\n        com = s[0]\n        n,\
    \ k = map(int, s[2:-1].split(\",\"))\n        if com == \"C\":\n            print(mc.comb(n,\
    \ k))\n        elif com == \"P\":\n            print(mc.perm(n, k))\n        elif\
    \ com == \"H\":\n            print(mc.hom(n, k))\n        else:\n            raise\
    \ ValueError\n\n\nif __name__ == \"__main__\":\n    sys.setrecursionlimit(10**6)\n\
    \    main()\n"
  dependsOn:
  - byslib/core/const.py
  - byslib/core/__init__.py
  - byslib/math/mod_comb.py
  - byslib/__init__.py
  - byslib/math/__init__.py
  - byslib/core/fastio.py
  isVerificationFile: true
  path: tests/mod_comb.test.py
  requiredBy: []
  timestamp: '2022-03-13 15:20:56+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/mod_comb.test.py
layout: document
redirect_from:
- /verify/tests/mod_comb.test.py
- /verify/tests/mod_comb.test.py.html
title: tests/mod_comb.test.py
---

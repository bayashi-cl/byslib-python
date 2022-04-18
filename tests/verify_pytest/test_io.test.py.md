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
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    from byslib.core.fastio import int1\n\n\ndef test_sinput_int1():\n    assert int1(\"\
    5\") == 4\n\n\nif __name__ == \"__main__\":\n    import sys\n\n    from exec_pytest\
    \ import exec_pytest\n\n    sys.exit(exec_pytest(__file__))\n"
  dependsOn:
  - byslib/core/fastio.py
  - byslib/__init__.py
  - byslib/core/__init__.py
  isVerificationFile: true
  path: tests/verify_pytest/test_io.test.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/verify_pytest/test_io.test.py
layout: document
redirect_from:
- /verify/tests/verify_pytest/test_io.test.py
- /verify/tests/verify_pytest/test_io.test.py.html
title: tests/verify_pytest/test_io.test.py
---

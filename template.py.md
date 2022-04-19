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
    path: byslib/core/const.py
    title: Const
  - icon: ':heavy_check_mark:'
    path: byslib/core/fastio.py
    title: Fast I/O
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from byslib.core.config import procon_setup\nfrom byslib.core.const import\
    \ IINF, MOD\nfrom byslib.core.fastio import debug, readline, sinput\n\n\n@procon_setup\n\
    def main(**kwargs) -> None:\n    ...\n\n\nif __name__ == \"__main__\":\n    t\
    \ = 1\n    # t = int(readline())\n    main(t)\n"
  dependsOn:
  - byslib/__init__.py
  - byslib/core/config.py
  - byslib/core/const.py
  - byslib/core/__init__.py
  - byslib/core/fastio.py
  isVerificationFile: false
  path: template.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: template.py
layout: document
redirect_from:
- /library/template.py
- /library/template.py.html
title: template.py
---

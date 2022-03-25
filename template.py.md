---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: byslib/__init__.py
    title: byslib/__init__.py
  - icon: ':heavy_check_mark:'
    path: byslib/core/__init__.py
    title: byslib/core/__init__.py
  - icon: ':warning:'
    path: byslib/core/config.py
    title: byslib/core/config.py
  - icon: ':heavy_check_mark:'
    path: byslib/core/const.py
    title: byslib/core/const.py
  - icon: ':heavy_check_mark:'
    path: byslib/core/fastio.py
    title: byslib/core/fastio.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from byslib.core.config import procon_setup\nfrom byslib.core.const import\
    \ IINF, MOD\nfrom byslib.core.fastio import debug, readline, sinput\n\n\n@procon_setup\n\
    def main(**kwargs) -> None:\n    ...\n\n\nif __name__ == \"__main__\":\n    t\
    \ = 1\n    # t = int(readline())\n    main(t)\n"
  dependsOn:
  - byslib/core/config.py
  - byslib/__init__.py
  - byslib/core/fastio.py
  - byslib/core/__init__.py
  - byslib/core/const.py
  isVerificationFile: false
  path: template.py
  requiredBy: []
  timestamp: '2022-03-15 05:43:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: template.py
layout: document
redirect_from:
- /library/template.py
- /library/template.py.html
title: template.py
---

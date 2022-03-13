---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: template.py
    title: template.py
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
  code: "import sys\nfrom typing import Callable\n\n\ndef procon_setup(main: Callable[...,\
    \ None]) -> Callable[..., None]:\n    sys.setrecursionlimit(10**7)\n\n    def\
    \ wrapper(case: int = 1) -> None:\n        for i in range(case):\n           \
    \ main(case=i + 1)\n\n    return wrapper\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/core/config.py
  requiredBy:
  - template.py
  timestamp: '2022-03-13 15:21:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/core/config.py
layout: document
redirect_from:
- /library/byslib/core/config.py
- /library/byslib/core/config.py.html
title: byslib/core/config.py
---

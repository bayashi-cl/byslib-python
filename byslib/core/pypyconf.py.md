---
data:
  _extendedDependsOn: []
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
  code: "try:\n    import pypyjit  # type: ignore\n\n    pypyjit.set_param(\"max_unroll_recursion=-1\"\
    )\nexcept ImportError:\n    pass\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/core/pypyconf.py
  requiredBy: []
  timestamp: '2022-03-10 05:04:36+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/core/pypyconf.py
layout: document
redirect_from:
- /library/byslib/core/pypyconf.py
- /library/byslib/core/pypyconf.py.html
title: byslib/core/pypyconf.py
---
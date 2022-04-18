---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: template.py
    title: template.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/numeric/mod_comb.test.py
    title: tests/numeric/mod_comb.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    document_title: setup
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title setup\nimport sys\nfrom typing import Callable\n\n\ndef procon_setup(main:\
    \ Callable[..., None]) -> Callable[..., None]:\n    \"\"\"setup\n\n    Notes\n\
    \    -----\n    * Set recursionlimit to 1e7\n    * Repeat main function for testcases\n\
    \    * If exception raised, indicate in which test case it was raised.\n    \"\
    \"\"\n\n    def wrapper(case: int = 1) -> None:\n        sys.setrecursionlimit(10**7)\n\
    \        for i in range(case):\n            try:\n                main(case=i\
    \ + 1)\n            except Exception as e:\n                print(\n         \
    \           f\"\u274C {type(e).__name__} raised in tastcase {i + 1}.\",\n    \
    \                file=sys.stderr,\n                )\n                raise\n\n\
    \    return wrapper\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/core/config.py
  requiredBy:
  - template.py
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/numeric/mod_comb.test.py
documentation_of: byslib/core/config.py
layout: document
redirect_from:
- /library/byslib/core/config.py
- /library/byslib/core/config.py.html
title: setup
---

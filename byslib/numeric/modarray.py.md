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
  code: "from array import array\n\n\ndef using_modarray(modulo: int):\n    class\
    \ ModArray(array):\n        __slots__ = ()\n        mod: int = modulo\n\n    \
    \    @classmethod\n        def zeros(cls, n: int) -> \"ModArray\":\n         \
    \   return cls(\"L\", [0] * n)\n\n        def __setitem__(self, index, value)\
    \ -> None:\n            super().__setitem__(index, value % self.mod)\n\n     \
    \   def inv(self, index: int) -> int:\n            return pow(self[index], self.mod\
    \ - 2, self.mod)\n\n    return ModArray\n\n\nmodarray998244353 = using_modarray(998244353)\n\
    modarray1000000007 = using_modarray(1000000007)\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/numeric/modarray.py
  requiredBy: []
  timestamp: '2022-03-25 15:36:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/numeric/modarray.py
layout: document
redirect_from:
- /library/byslib/numeric/modarray.py
- /library/byslib/numeric/modarray.py.html
title: byslib/numeric/modarray.py
---

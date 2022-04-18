---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    document_title: Matrix
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Matrix\nfrom collections import UserList\nfrom typing import Generic,\
    \ Iterable, Optional, TypeVar, Union\n\n_T = TypeVar(\"_T\", int, float)\n\n\n\
    class Vector(UserList, Generic[_T]):\n    def __init__(self, initlist: Optional[Iterable[_T]])\
    \ -> None:\n        super().__init__(initlist=initlist)\n\n    def __add__(self,\
    \ other: Union[Iterable[_T], _T]) -> \"Vector[_T]\":\n        if isinstance(other,\
    \ float) or isinstance(other, int):\n            return Vector(map(lambda x: x\
    \ + other, self))\n        elif isinstance(other, Vector):\n            if len(other)\
    \ != len(self):\n                raise ValueError\n\n            for i in range(len(self)):\n\
    \                self[i] += other[i]\n            return self\n        else:\n\
    \            raise ValueError\n\n\nclass Matrix:\n    ...\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/numeric/matrix.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/numeric/matrix.py
layout: document
redirect_from:
- /library/byslib/numeric/matrix.py
- /library/byslib/numeric/matrix.py.html
title: Matrix
---

---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    document_title: Modint
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Modint\nfrom typing import Union\n\n\nclass modint:\n    \"\"\"\
    Modint\n    Not so fast.\n    \"\"\"\n\n    __slots__ = (\"v\",)\n    mod: int\
    \ = 0\n\n    def __init__(self, v: int = 0) -> None:\n        self.v = v % self.mod\n\
    \n    def __repr__(self):\n        return str(self.v)\n\n    def __index__(self):\n\
    \        return self.v\n\n    def __iadd__(self, other: Union[\"modint\", int])\
    \ -> \"modint\":\n        if isinstance(other, int):\n            self.v += other\n\
    \        else:\n            self.v += other.v\n\n        self.v %= self.mod\n\
    \        return self\n\n    def __isub__(self, other: Union[\"modint\", int])\
    \ -> \"modint\":\n        if isinstance(other, int):\n            self.v -= other\n\
    \        else:\n            self.v -= other.v\n\n        self.v %= self.mod\n\
    \        return self\n\n    def __imul__(self, other: Union[\"modint\", int])\
    \ -> \"modint\":\n        if isinstance(other, int):\n            self.v *= other\n\
    \        else:\n            self.v *= other.v\n\n        self.v %= self.mod\n\
    \        return self\n\n    def __ipow__(self, other: int) -> \"modint\":\n  \
    \      self.v = pow(self.v, other, self.mod)\n        return self\n\n    def __ifloordiv__(self,\
    \ other: Union[\"modint\", int]) -> \"modint\":\n        if isinstance(other,\
    \ int):\n            self.v *= pow(other, self.mod - 2, self.mod)\n        else:\n\
    \            self.v *= pow(other.v, self.mod - 2, self.mod)\n\n        self.v\
    \ %= self.mod\n        return self\n\n    def __add__(self, other: Union[\"modint\"\
    , int]) -> \"modint\":\n        res = self.__class__(self.v)\n        res += other\n\
    \        return res\n\n    def __sub__(self, other: Union[\"modint\", int]) ->\
    \ \"modint\":\n        res = self.__class__(self.v)\n        res -= other\n  \
    \      return res\n\n    def __mul__(self, other: Union[\"modint\", int]) -> \"\
    modint\":\n        res = self.__class__(self.v)\n        res *= other\n      \
    \  return res\n\n    def __floordiv__(self, other: Union[\"modint\", int]) ->\
    \ \"modint\":\n        res = self.__class__(self.v)\n        res //= other\n \
    \       return res\n\n    def __pow__(self, other: int) -> \"modint\":\n     \
    \   res = self.__class__(self.v)\n        res **= other\n        return res\n\n\
    \    def inv(self) -> \"modint\":\n        return self.__class__(pow(self.v, self.mod\
    \ - 2, self.mod))\n\n    def __radd__(self, other: int) -> \"modint\":\n     \
    \   res = self.__class__(other)\n        res += self\n        return res\n\n \
    \   def __rsub__(self, other: int) -> \"modint\":\n        res = self.__class__(other)\n\
    \        res -= self\n        return res\n\n    def __rmul__(self, other: int)\
    \ -> \"modint\":\n        res = self.__class__(other)\n        res *= self\n \
    \       return res\n\n    def __rfloordiv__(self, other: int) -> \"modint\":\n\
    \        res = self.__class__(other)\n        res //= self\n        return res\n\
    \n\ndef using_modint(modulo: int):\n    \"\"\"using modint\n\n    set modulo to\
    \ modint class\n\n    Parameters\n    ----------\n    modulo\n\n    Returns\n\
    \    -------\n        modint class mod = modulo\n    \"\"\"\n\n    class Mint(modint):\n\
    \        __slots__ = ()\n        mod: int = modulo\n\n    return Mint\n\n\nmodint998244353\
    \ = using_modint(998244353)\nmodint1000000007 = using_modint(1000000007)\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/numeric/modint.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/numeric/modint.py
layout: document
redirect_from:
- /library/byslib/numeric/modint.py
- /library/byslib/numeric/modint.py.html
title: Modint
---

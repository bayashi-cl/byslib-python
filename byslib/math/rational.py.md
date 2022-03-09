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
  code: "import numbers\n\n\nclass Rational(numbers.Rational):\n    _numerator: int\n\
    \    _denominator: int\n\n    def __init__(self, numerator: int, denomerator:\
    \ int) -> None:\n        sgn = 1\n        if denomerator < 0:\n            sgn\
    \ *= -1\n            denomerator *= -1\n        self._numerator = sgn * numerator\n\
    \        self._denominator = denomerator\n\n    def __add__(self, other):\n  \
    \      \"\"\"self + other\"\"\"\n        raise NotImplementedError\n\n    def\
    \ __radd__(self, other):\n        \"\"\"other + self\"\"\"\n        raise NotImplementedError\n\
    \n    def __neg__(self):\n        \"\"\"-self\"\"\"\n        raise NotImplementedError\n\
    \n    def __pos__(self):\n        \"\"\"+self\"\"\"\n        raise NotImplementedError\n\
    \n    def __mul__(self, other):\n        \"\"\"self * other\"\"\"\n        raise\
    \ NotImplementedError\n\n    def __rmul__(self, other):\n        \"\"\"other *\
    \ self\"\"\"\n        raise NotImplementedError\n\n    def __truediv__(self, other):\n\
    \        \"\"\"self / other: Should promote to float when necessary.\"\"\"\n \
    \       raise NotImplementedError\n\n    def __rtruediv__(self, other):\n    \
    \    \"\"\"other / self\"\"\"\n        raise NotImplementedError\n\n    def __pow__(self,\
    \ exponent):\n        \"\"\"self**exponent; should promote to float or complex\
    \ when necessary.\"\"\"\n        raise NotImplementedError\n\n    def __rpow__(self,\
    \ base):\n        \"\"\"base ** self\"\"\"\n        raise NotImplementedError\n\
    \n    def __abs__(self):\n        \"\"\"Returns the Real distance from 0. Called\
    \ for abs(self).\"\"\"\n        raise NotImplementedError\n\n    def __eq__(self,\
    \ other):\n        \"\"\"self == other\"\"\"\n        raise NotImplementedError\n\
    \n    def __trunc__(self) -> int:\n        if self._numerator < 0:\n         \
    \   return -(-self._numerator // self._denominator)\n        else:\n         \
    \   return self._numerator // self._denominator\n\n    def __floor__(self) ->\
    \ int:\n        return self._numerator // self._denominator\n\n    def __ceil__(self)\
    \ -> int:\n        return -(-self.numerator // self.denominator)\n\n    def __round__(self,\
    \ ndigits=None):\n        if ndigits is None:\n            floor, remainder =\
    \ divmod(self._numerator, self._denominator)\n            if remainder * 2 < self._denominator:\n\
    \                return floor\n            elif remainder * 2 > self._denominator:\n\
    \                return floor + 1\n            elif floor % 2 == 0:\n        \
    \        return floor\n            else:\n                return floor + 1\n \
    \       else:\n            raise NotImplementedError\n\n    def __floordiv__(self,\
    \ other):\n        \"\"\"self // other: The floor() of self/other.\"\"\"\n   \
    \     raise NotImplementedError\n\n    def __rfloordiv__(self, other):\n     \
    \   \"\"\"other // self: The floor() of other/self.\"\"\"\n        raise NotImplementedError\n\
    \n    def __mod__(self, other):\n        \"\"\"self % other\"\"\"\n        raise\
    \ NotImplementedError\n\n    def __rmod__(self, other):\n        \"\"\"other %\
    \ self\"\"\"\n        raise NotImplementedError\n\n    def __lt__(self, other):\n\
    \        \"\"\"self < other\n\n        < on Reals defines a total ordering, except\
    \ perhaps for NaN.\"\"\"\n        raise NotImplementedError\n\n    def __le__(self,\
    \ other):\n        \"\"\"self <= other\"\"\"\n        raise NotImplementedError\n\
    \n    @property\n    def numerator(self) -> int:\n        return self._numerator\n\
    \n    @property\n    def denominator(self) -> int:\n        return self._denominator\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/math/rational.py
  requiredBy: []
  timestamp: '2022-02-14 17:11:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/math/rational.py
layout: document
redirect_from:
- /library/byslib/math/rational.py
- /library/byslib/math/rational.py.html
title: byslib/math/rational.py
---

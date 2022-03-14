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
  code: "import math\nimport numbers\nfrom dataclasses import dataclass\nfrom typing\
    \ import Generic, TypeVar, Union\n\nReal = Union[int, float]\nEPS = 1e-9\n\n\n\
    def sign(x: float) -> int:\n    if x < -EPS:\n        return -1\n    elif x >\
    \ EPS:\n        return 1\n    else:\n        return 0\n\n\n@dataclass\nclass Point:\n\
    \    x: Real\n    y: Real\n\n    def __add__(self, other: Union[\"Point\", Real])\
    \ -> \"Point\":\n        if isinstance(other, Point):\n            return Point(self.x\
    \ + other.x, self.y + other.y)\n        else:\n            return Point(self.x\
    \ + other, self.y + other)\n\n    def __sub__(self, other: Union[\"Point\", Real])\
    \ -> \"Point\":\n        if isinstance(other, Point):\n            return Point(self.x\
    \ - other.x, self.y - other.y)\n        else:\n            return Point(self.x\
    \ - other, self.y - other)\n\n    def __mul__(self, other: Real) -> \"Point\"\
    :\n        return Point(self.x * other, self.y * other)\n\n    def __truediv__(self,\
    \ other: Real) -> \"Point\":\n        return Point(self.x / other, self.y / other)\n\
    \n    def __iadd__(self, other: Union[\"Point\", Real]) -> \"Point\":\n      \
    \  if isinstance(other, Point):\n            self.x += other.x\n            self.y\
    \ += other.y\n        else:\n            self.x += other\n            self.y +=\
    \ other\n        return self\n\n    def __isub__(self, other: Union[\"Point\"\
    , Real]) -> \"Point\":\n        if isinstance(other, Point):\n            self.x\
    \ -= other.x\n            self.y -= other.y\n        else:\n            self.x\
    \ -= other\n            self.y -= other\n        return self\n\n    def __imul__(self,\
    \ other: Real) -> \"Point\":\n        if isinstance(other, Point):\n         \
    \   self.x += other.x\n            self.y += other.y\n        else:\n        \
    \    self.x += other\n            self.y += other\n        return self\n\n   \
    \ def __itruediv__(self, other: Real) -> \"Point\":\n        self.x /= other\n\
    \        self.y /= other\n        return self\n\n    def __eq__(self, other: object)\
    \ -> bool:\n        if not isinstance(other, Point):\n            return False\n\
    \        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)\n\
    \n    def __ne__(self, other: object) -> bool:\n        return not self == other\n\
    \n    def norm2(self) -> Real:\n        return self.x ** 2 + self.y ** 2\n\n \
    \   def norm(self) -> float:\n        return math.sqrt(self.norm2())\n\n    def\
    \ normalized(self) -> \"Point\":\n        n = self.norm()\n        return Point(self.x\
    \ / n, self.y / n)\n\n    def angle(self) -> float:\n        return math.atan2(self.y,\
    \ self.x)\n\n    def quadrant(self) -> int:\n        if sign(self.y) >= 0:\n \
    \           return 1 if sign(self.x) >= 0 else 2\n        return 4 if sign(self.x)\
    \ >= 0 else 3\n\n    def normal(self) -> \"Point\":\n        return Point(-self.normalized().y,\
    \ self.normalized().x)\n\n    def manhattan_rotate(self) -> \"Point\":\n     \
    \   return Point(self.x - self.y, self.x + self.y)\n\n    def rotate(self, theta:\
    \ float) -> \"Point\":\n        ct = math.cos(theta)\n        st = math.sin(theta)\n\
    \        return Point(self.x * ct - self.y * st, self.x * st + self.y * ct)\n\n\
    \    def dot(self, other: \"Point\") -> Real:\n        return self.x * other.x\
    \ + self.y * other.y\n\n    def det(self, other: \"Point\") -> Real:\n       \
    \ return self.x * other.y - self.y * other.x\n\n    def projection(self, to: \"\
    Point\") -> \"Point\":\n        return to * (self.dot(to) / to.norm2())\n\n  \
    \  def __lt__(self, other: \"Point\") -> bool:\n        q = self.quadrant()\n\
    \        oq = other.quadrant()\n        if q != oq:\n            return q < oq\n\
    \        return sign(self.det(other)) > 0\n\n\nif __name__ == \"__main__\":\n\
    \    p = Point(3, 4)\n    print(p.norm())\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/geometry/geometry.py
  requiredBy: []
  timestamp: '2022-03-15 06:00:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/geometry/geometry.py
layout: document
redirect_from:
- /library/byslib/geometry/geometry.py
- /library/byslib/geometry/geometry.py.html
title: byslib/geometry/geometry.py
---

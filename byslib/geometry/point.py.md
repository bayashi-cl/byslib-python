---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    document_title: Point
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Point\nimport enum\nimport math\nfrom dataclasses import dataclass\n\
    from typing import Union\n\nReal = Union[int, float]\nEPS = 1e-9\n\n\ndef sign(x:\
    \ float) -> int:\n    if math.isclose(x, 0):\n        return 0\n    elif x < 0:\n\
    \        return -1\n    else:\n        return 1\n\n\n@dataclass\nclass Point:\n\
    \    \"\"\"vector or point\n\n    Support both int and float choordinate.\n  \
    \  \"\"\"\n\n    x: Real\n    y: Real\n\n    def __add__(self, other: Union[\"\
    Point\", Real]) -> \"Point\":\n        if isinstance(other, Point):\n        \
    \    return Point(self.x + other.x, self.y + other.y)\n        else:\n       \
    \     return Point(self.x + other, self.y + other)\n\n    def __sub__(self, other:\
    \ Union[\"Point\", Real]) -> \"Point\":\n        if isinstance(other, Point):\n\
    \            return Point(self.x - other.x, self.y - other.y)\n        else:\n\
    \            return Point(self.x - other, self.y - other)\n\n    def __mul__(self,\
    \ other: Real) -> \"Point\":\n        return Point(self.x * other, self.y * other)\n\
    \n    def __truediv__(self, other: Real) -> \"Point\":\n        return Point(self.x\
    \ / other, self.y / other)\n\n    def __iadd__(self, other: Union[\"Point\", Real])\
    \ -> \"Point\":\n        if isinstance(other, Point):\n            self.x += other.x\n\
    \            self.y += other.y\n        else:\n            self.x += other\n \
    \           self.y += other\n        return self\n\n    def __isub__(self, other:\
    \ Union[\"Point\", Real]) -> \"Point\":\n        if isinstance(other, Point):\n\
    \            self.x -= other.x\n            self.y -= other.y\n        else:\n\
    \            self.x -= other\n            self.y -= other\n        return self\n\
    \n    def __imul__(self, other: Real) -> \"Point\":\n        if isinstance(other,\
    \ Point):\n            self.x += other.x\n            self.y += other.y\n    \
    \    else:\n            self.x += other\n            self.y += other\n       \
    \ return self\n\n    def __itruediv__(self, other: Real) -> \"Point\":\n     \
    \   self.x /= other\n        self.y /= other\n        return self\n\n    def __eq__(self,\
    \ other: object) -> bool:\n        if not isinstance(other, Point):\n        \
    \    return False\n        return math.isclose(self.x, other.x) and math.isclose(self.y,\
    \ other.y)\n\n    def __ne__(self, other: object) -> bool:\n        return not\
    \ self == other\n\n    def norm2(self) -> Real:\n        return self.x**2 + self.y**2\n\
    \n    def norm(self) -> float:\n        return math.sqrt(self.norm2())\n\n   \
    \ def unit(self) -> \"Point\":\n        n = self.norm()\n        return Point(self.x\
    \ / n, self.y / n)\n\n    def angle(self) -> float:\n        return math.atan2(self.y,\
    \ self.x)\n\n    def quadrant(self) -> int:\n        if sign(self.y) >= 0:\n \
    \           return 1 if sign(self.x) >= 0 else 2\n        return 4 if sign(self.x)\
    \ >= 0 else 3\n\n    def normal(self) -> \"Point\":\n        return Point(-self.unit().y,\
    \ self.unit().x)\n\n    def manhattan_rotate(self) -> \"Point\":\n        return\
    \ Point(self.x - self.y, self.x + self.y)\n\n    def rotate(self, theta: float)\
    \ -> \"Point\":\n        ct = math.cos(theta)\n        st = math.sin(theta)\n\
    \        return Point(self.x * ct - self.y * st, self.x * st + self.y * ct)\n\n\
    \    def dot(self, other: \"Point\") -> Real:\n        return self.x * other.x\
    \ + self.y * other.y\n\n    def det(self, other: \"Point\") -> Real:\n       \
    \ return self.x * other.y - self.y * other.x\n\n    def projection(self, to: \"\
    Point\") -> \"Point\":\n        return to * (self.dot(to) / to.norm2())\n\n  \
    \  def __lt__(self, other: \"Point\") -> bool:\n        q = self.quadrant()\n\
    \        oq = other.quadrant()\n        if q != oq:\n            return q < oq\n\
    \        return sign(self.det(other)) > 0\n\n    def __repr__(self) -> str:\n\
    \        return f\"{self.x} {self.y}\"\n\n\n@enum.unique\nclass Turn(enum.IntEnum):\n\
    \    \"\"\"Turn direction\"\"\"\n\n    BACK = -2\n    CW = -1\n    MIDDLE = 0\n\
    \    CCW = 1\n    FRONT = 2\n\n\ndef iSP(a: Point, b: Point, c: Point) -> Turn:\n\
    \    \"\"\"iSP\n\n    Determine the positional relationship of the three Points.\n\
    \n    Returns\n    -------\n        Turn direction\n    \"\"\"\n    flg = sign((b\
    \ - a).det(c - a))\n    if flg == 1:\n        return Turn.CCW\n    elif flg ==\
    \ -1:\n        return Turn.CW\n    else:\n        if sign((b - a).dot(c - b))\
    \ > 0:\n            return Turn.FRONT\n        elif sign((a - b).dot(c - a)) >\
    \ 0:\n            return Turn.BACK\n        else:\n            return Turn.MIDDLE\n\
    \n\n@enum.unique\nclass Angle(enum.IntEnum):\n    \"\"\"Angle type\"\"\"\n\n \
    \   NOT_ANGLE = -2\n    OBTUSE = -1\n    RIGHT = 0\n    ACUTE = 1\n\n\ndef angle_type(a:\
    \ Point, b: Point, c: Point) -> Angle:\n    if abs(iSP(a, b, c)) == 1:\n     \
    \   return Angle.NOT_ANGLE\n    else:\n        return Angle(sign((a - b).dot(c\
    \ - b)))\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/geometry/point.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/geometry/point.py
layout: document
redirect_from:
- /library/byslib/geometry/point.py
- /library/byslib/geometry/point.py.html
title: Point
---

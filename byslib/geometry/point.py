# @title Point
import enum
import math
from dataclasses import dataclass
from typing import Union

Real = Union[int, float]
EPS = 1e-9


def sign(x: float) -> int:
    if math.isclose(x, 0):
        return 0
    elif x < 0:
        return -1
    else:
        return 1


@dataclass
class Point:
    """vector or point

    Support both int and float choordinate.
    """

    x: Real
    y: Real

    def __add__(self, other: Union["Point", Real]) -> "Point":
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

    def __sub__(self, other: Union["Point", Real]) -> "Point":
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Point(self.x - other, self.y - other)

    def __mul__(self, other: Real) -> "Point":
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other: Real) -> "Point":
        return Point(self.x / other, self.y / other)

    def __iadd__(self, other: Union["Point", Real]) -> "Point":
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self

    def __isub__(self, other: Union["Point", Real]) -> "Point":
        if isinstance(other, Point):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other
        return self

    def __imul__(self, other: Real) -> "Point":
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self

    def __itruediv__(self, other: Real) -> "Point":
        self.x /= other
        self.y /= other
        return self

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __ne__(self, other: object) -> bool:
        return not self == other

    def norm2(self) -> Real:
        return self.x**2 + self.y**2

    def norm(self) -> float:
        return math.sqrt(self.norm2())

    def unit(self) -> "Point":
        n = self.norm()
        return Point(self.x / n, self.y / n)

    def angle(self) -> float:
        return math.atan2(self.y, self.x)

    def quadrant(self) -> int:
        if sign(self.y) >= 0:
            return 1 if sign(self.x) >= 0 else 2
        return 4 if sign(self.x) >= 0 else 3

    def normal(self) -> "Point":
        return Point(-self.unit().y, self.unit().x)

    def manhattan_rotate(self) -> "Point":
        return Point(self.x - self.y, self.x + self.y)

    def rotate(self, theta: float) -> "Point":
        ct = math.cos(theta)
        st = math.sin(theta)
        return Point(self.x * ct - self.y * st, self.x * st + self.y * ct)

    def dot(self, other: "Point") -> Real:
        return self.x * other.x + self.y * other.y

    def det(self, other: "Point") -> Real:
        return self.x * other.y - self.y * other.x

    def projection(self, to: "Point") -> "Point":
        return to * (self.dot(to) / to.norm2())

    def __lt__(self, other: "Point") -> bool:
        q = self.quadrant()
        oq = other.quadrant()
        if q != oq:
            return q < oq
        return sign(self.det(other)) > 0

    def __repr__(self) -> str:
        return f"{self.x} {self.y}"


@enum.unique
class Turn(enum.IntEnum):
    """Turn direction"""

    BACK = -2
    CW = -1
    MIDDLE = 0
    CCW = 1
    FRONT = 2


def iSP(a: Point, b: Point, c: Point) -> Turn:
    """iSP

    Determine the positional relationship of the three Points.

    Returns
    -------
        Turn direction
    """
    flg = sign((b - a).det(c - a))
    if flg == 1:
        return Turn.CCW
    elif flg == -1:
        return Turn.CW
    else:
        if sign((b - a).dot(c - b)) > 0:
            return Turn.FRONT
        elif sign((a - b).dot(c - a)) > 0:
            return Turn.BACK
        else:
            return Turn.MIDDLE


@enum.unique
class Angle(enum.IntEnum):
    """Angle type"""

    NOT_ANGLE = -2
    OBTUSE = -1
    RIGHT = 0
    ACUTE = 1


def angle_type(a: Point, b: Point, c: Point) -> Angle:
    if abs(iSP(a, b, c)) == 1:
        return Angle.NOT_ANGLE
    else:
        return Angle(sign((a - b).dot(c - b)))

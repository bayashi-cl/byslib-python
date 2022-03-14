import math
import numbers
from dataclasses import dataclass
from typing import Generic, TypeVar, Union

Real = Union[int, float]
EPS = 1e-9


def sign(x: float) -> int:
    if x < -EPS:
        return -1
    elif x > EPS:
        return 1
    else:
        return 0


@dataclass
class Point:
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
        return self.x ** 2 + self.y ** 2

    def norm(self) -> float:
        return math.sqrt(self.norm2())

    def normalized(self) -> "Point":
        n = self.norm()
        return Point(self.x / n, self.y / n)

    def angle(self) -> float:
        return math.atan2(self.y, self.x)

    def quadrant(self) -> int:
        if sign(self.y) >= 0:
            return 1 if sign(self.x) >= 0 else 2
        return 4 if sign(self.x) >= 0 else 3

    def normal(self) -> "Point":
        return Point(-self.normalized().y, self.normalized().x)

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


if __name__ == "__main__":
    p = Point(3, 4)
    print(p.norm())

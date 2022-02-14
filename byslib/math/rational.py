import numbers


class Rational(numbers.Rational):
    _numerator: int
    _denominator: int

    def __init__(self, numerator: int, denomerator: int) -> None:
        sgn = 1
        if denomerator < 0:
            sgn *= -1
            denomerator *= -1
        self._numerator = sgn * numerator
        self._denominator = denomerator

    def __add__(self, other):
        """self + other"""
        raise NotImplementedError

    def __radd__(self, other):
        """other + self"""
        raise NotImplementedError

    def __neg__(self):
        """-self"""
        raise NotImplementedError

    def __pos__(self):
        """+self"""
        raise NotImplementedError

    def __mul__(self, other):
        """self * other"""
        raise NotImplementedError

    def __rmul__(self, other):
        """other * self"""
        raise NotImplementedError

    def __truediv__(self, other):
        """self / other: Should promote to float when necessary."""
        raise NotImplementedError

    def __rtruediv__(self, other):
        """other / self"""
        raise NotImplementedError

    def __pow__(self, exponent):
        """self**exponent; should promote to float or complex when necessary."""
        raise NotImplementedError

    def __rpow__(self, base):
        """base ** self"""
        raise NotImplementedError

    def __abs__(self):
        """Returns the Real distance from 0. Called for abs(self)."""
        raise NotImplementedError

    def __eq__(self, other):
        """self == other"""
        raise NotImplementedError

    def __trunc__(self) -> int:
        if self._numerator < 0:
            return -(-self._numerator // self._denominator)
        else:
            return self._numerator // self._denominator

    def __floor__(self) -> int:
        return self._numerator // self._denominator

    def __ceil__(self) -> int:
        return -(-self.numerator // self.denominator)

    def __round__(self, ndigits=None):
        if ndigits is None:
            floor, remainder = divmod(self._numerator, self._denominator)
            if remainder * 2 < self._denominator:
                return floor
            elif remainder * 2 > self._denominator:
                return floor + 1
            elif floor % 2 == 0:
                return floor
            else:
                return floor + 1
        else:
            raise NotImplementedError

    def __floordiv__(self, other):
        """self // other: The floor() of self/other."""
        raise NotImplementedError

    def __rfloordiv__(self, other):
        """other // self: The floor() of other/self."""
        raise NotImplementedError

    def __mod__(self, other):
        """self % other"""
        raise NotImplementedError

    def __rmod__(self, other):
        """other % self"""
        raise NotImplementedError

    def __lt__(self, other):
        """self < other

        < on Reals defines a total ordering, except perhaps for NaN."""
        raise NotImplementedError

    def __le__(self, other):
        """self <= other"""
        raise NotImplementedError

    @property
    def numerator(self) -> int:
        return self._numerator

    @property
    def denominator(self) -> int:
        return self._denominator

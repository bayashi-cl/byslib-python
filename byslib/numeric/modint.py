# @title Modint
from typing import Union


class modint:
    """Modint
    Not so fast.
    """

    __slots__ = ("v",)
    mod: int = 0

    def __init__(self, v: int = 0) -> None:
        self.v = v % self.mod

    def __repr__(self):
        return str(self.v)

    def __index__(self):
        return self.v

    def __iadd__(self, other: Union["modint", int]) -> "modint":
        if isinstance(other, int):
            self.v += other
        else:
            self.v += other.v

        self.v %= self.mod
        return self

    def __isub__(self, other: Union["modint", int]) -> "modint":
        if isinstance(other, int):
            self.v -= other
        else:
            self.v -= other.v

        self.v %= self.mod
        return self

    def __imul__(self, other: Union["modint", int]) -> "modint":
        if isinstance(other, int):
            self.v *= other
        else:
            self.v *= other.v

        self.v %= self.mod
        return self

    def __ipow__(self, other: int) -> "modint":
        self.v = pow(self.v, other, self.mod)
        return self

    def __ifloordiv__(self, other: Union["modint", int]) -> "modint":
        if isinstance(other, int):
            self.v *= pow(other, self.mod - 2, self.mod)
        else:
            self.v *= pow(other.v, self.mod - 2, self.mod)

        self.v %= self.mod
        return self

    def __add__(self, other: Union["modint", int]) -> "modint":
        res = self.__class__(self.v)
        res += other
        return res

    def __sub__(self, other: Union["modint", int]) -> "modint":
        res = self.__class__(self.v)
        res -= other
        return res

    def __mul__(self, other: Union["modint", int]) -> "modint":
        res = self.__class__(self.v)
        res *= other
        return res

    def __floordiv__(self, other: Union["modint", int]) -> "modint":
        res = self.__class__(self.v)
        res //= other
        return res

    def __pow__(self, other: int) -> "modint":
        res = self.__class__(self.v)
        res **= other
        return res

    def inv(self) -> "modint":
        return self.__class__(pow(self.v, self.mod - 2, self.mod))

    def __radd__(self, other: int) -> "modint":
        res = self.__class__(other)
        res += self
        return res

    def __rsub__(self, other: int) -> "modint":
        res = self.__class__(other)
        res -= self
        return res

    def __rmul__(self, other: int) -> "modint":
        res = self.__class__(other)
        res *= self
        return res

    def __rfloordiv__(self, other: int) -> "modint":
        res = self.__class__(other)
        res //= self
        return res


def using_modint(modulo: int):
    """using modint

    set modulo to modint class

    Parameters
    ----------
    modulo

    Returns
    -------
        modint class mod = modulo
    """

    class Mint(modint):
        __slots__ = ()
        mod: int = modulo

    return Mint


modint998244353 = using_modint(998244353)
modint1000000007 = using_modint(1000000007)

from array import array


def using_modarray(modulo: int):
    class ModArray(array):
        __slots__ = ()
        mod: int = modulo

        @classmethod
        def zeros(cls, n: int) -> "ModArray":
            return cls("L", [0] * n)

        def __setitem__(self, index, value) -> None:
            super().__setitem__(index, value % self.mod)

        def inv(self, index: int) -> int:
            return pow(self[index], self.mod - 2, self.mod)

    return ModArray


modarray998244353 = using_modarray(998244353)
modarray1000000007 = using_modarray(1000000007)

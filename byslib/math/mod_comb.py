class MultiComb:
    """二項係数
    **__init__: O(n)**
    **comb: O(1)**
    """

    def __init__(self, n: int, mod: int = 10 ** 9 + 7) -> None:
        self.n = n
        self.mod = mod
        self.fact = [1, 1]
        self.factinv = [1, 1]
        self.inv = [0, 1]
        for i in range(2, self.n + 1):
            self.fact.append((self.fact[-1] * i) % self.mod)
            self.inv.append((-self.inv[self.mod % i] * (self.mod // i)) % self.mod)
            self.factinv.append((self.factinv[-1] * self.inv[-1]) % self.mod)

    def comb(self, n: int, r: int) -> int:
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] * self.factinv[n - r] % self.mod


def mono_comb(n: int, r: int, mod: int = 10 ** 9 + 7) -> int:
    """二項係数
    **O(r)**
    python3.8 or later
    """
    r = min(r, n - r)
    numer = 1
    denom = 1
    for i in range(r):
        numer *= n - i
        denom *= r - i

        numer %= mod
        denom %= mod

    denom_mod = pow(denom, -1, mod)
    return (numer * denom_mod) % mod

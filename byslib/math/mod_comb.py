MOD = 10 ** 9 + 7


def comb(n, r, mod=10 ** 9 + 7):
    def cmb(n, r, p):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return fact[n] * factinv[r] * factinv[n - r] % p

    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)

    return cmb(n, r, mod)


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


def mono_comb2(n, r, p=10 ** 9 + 7):
    bunshi = 1
    for i in range(n - r + 1, n + 1):
        bunshi = bunshi * i % p
    bunbo = 1
    for i in range(1, r + 1):
        bunbo = bunbo * i % p
    return bunshi * pow(bunbo, p - 2, p)


if __name__ == "__main__":
    pass

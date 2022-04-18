# @title Binomial coefficient
class MultiComb:
    """Binomial coefficient

    Notes
    -----
    Time complexity

    * construct: O(n)
    * query: O(1)

    References
    ----------
    ..[1] https://drken1215.hatenablog.com/entry/2018/06/08/210000

    Examples
    --------
    >>> mc = MultiComb(10)
    >>> print(mc.comb(5, 3))
    10
    """

    def __init__(self, n: int, mod: int = 10**9 + 7) -> None:
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
        """nCr"""
        if r < 0 or n < r:
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] * self.factinv[n - r] % self.mod

    def perm(self, n: int, r: int) -> int:
        """nPr"""
        if r < 0 or n < r:
            return 0
        return self.fact[n] * self.factinv[n - r] % self.mod

    def hom(self, n: int, r: int) -> int:
        """nHr"""
        if n == r == 0:
            return 1
        return self.comb(n + r - 1, r)


def mono_comb(n: int, r: int, mod: int = 10**9 + 7) -> int:
    """Binomial coefficient

    python 3.8 or later

    Parameters
    ----------
    n
        n
    r
        r
    mod, optional
        mod, by default 10**9+7

    Returns
    -------
        nCr

    Notes
    -----
    Time complexity

    O(min(r, n - r))

    Examples
    --------
    Examples
    --------
    >>> print(mono_comb(5, 3))
    10
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

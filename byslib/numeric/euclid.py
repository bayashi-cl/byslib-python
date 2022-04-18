# @title Euclid
from typing import Tuple


def ext_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended Euclidean algorithm

    solve ax + by = gcd(a, b)

    Parameters
    ----------
    a
    b

    Returns
    -------
        (d, y, x) s.t. ax + by = gcd(a, b)
    """
    if b:
        d, y, x = ext_gcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0


def crt(a: int, b: int, mod1: int, mod2: int) -> int:
    g, k, _ = ext_gcd(mod1, mod2)
    if (b - a) % g != 0:
        return -1
    k *= (b - a) // g
    ans = mod1 * k + a
    lcm = mod1 * mod2 // g
    return ans % lcm

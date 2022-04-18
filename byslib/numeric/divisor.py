# @title Divisor
import typing


def make_divisors(n):
    """_summary_

    Parameters
    ----------
    n
        max n < 10**12

    Returns
    -------
        List of divisors(sorted)

    Notes
    -----
    Time complexity

    O(√n)

    References
    ----------
    ..[1] https://qiita.com/drken/items/a14e9af0ca2d857dad23#3-1-%E7%B4%84%E6%95%B0%E5%88%97%E6%8C%99

    Examples
    --------
    >>> make_divisors(12)
    [1, 2, 3, 4, 6, 12]
    """
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def prime_factorize(n: int) -> typing.List[int]:
    """Prime factorization

    trial division

    Parameters
    ----------
    n
        max n < 10**12

    Returns
    -------
        list of factor

    Notes
    -----
    Time complexity

    O(√n)

    References
    ----------
    ..[1] https://en.wikipedia.org/wiki/Trial_division

    Examples
    --------
    >>> prime_factorize(24)
    [2, 2, 2, 3]
    """
    res = []
    while n % 2 == 0:
        res.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            res.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        res.append(n)
    return res

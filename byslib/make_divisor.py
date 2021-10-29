import typing


def make_divisors(n):
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


if __name__ == "__main__":
    print(len(make_divisors(2 ** 4 * 3 ** 4 * 5 ** 2)))

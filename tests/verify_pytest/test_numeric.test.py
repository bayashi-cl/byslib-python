# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
import pytest
from byslib.numeric import divisor, euclid


class TestDivisor:
    @pytest.mark.parametrize(
        ("x", "divs"),
        [
            (1, [1]),
            (2, [1, 2]),
            (12, [1, 2, 3, 4, 6, 12]),
            (17, [1, 17]),
            (57, [1, 3, 19, 57]),
            (998244353, [1, 998244353]),
            (100003**2, [1, 100003, 100003**2]),
        ],
    )
    def test_make_divisor(self, x, divs):
        assert divisor.make_divisors(x) == divs

    @pytest.mark.parametrize(
        ("x", "facts"),
        [
            (1, []),
            (2, [2]),
            (17, [17]),
            (24, [2, 2, 2, 3]),
            (998244353, [998244353]),
        ],
    )
    def test_prime_factorize(self, x, facts):
        assert divisor.prime_factorize(x) == facts


class TestEuclid:
    @pytest.mark.parametrize(
        ("a", "b"),
        [
            (3, 4),
            (5, 8),
            (-5, 4),
            (-1, -8),
            (998244353, 1000000007),
        ],
    )
    def test_ext_gcd(self, a, b):
        d, x, y = euclid.ext_gcd(a, b)
        assert a * x + b * y == d


if __name__ == "__main__":
    import sys

    from exec_pytest import exec_pytest

    sys.exit(exec_pytest(__file__))

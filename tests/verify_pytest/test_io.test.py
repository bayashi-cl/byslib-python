# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
from byslib.core.fastio import int1


def test_sinput_int1():
    assert int1("5") == 4


if __name__ == "__main__":
    import sys

    from exec_pytest import exec_pytest

    sys.exit(exec_pytest(__file__))

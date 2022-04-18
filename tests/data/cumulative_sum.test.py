# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum
import sys

from byslib.core.fastio import readline
from byslib.data.cumulative_sum import CumulativeSum


def main() -> None:
    n, q = map(int, readline().split())
    a = list(map(int, readline().split()))
    cs = CumulativeSum(a)
    for _ in range(q):
        l, r = map(int, readline().split())
        print(cs.fold(l, r))


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()

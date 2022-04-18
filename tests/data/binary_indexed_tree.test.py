# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum
import sys

from byslib.core.fastio import readline
from byslib.data.binary_indexed_tree import BinaryIndexedTree


def main() -> None:
    _, q = map(int, readline().split())
    a = list(map(int, readline().split()))
    bit = BinaryIndexedTree(a)
    for _ in range(q):
        t, *que = map(int, readline().split())
        if t == 0:
            p, x = que
            bit.point_append(p, x)
        else:
            l, r = que
            print(bit.fold(l, r))


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()

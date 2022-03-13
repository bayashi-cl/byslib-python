# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum
import sys
from operator import add

from byslib.core.const import IINF, MOD
from byslib.core.fastio import debug, readline, sinput
from byslib.data.segment_tree import SegmentTree


def main() -> None:
    _, q = map(int, readline().split())
    a = list(map(int, readline().split()))
    seg = SegmentTree(add, 0, a)
    for _ in range(q):
        c, s, t = map(int, sinput().split())
        if c == 0:
            ap = seg[s]
            seg.update(s, ap + t)
        else:
            print(seg.query(s, t))


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()

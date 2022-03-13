# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_F
import sys

from byslib.core.const import IINF, MOD
from byslib.core.fastio import debug, readline, sinput

from byslib.data.lazy_segment_tree import LazySegmentTree


def main() -> None:
    id_S: int = 2**31 - 1
    id_F = -1

    def op(a: int, b: int) -> int:
        return min(a, b)

    def mp(a: int, b: int) -> int:
        return b if a == -1 else a

    def cp(f: int, g: int) -> int:
        return g if f == -1 else f

    n, q = map(int, readline().split())
    a = [id_S] * n
    seg = LazySegmentTree(op, id_S, mp, cp, id_F, a)
    for _ in range(q):
        head, *body = map(int, readline().split())
        if head == 0:
            s, t, x = body
            seg.apply(s, t + 1, x)
        else:
            s, t = body
            print(seg.query(s, t + 1))


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()

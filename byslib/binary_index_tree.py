"""https://judge.yosupo.jp/problem/point_add_range_sum"""

# region template
import sys
import typing

sys.setrecursionlimit(10 ** 6)
Vec = typing.List[int]
VecVec = typing.List[Vec]
sinput: typing.Callable[..., str] = sys.stdin.readline
MOD: int = 1000000007
INF: float = float("Inf")
IINF: int = sys.maxsize
# endregion


class BinaryIndexedTree:
    """フェニック木
    **0-index**
    """

    def __init__(self, size: int) -> None:
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, i: int, x: int) -> None:
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def cumsum(self, r: int) -> int:
        """累積和
        [0, r)の和を求める。
        """
        s = 0
        while r:
            s += self.tree[r]
            r -= r & -r
        return s

    def range_sum(self, l: int, r: int) -> int:
        """部分和
        [l, r)の和を求める。
        """
        return self.cumsum(r) - self.cumsum(l)

    @classmethod
    def construct(cls, array: typing.List[int]) -> "BinaryIndexedTree":
        res = cls(len(array))
        for ele in enumerate(array):
            res.add(*ele)

        return res


def main() -> None:
    n, q = map(int, sinput().split())
    a = list(map(int, sinput().split()))

    fen = BinaryIndexedTree.construct(a)
    for _ in range(q):
        t, x, y = map(int, sinput().split())
        if t == 0:
            fen.add(x, y)
        else:
            print(fen.range_sum(x, y))


if __name__ == "__main__":
    main()

# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_2_A
import sys

from byslib.core.const import IINF, MOD
from byslib.core.fastio import debug, readline, sinput
from byslib.graph.edge import Edge
from byslib.graph.kruskal import kruskal


def main() -> None:
    v, e = map(int, sinput().split())
    edges = [Edge(*map(int, sinput().split())) for _ in range(e)]
    cost, _ = kruskal(edges, v)
    print(cost)


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()

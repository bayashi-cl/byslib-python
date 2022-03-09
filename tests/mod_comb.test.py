# verification-helper: PROBLEM https://yukicoder.me/problems/no/117
import sys

from byslib.core.const import IINF, MOD
from byslib.core.io import debug, readline, sinput
from byslib.math.mod_comb import MultiComb


def main() -> None:
    t = int(readline())
    mc = MultiComb(2_000_000)

    for _ in range(t):
        s = sinput()
        com = s[0]
        n, k = map(int, s[2:-1].split(","))
        if com == "C":
            print(mc.comb(n, k))
        elif com == "P":
            print(mc.perm(n, k))
        elif com == "H":
            print(mc.hom(n, k))
        else:
            raise ValueError


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()

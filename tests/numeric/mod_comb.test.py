# verification-helper: PROBLEM https://yukicoder.me/problems/no/117
from byslib.core.config import procon_setup
from byslib.core.fastio import readline, sinput
from byslib.numeric.mod_comb import MultiComb


@procon_setup
def main(**kwargs) -> None:
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
    t = 1
    # t = int(readline())
    main(t)

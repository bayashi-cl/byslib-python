# verification-helper: PROBLEM https://judge.yosupo.jp/problem/many_aplusb
from byslib.core.fastio import readline


def main() -> None:
    t = int(readline())
    for _ in range(t):
        a, b = map(int, readline().split())
        print(a + b)


if __name__ == "__main__":
    main()

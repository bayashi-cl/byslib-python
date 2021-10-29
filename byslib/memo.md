# 競プロ用メモ
@bayashi_cl

## テンプレ
```python
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


def main() -> None:
    ...


if __name__ == "__main__":
    main()

```


## 強連結成分分解

[競プロ典型90問 021 - Come Back in One Piece（★5）](https://atcoder.jp/contests/typical90/tasks/typical90_u)

```python
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

n, m = map(int, sinput().split())
edge = np.array([sinput().split() for _ in range(m)], dtype=np.int64).T
cost = np.ones(m).T
graph = csr_matrix((cost, edge - 1), (n, n))
_, scc = connected_components(graph, directed=True, connection="strong")
_, count = np.unique(scc, return_counts=True)
ans = np.sum(count * (count - 1) // 2)
print(ans)

```

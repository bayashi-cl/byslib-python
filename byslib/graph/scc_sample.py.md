---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://atcoder.jp/contests/typical90/tasks/typical90_u
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: 'pass

    # """

    # https://atcoder.jp/contests/typical90/tasks/typical90_u

    # """


    # # region template

    # from __future__ import annotations


    # import sys

    # from typing import Callable, Final


    # import numpy as np

    # from scipy.sparse import csr_matrix

    # from scipy.sparse.csgraph import connected_components


    # sys.setrecursionlimit(10 ** 9)

    # sinput: Callable[..., str] = sys.stdin.readline

    # INF: Final[float] = float("inf")

    # MOD: Final[int] = 10 ** 9 + 7

    # # endregion



    # def main() -> None:

    #     n, m = map(int, sinput().split())

    #     edge = np.array([sinput().split() for _ in range(m)], dtype=np.int64).T

    #     cost = np.ones(m).T

    #     graph = csr_matrix((cost, edge - 1), (n, n))

    #     _, scc = connected_components(graph, directed=True, connection="strong")

    #     _, count = np.unique(scc, return_counts=True)

    #     ans = np.sum(count * (count - 1) // 2)

    #     print(ans)



    # if __name__ == "__main__":

    #     main()

    '
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/scc_sample.py
  requiredBy: []
  timestamp: '2022-02-18 18:18:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/graph/scc_sample.py
layout: document
redirect_from:
- /library/byslib/graph/scc_sample.py
- /library/byslib/graph/scc_sample.py.html
title: byslib/graph/scc_sample.py
---

---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# region template\nimport sys\nimport typing\nfrom typing import Callable,\
    \ Dict, List, Set, Tuple\n\nsys.setrecursionlimit(10 ** 6)\nVec = List[int]\n\
    VecVec = List[Vec]\nsinput: Callable[..., str] = sys.stdin.readline\nMOD: int\
    \ = 1000000007\nINF: float = float(\"Inf\")\nIINF: int = sys.maxsize\n# endregion\n\
    \n\ndef make_adj(board: List[str]) -> VecVec:\n    h = len(board)\n    w = len(board[0])\n\
    \    adj: VecVec = [[] for _ in range(h * w)]\n\n    delta = ((1, 0), (-1, 0),\
    \ (0, 1), (0, -1))\n    for i in range(h):\n        for j in range(w):\n     \
    \       if board[i][j] == \"#\":\n                continue\n            now =\
    \ i * w + j\n            for di, dj in delta:\n                if i + di < 0 or\
    \ h <= i + di:\n                    continue\n                if j + dj < 0 or\
    \ w <= j + dj:\n                    continue\n                adj[now].append((i\
    \ + di) * w + j + dj)\n\n    return adj\n\n\ndef main() -> None:\n    ...\n\n\n\
    if __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/utility/util.py
  requiredBy: []
  timestamp: '2022-02-14 17:11:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/utility/util.py
layout: document
redirect_from:
- /library/byslib/utility/util.py
- /library/byslib/utility/util.py.html
title: byslib/utility/util.py
---

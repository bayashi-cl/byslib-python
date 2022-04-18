---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    document_title: Warshall Floyd
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Warshall Floyd\nfrom typing import List\n\nfrom ..core.const import\
    \ IINF\nfrom .edge import Edge\n\n\ndef warshall_floyd(elist: List[Edge], n: int)\
    \ -> List[List[int]]:\n    \"\"\"warshall floyd\n\n    Parameters\n    ----------\n\
    \    elist\n        List of Edge\n    n\n        Vertex Size\n\n    Returns\n\
    \    -------\n    Cost matrix\n\n    Notes\n    -----\n    Time complexity\n\n\
    \    O(N^3)\n\n    References\n    ----------\n    ..[1] \U0001F41C p.98\n   \
    \ \"\"\"\n    cost = [[IINF] * n for _ in range(n)]\n    for e in elist:\n   \
    \     cost[e.src][e.dest] = e.weight\n    for i in range(n):\n        cost[i][i]\
    \ == 0\n\n    for k in range(n):\n        for i in range(n):\n            for\
    \ j in range(n):\n                if cost[i][k] == IINF or cost[k][j] == IINF:\n\
    \                    continue\n                tmp_cost = cost[i][k] + cost[k][j]\n\
    \                if cost[i][j] > tmp_cost:\n                    cost[i][j] = tmp_cost\n\
    \n    return cost\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/graph/warshall_floyd.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/graph/warshall_floyd.py
layout: document
redirect_from:
- /library/byslib/graph/warshall_floyd.py
- /library/byslib/graph/warshall_floyd.py.html
title: Warshall Floyd
---

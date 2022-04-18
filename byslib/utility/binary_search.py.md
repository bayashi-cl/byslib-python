---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    document_title: Binary search
    links:
    - https://twitter.com/meguru_comp/status/697008509376835584
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Binary search\r\nfrom typing import Callable\r\n\r\n\r\ndef meguru_bisect(ok:\
    \ int, ng: int, is_ok: Callable[..., bool], *args) -> int:\r\n    \"\"\"Binary\
    \ Search\r\n\r\n    Parameters\r\n    ----------\r\n    ok\r\n        Inital value\
    \ s.t. is_ok(ok) == True\r\n    ng\r\n        Inital value s.t. is_ok(ng) == False\r\
    \n    is_ok\r\n        Judge function\r\n\r\n    Returns\r\n    -------\r\n  \
    \      number of is_ok(x) == True and is_ok(x \xB1 1) == False\r\n\r\n    Notes\r\
    \n    -----\r\n    Time complexity\r\n\r\n    O(log(abs(ok-ng)))\r\n\r\n    References\r\
    \n    ----------\r\n    ..[1] https://twitter.com/meguru_comp/status/697008509376835584\r\
    \n\r\n    Examples\r\n    --------\r\n    \"\"\"\r\n    assert is_ok(ok, *args)\r\
    \n    assert not is_ok(ng, *args)\r\n\r\n    while abs(ok - ng) > 1:\r\n     \
    \   mid = (ok + ng) >> 1\r\n        if is_ok(mid, *args):\r\n            ok =\
    \ mid\r\n        else:\r\n            ng = mid\r\n    return ok\r\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/utility/binary_search.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/utility/binary_search.py
layout: document
redirect_from:
- /library/byslib/utility/binary_search.py
- /library/byslib/utility/binary_search.py.html
title: Binary search
---

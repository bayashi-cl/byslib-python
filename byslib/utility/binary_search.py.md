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
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 74, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable\r\n\r\n\r\ndef meguru_bisect(ok: int, ng: int,\
    \ is_ok: Callable[..., bool], *args) -> int:\r\n    \"\"\"\u4E8C\u5206\u63A2\u7D22\
    \u6CD5\r\n    Args:\r\n        ok (int): is_ok\u3092\u6E80\u305F\u3059\u521D\u671F\
    \u5024\r\n        ng (int): is_ok\u3092\u6E80\u305F\u3055\u306A\u3044\u521D\u671F\
    \u5024\r\n        is_ok (typing.Callable[..., bool]): \u5224\u5B9A\u7528\u95A2\
    \u6570\r\n        *args (object): is_ok\u306B\u6E21\u3055\u308C\u308B\u5F15\u6570\
    \r\n\r\n    Returns:\r\n        int: is_ok\u3092\u6E80\u305F\u3059\u6700\u5927\
    /\u5C0F\u306E\u6574\u6570\r\n    \"\"\"\r\n    assert is_ok(ok, *args)\r\n   \
    \ assert not is_ok(ng, *args)\r\n\r\n    while abs(ok - ng) > 1:\r\n        mid\
    \ = (ok + ng) >> 1\r\n        if is_ok(mid, *args):\r\n            ok = mid\r\n\
    \        else:\r\n            ng = mid\r\n    return ok\r\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/utility/binary_search.py
  requiredBy: []
  timestamp: '2022-02-18 18:18:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/utility/binary_search.py
layout: document
redirect_from:
- /library/byslib/utility/binary_search.py
- /library/byslib/utility/binary_search.py.html
title: byslib/utility/binary_search.py
---

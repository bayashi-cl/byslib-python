---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    document_title: Divisor
    links:
    - https://en.wikipedia.org/wiki/Trial_division
    - https://qiita.com/drken/items/a14e9af0ca2d857dad23#3-1-%E7%B4%84%E6%95%B0%E5%88%97%E6%8C%99
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# @title Divisor\nimport typing\n\n\ndef make_divisors(n):\n    \"\"\"_summary_\n\
    \n    Parameters\n    ----------\n    n\n        max n < 10**12\n\n    Returns\n\
    \    -------\n        List of divisors(sorted)\n\n    Notes\n    -----\n    Time\
    \ complexity\n\n    O(\u221An)\n\n    References\n    ----------\n    ..[1] https://qiita.com/drken/items/a14e9af0ca2d857dad23#3-1-%E7%B4%84%E6%95%B0%E5%88%97%E6%8C%99\n\
    \n    Examples\n    --------\n    >>> make_divisors(12)\n    [1, 2, 3, 4, 6, 12]\n\
    \    \"\"\"\n    lower_divisors, upper_divisors = [], []\n    i = 1\n    while\
    \ i * i <= n:\n        if n % i == 0:\n            lower_divisors.append(i)\n\
    \            if i != n // i:\n                upper_divisors.append(n // i)\n\
    \        i += 1\n    return lower_divisors + upper_divisors[::-1]\n\n\ndef prime_factorize(n:\
    \ int) -> typing.List[int]:\n    \"\"\"Prime factorization\n\n    trial division\n\
    \n    Parameters\n    ----------\n    n\n        max n < 10**12\n\n    Returns\n\
    \    -------\n        list of factor\n\n    Notes\n    -----\n    Time complexity\n\
    \n    O(\u221An)\n\n    References\n    ----------\n    ..[1] https://en.wikipedia.org/wiki/Trial_division\n\
    \n    Examples\n    --------\n    >>> prime_factorize(24)\n    [2, 2, 2, 3]\n\
    \    \"\"\"\n    res = []\n    while n % 2 == 0:\n        res.append(2)\n    \
    \    n //= 2\n    f = 3\n    while f * f <= n:\n        if n % f == 0:\n     \
    \       res.append(f)\n            n //= f\n        else:\n            f += 2\n\
    \    if n != 1:\n        res.append(n)\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/numeric/divisor.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/numeric/divisor.py
layout: document
redirect_from:
- /library/byslib/numeric/divisor.py
- /library/byslib/numeric/divisor.py.html
title: Divisor
---

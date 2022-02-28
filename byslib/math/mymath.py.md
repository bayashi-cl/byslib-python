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
  code: "# ax+by = gcd(a,b)\n# def ext_gcd(a, b):\n#     if b == 0:\n#         return\
    \ (1, 0)\n#     q, r = divmod(a, b)\n#     s, t = ext_gcd(b, r)\n#     return\
    \ (t, -q * t + s)\n\n\ndef ext_gcd(a, b):\n    if b:\n        d, y, x = ext_gcd(b,\
    \ a % b)\n        y -= (a // b) * x\n        return d, x, y\n    return a, 1,\
    \ 0\n\n\ndef crt(a, b, mod1, mod2):\n    g, k, _ = ext_gcd(mod1, mod2)\n    if\
    \ (b - a) % g != 0:\n        return -1\n    k *= (b - a) // g\n    ans = mod1\
    \ * k + a\n    lcm = mod1 * mod2 // g\n    return ans % lcm\n\n\nif __name__ ==\
    \ \"__main__\":\n    print(crt(3, 5, 2, 3))\n"
  dependsOn: []
  isVerificationFile: false
  path: byslib/math/mymath.py
  requiredBy: []
  timestamp: '2022-02-14 17:11:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: byslib/math/mymath.py
layout: document
redirect_from:
- /library/byslib/math/mymath.py
- /library/byslib/math/mymath.py.html
title: byslib/math/mymath.py
---

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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir], 'release': True}).decode()\n\
    \  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 80, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import subprocess\nimport sys\n\n\ndef exec_pytest(file: str) -> int:\n \
    \   args = [\"pytest\", file, \"--import-mode=importlib\"]\n    try:\n       \
    \ subprocess.run(args, text=True, check=True, stdout=sys.stderr)\n    except subprocess.CalledProcessError\
    \ as e:\n        print(e, file=sys.stderr)\n        return 1\n    else:\n    \
    \    print(\"Hello World\")\n        return 0\n"
  dependsOn: []
  isVerificationFile: false
  path: tests/verify_pytest/exec_pytest.py
  requiredBy: []
  timestamp: '2022-04-18 22:29:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/verify_pytest/exec_pytest.py
layout: document
redirect_from:
- /library/tests/verify_pytest/exec_pytest.py
- /library/tests/verify_pytest/exec_pytest.py.html
title: tests/verify_pytest/exec_pytest.py
---

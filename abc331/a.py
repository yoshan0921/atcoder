import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
12 30
2012 6 20
"""
sys.stdin = io.StringIO(_INPUT)

M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d + 1 > D:
    d = 1
    if m + 1 > M:
        m = 1
        y += 1
    else:
        m += 1
else:
    d += 1

print(y, m, d)

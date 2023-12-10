import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
5 300 500
"""
sys.stdin = io.StringIO(_INPUT)

K, G, M = map(int, input().split())

glass = 0
mug = 0

for i in range(K):
    if glass == G:
        glass = 0
    elif mug == 0:
        mug = M
    else:
        if G - glass >= mug:
            glass = mug
            mug = 0
        else:
            mug = mug - (G - glass)
            glass = G

print(glass, mug)

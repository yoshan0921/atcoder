import io
import sys
import bisect
import collections
import itertools
import math
sys.setrecursionlimit(10**9)

_INPUT = """\
2 2
1000000000 1000000000
200000000000000
1
"""
sys.stdin = io.StringIO(_INPUT)

N, Q = map(int, input().split())
R = list(map(int, input().split()))

R.sort()
R_accumulate = list(itertools.accumulate(R))

for i in range(Q):
    X = int(input())
    idx = bisect.bisect_right(R_accumulate, X)
    print(idx)

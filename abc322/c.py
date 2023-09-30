import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
8 1
8
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(1, N+1):
    date = bisect.bisect_left(A, i)
    # print("date", date)
    print(A[date]-i)

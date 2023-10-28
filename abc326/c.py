import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
8 6
2 2 2 2 2 7 17 19
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

max_num = 0
for i in range(len(A)):
    ret = bisect.bisect_left(A, A[i]+M)
    max_num = max(max_num, ret-i)

print(max_num)

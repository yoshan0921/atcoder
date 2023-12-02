import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
50
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

A_sorted = sorted(A)
total = []

# 累積和を計算する。
for i in range(N):
    if i == 0:
        total.append(A_sorted[i])
    else:
        total.append(total[i-1] + A_sorted[i])

for a in A:
    ret = bisect.bisect_right(A_sorted, a)
    if ret == N:
        print(0, end=" ")
    else:
        print(total[N-1] - total[ret-1], end=" ")

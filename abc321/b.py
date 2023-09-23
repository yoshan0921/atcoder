import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
4 100
10 30 40
"""
sys.stdin = io.StringIO(_INPUT)

N, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# print(A)

# 小さい方からN-2個を選んで、Xを超える場合は0を出力して終了
min = sum(A[0:N-2])
mid = sum(A[1:N-2])
max = sum(A[1:])
# print(min, mid, max)
if min >= X:
    print(0)
    exit(0)

if max < X:
    print(-1)
    exit(0)

target_score = X - mid
if target_score > 100:
    print(-1)
    exit(0)
else:
    print(target_score)

import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
6
31 3
20 8
11 5
4 3
47 14
1 18
"""
sys.stdin = io.StringIO(_INPUT)
W = []
X = []

N = int(input())
for _ in range(N):
    w, x = map(int, input().split())
    W.append(w)
    X.append(x)
# print(W, X)

max_count = 0
for i in range(24):
    count = 0
    for j in range(N):
        if 9 <= i + X[j] < 18:
            count += W[j]
        elif 33 <= i + X[j] < 42:
            count += W[j]
    max_count = max(max_count, count)

print(max_count)

import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
5
2 5
2 5
-3 4
-4 -8
6 -2
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()
x_mid = X[N//2]
y_mid = Y[N//2]

ans = 0
for i in range(N):
    ans += abs(X[i] - x_mid)
    ans += abs(Y[i] - y_mid)
print(ans)

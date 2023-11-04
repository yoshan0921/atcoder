import numpy as np
import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)


_INPUT = """\
7 8
1 6 2 7 5 4 2 2
3 2 7 2 1 2 3 3
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
X = [-1] * N
ans = "Yes"

G = [[] for _ in range(N)]
for i in range(M):
    G[A[i]-1].append(B[i]-1)
    G[B[i]-1].append(A[i]-1)
# print(G)


def dfs(v, x):
    X[v] = x
    for v2 in G[v]:
        if X[v2] == -1:
            dfs(v2, 1-x)
        elif X[v2] == X[v]:
            global ans
            ans = "No"


for i in range(N):
    # print(X)
    if X[i] == -1:
        dfs(i, 0)

print(ans)

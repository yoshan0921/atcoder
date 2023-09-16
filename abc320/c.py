import math
import io
import sys
import bisect
import collections
import itertools

_INPUT = """\
10
1937458062
8124690357
2385760149
"""
sys.stdin = io.StringIO(_INPUT)

M = int(input())
S = []
for _ in range(3):
    S.append(input())

INF = 10**9
ans = INF
for i in range(M * 3):
    for j in range(M * 3):
        for k in range(M * 3):
            if i != j and i != k and j != k and S[0][i % M] == S[1][j % M] == S[2][k % M]:
                ans = min(ans, max(i, j, k))

print(ans if ans < INF else -1)

"""
Dynamic Programming Template
"""

import io
import sys
import math

_INPUT = """\
4 15
5 5 5 12
8 9 10 24
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
# ボールの重さ
W = list(map(int, input().split()))
# ボールの価値
V = list(map(int, input().split()))

dp = [[-1] * (M + 1) for _ in range(N + 1)]

dp[0][0] = 0

for i in range(N):
    for j in range(M + 1):
        if dp[i][j] == -1:
            continue

        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

        if j + W[i] <= M:
            dp[i + 1][j + W[i]] = max(dp[i + 1][j + W[i]], dp[i][j] + V[i])

print(max(dp[N]))

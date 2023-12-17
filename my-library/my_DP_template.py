"""
Dynamic Programming Template
"""

import io
import sys

# Q1: Suppose there are N items, each with weight W and value V. Find the maximum value of the sum of their values, provided that the sum of their weights does not exceed M.
_INPUT = """\
5 10
1 4 2 1 5
7 4 5 9 1
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
W = list(map(int, input().split()))
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

    print(f"i={i}")
    for vals in dp:
        print(*vals, sep="\t")

print(dp[N])
print(max(dp[N]))

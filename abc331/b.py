import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
99 600 800 1200
"""
sys.stdin = io.StringIO(_INPUT)

N, S, M, L = map(int, input().split())

# dpテーブルの初期化
dp = [float('inf')] * (N + 50)
dp[0] = 0

for i in range(N + 1):
    if dp[i] == float('inf'):
        continue
    dp[i+6] = min(dp[i+6], dp[i] + S)
    dp[i+8] = min(dp[i+8], dp[i] + M)
    dp[i+12] = min(dp[i+12], dp[i] + L)

# 最小コストを出力
min_cost = min(dp[N:])
print(min_cost)

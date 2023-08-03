# Atcoder ABC245-C Choose Elements
# https://atcoder.jp/contests/abc245/tasks/abc245_c
#
# DPを使った解答例

import io
import sys

_INPUT = """\
4 1000000000
1 1 1000000000 1000000000
1 1000000000 1 1000000000
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []

for a, b in zip(A, B):
    C.append([a, b])
# print(C)

dp = [[False] * (2) for _ in range(N)]
dp[0][0], dp[0][1] = True, True

for i in range(N-1):
    for j in range(2):
        if dp[i][j] == True:
            if abs(C[i][j] - C[i+1][0]) <= K:
                dp[i+1][0] = True
            if abs(C[i][j] - C[i+1][1]) <= K:
                dp[i+1][1] = True

# print(dp)
print("Yes" if dp[N-1][0] or dp[N-1][1] else "No")

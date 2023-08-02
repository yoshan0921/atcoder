# Atcoder ABC240-C Jumping Takahashi
# https://atcoder.jp/contests/abc240/tasks/abc240_c
#
# DPを使った解答例

import io
import sys

_INPUT = """\
4 12
1 8
5 7
3 4
2 6
"""
sys.stdin = io.StringIO(_INPUT)

N, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[False] * (X + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(N):
    for j in range(X + 1):
        if dp[i][j] == True:

            if j + A[i][0] <= X:
                dp[i + 1][j + A[i][0]] = True

            if j + A[i][1] <= X:
                dp[i + 1][j + A[i][1]] = True

print("Yes" if dp[N][X] else "No")

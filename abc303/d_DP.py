# Atcoder ABC303-D Shift vs. CapsLock
# https://atcoder.jp/contests/abc303/tasks/abc303_d
#
# 動的計画法

import io
import sys

_INPUT = """\
1 3 3
AAaA
"""
sys.stdin = io.StringIO(_INPUT)

# X ミリ秒かけて a キーのみを押す。
# Y ミリ秒かけて Shift キーと a キーを同時に押す。
# Z ミリ秒かけて CapsLock キーを押す。


X, Y, Z = map(int, input().split())
S = input()

dp = [[0]*2 for _ in range(len(S) + 1)]

# dp[i][j]: capslockON(j=1), OFF(j=0)のときの最小値
# 初め、CapsLock キーのランプは OFF
dp[0][1] = 1 << 60

for i in range(len(S)):
    if S[i] == 'a':
        dp[i + 1][0] = min(dp[i][0] + X, dp[i][1] + Z + X)
        dp[i + 1][1] = min(dp[i][0] + Z + Y, dp[i][1] + Y)
    elif S[i] == 'A':
        dp[i + 1][0] = min(dp[i][0] + Y, dp[i][1] + Z + Y)
        dp[i + 1][1] = min(dp[i][0] + Z + X, dp[i][1] + X)

print(min(dp[-1]))

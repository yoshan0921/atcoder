# Atcoder ABC306-D Poisonous Full-Course
# https://atcoder.jp/contests/abc306/tasks/abc306_d
#
# 動的計画法

import io
import sys

_INPUT = """\
15
1 900000000
0 600000000
1 -300000000
0 -700000000
1 200000000
1 300000000
0 -600000000
1 -900000000
1 600000000
1 -100000000
1 -400000000
0 900000000
0 200000000
1 -500000000
1 900000000
"""
sys.stdin = io.StringIO(_INPUT)
N = int(input())
X = []

for i in range(N):
    x, y = input().split()
    X.append([int(x), int(y)])

# dpテーブルの初期化
INF = -10**60
dp = [[INF, INF] for _ in range(N+1)]

dp[0][0] = 0

for i in range(N):
    # 料理を食べない場合
    dp[i+1][0] = max(dp[i+1][0], dp[i][0])
    dp[i+1][1] = max(dp[i+1][1], dp[i][1])

    # 料理を食べる場合
    # 解毒剤入り料理
    if X[i][0] == 0:
        dp[i+1][0] = max(dp[i+1][0], dp[i][0] + X[i][1])
        dp[i+1][0] = max(dp[i+1][0], dp[i][1] + X[i][1])
    # 毒入り料理
    else:
        dp[i+1][1] = max(dp[i+1][1], dp[i][0] + X[i][1])

print(max(dp[N][0], dp[N][1]))

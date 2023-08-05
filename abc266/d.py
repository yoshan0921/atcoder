# Atcoder ABC266-D Snuke Panic (1D)
# https://atcoder.jp/contests/abc266/tasks/abc266_d
#
# DPを使った解答例

import io
import sys

_INPUT = """\
3
1 0 100
3 3 10
5 4 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
Tmax = 10**5

X = [0] * (Tmax + 1)
A = [0] * (Tmax + 1)
T = []
for i in range(N):
    t, x, a = map(int, input().split())

    X[t] = x
    A[t] = a

C = [[0] * 5 for i in range(Tmax + 1)]
for t, x, a in zip(T, X, A):
    C[t][x] = a

# DP[x][t]= 高橋君が時刻 t に座標 x にいるときの、それまでに捕まえたすぬけ君の大きさの合計の最大値
dp = [[-1] * 5 for _ in range(Tmax + 1)]
print(dp)
dp[0][0] = 0

for i in range(1, Tmax + 1):
    for j in range(5):
        dp[i][j] = (
                max(dp[i - 1][max(0, j - 1)], dp[i - 1][j], dp[i - 1][min(4, j + 1)]) + C[i][j]
            )
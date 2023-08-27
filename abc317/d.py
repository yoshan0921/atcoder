import io
import sys

_INPUT = """\
10
1878 2089 15
1982 1769 13
2148 1601 14
2189 2362 15
2268 2279 16
2394 2841 18
2926 2971 20
3091 2146 20
3878 4685 38
4504 4617 29
"""
sys.stdin = io.StringIO(_INPUT)

# 選挙区がN個ある。
# i番目の選挙区にはX+Yの有権者がいる。
# そのうちX人は高橋を、Y人は青木を支持している。
# それぞれの区の多数派が、その区の全Z議席を獲得する。
# 過半数の議席を獲得した方が勝利する。

INF = 10**19

N = int(input())
T_seat = 0
A_seat = 0
Total_seat = 0
Required_seat = 0

# 選挙区ごとに、勝つために必要な鞍替え数と獲得議席数を整理する
# Zone = 青木が勝利している選挙区のリスト
# K = 勝利のために必要な鞍替え数
# Z = 獲得議席数
Zone = []
for i in range(N):
    X, Y, Z = map(int, input().split())

    if X > Y:
        Total_seat += Z
        T_seat += Z
        K = 0
    else:
        Total_seat += Z
        A_seat += Z
        K = ((X + Y) // 2 + 1) - X
        Zone.append([K, Z])

# 高橋が勝つために必要な議席数を計算する
if T_seat > A_seat:
    Required_seat = 0
else:
    Required_seat = ((A_seat + T_seat) // 2 + 1) - T_seat

if Required_seat <= 0:
    print(0)
    exit(0)

# 動的計画法で、鞍替え数の最小値を求める
# dp[i][j] = i番目までの選挙区を見たときに、j個の議席を獲得するために必要な鞍替え数の最小値
dp = [[INF] * (Total_seat+1) for _ in range(len(Zone)+1)]
dp[0][0] = 0

for i in range(len(Zone)):
    for j in range(Total_seat+1):
        if dp[i][j] == INF:
            continue

        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

        if j + Zone[i][1] <= Total_seat:
            dp[i+1][j+Zone[i][1]] = min(dp[i+1]
                                        [j+Zone[i][1]], dp[i][j] + Zone[i][0])

# 鞍替え数の最小値が求まったので、獲得議席数がRequired_seat以上の最小値を求める
min_ppl = INF
for l in dp:
    for m in range(Required_seat, Total_seat+1):
        if l[m] != INF:
            min_ppl = min(min_ppl, l[m])

print(min_ppl)

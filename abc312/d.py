# Atcoder ABC312-D - Count Bracket Sequences
# https://atcoder.jp/contests/abc312/tasks/abc312_d
#
# 動的計画法

import io
import sys

_INPUT = """\
(???(?
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
# Sの長さをNとする
N = len(S)
# 添字を1始まりにするため先頭に適当な文字を追加
S = "!" + S

# dp[(i文字目まで見て)] ['(' - ')'の数]

dp = [[0] * (N+1) for _ in range(N+1)]
# 1文字も選ばずに、'(' - ')'=0になるように選ぶ方法は1通り
dp[0][0] = 1

MOD = 998244353

for i in range(N):
    for j in range(N):
        # もしS[i+1]が'('または'?'なら
        if S[i+1] in ('(', '?'):
            # (を選ぶ
            dp[i+1][j+1] += dp[i][j]
            # 余りをとる
            dp[i+1][j+1] %= MOD

        # もしS[i+1]が')'または'?'なら
        if S[i+1] in (')', '?'):
            # )を選ぶ j-1<0の時は考えない
            if j-1 < 0:
                continue
            dp[i+1][j-1] += dp[i][j]
            # 余りをとる
            dp[i+1][j-1] %= MOD

# N文字目まで見て'(' - ')'が0になる時が括弧列
print(dp[N][0])
# for i in dp:
#     print(i)

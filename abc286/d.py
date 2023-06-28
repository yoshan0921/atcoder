# Atcoder ABC286-D Money in Hand
# https://atcoder.jp/contests/abc286/tasks/abc286_d
#
# 動的計画法


import io
import sys

_INPUT = """\
2 19
2 3
5 6
"""
sys.stdin = io.StringIO(_INPUT)
N, X = map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(N)]
# print(AB)

dp = [False]*(X+1)
dp[0] = True

for _ in range(N):
    a, b = map(int, input().split())
    nx = [False]*(X+1)
    for i in range(X+1):
        # 今まで見た硬貨で作れる金額の場合
        if dp[i]:
            for j in range(b+1):

                if i+a*j <= X:
                    nx[i+a*j] = True
    dp = nx
if dp[-1]:
    print('Yes')
else:
    print('No')

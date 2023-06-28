# Atcoder ABC289-D Step Up Robot
# https://atcoder.jp/contests/abc289/tasks/abc289_d
#
# 動的計画法

# iがBに含まれているかどうか
# i より前の段 i-A[0], i-A[1], ... , i-A[N]が到達可能かどうか
# の2項目を確認すれば、i 段目に到達できるかどうかの計算が可能。

import io
import sys

_INPUT = """\
3
3 4 5
4
4 5 6 8
15
"""
sys.stdin = io.StringIO(_INPUT)
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
X = int(input())

dp = [0]*(X+1)
dp[0] = 1

for x in range(X+1):
    # Bに含まれる場合は無視
    if x in B:
        continue
    # step
    for a in A:
        # 0以上でかつBに含まれていない場合
        if x-a >= 0 and not x-a in B:
            dp[x] = max(dp[x], dp[x-a])


# print(dp)
if dp[-1] == 1:
    print('Yes')
else:
    print('No')

# 参考
# https://atcoder.jp/contests/abc322/submissions/46245075

import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
4 3 5
5 3 0 2
3 1 2 3
3 2 4 0
1 0 1 4
"""
sys.stdin = io.StringIO(_INPUT)

# N: 開発案の数 (<= 100)
# K: パラメータの数 (<= 5)
# P: 目標値 (<= 5)
N, K, P = map(int, input().split())

# 開発案のコストとパラメータ
Cost = []
A = []
for i in range(N):
    c, *a = map(int, input().split())
    Cost.append(c)
    A.append(a)

# print(Cost)
# print(A)

# dp[開発案][パラメータ状態] = その条件でのコストの最小値
INF = 10 ** 15
dp = [[INF] * ((P+1) ** K) for _ in range(N + 1)]
dp[0][0] = 0

# print(dp)


def base_n(num_10, n, K):
    '''
    10進数をn進数に変換する
    num_10: 10進数 
    n: 変換後の進数
    K: 桁数
    '''
    str_n = ''
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return list(str_n[::-1].zfill(K))


for i in range(N):
    dev_i = A[i]
    for j in range((P+1) ** K):

        # jをP+1進数に変換
        digit_j = base_n(j, P+1, K)
        # print(digit_j)

        # P+1進数に変換したjに開発案iのパラメータを加算し、再度10進数に変換
        s = 0
        for k in range(K):
            s += min(P, dev_i[k]+int(digit_j[k])) * (P+1)**(K-1-k)

        if dp[i][j] < INF:
            # 開発案iを採用する場合
            dp[i+1][min(s, (P+1) ** K - 1)] = min(dp[i+1]
                                                  [min(s, (P+1) ** K-1)], dp[i][j]+Cost[i])
            # 開発案iを採用しない場合
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])

if dp[-1][-1] == INF:
    print(-1)
else:
    print(dp[-1][-1])

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

N, K, P = map(int, input().split())
Dev = []
for i in range(N):
    Dev.append(list(map(int, input().split())))

INF = 10 ** 9
min_cost = INF

# 開発プランの組み合わせ
for i in range(1 << N):
    # パラメータを初期化
    Param = [0] * K
    # コストを初期化
    cost = 0

    # j番目の開発プランを適用するかどうか
    for j in range(N):
        # 適用する場合
        if i & (1 << j):
            # コストを加算
            cost += Dev[j][0]
            # コストがその時点の最小値を超えたら打ち切り
            if cost > min_cost:
                break
            # パラメータを更新
            for idx in range(K):
                Param[idx] += Dev[j][idx + 1]

    # パラメータがすべて目標達成できたか？
    # print(min(Param))
    if min(Param) < P:
        continue
    # コストがより低ければ更新
    # print("cost is updated", min_cost)
    min_cost = min(min_cost, cost)

if min_cost == INF:
    print(-1)
else:
    print(min_cost)

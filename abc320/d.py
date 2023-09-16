import math
import io
import sys
import bisect
import collections
import itertools

_INPUT = """\
5 7
1 2 0 0
1 2 0 0
2 3 0 0
3 1 0 0
2 1 0 0
3 2 0 0
4 5 0 0
"""

# 速度改善のために以下を実施
# 隣接リストの最適化：リストの代わりに、collections.defaultdictを使用して隣接リストを効率的に管理します。
# 再帰の最適化：再帰の代わりにループを使用して深さ優先探索を実行する。

sys.stdin = io.StringIO(_INPUT)
# sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
# G = [[] for _ in range(N+1)]
G = collections.defaultdict(list)
for _ in range(M):
    a, b, x, y = map(int, input().split())
    # 重複情報を除外
    if [b, x, y] not in G[a]:
        G[a].append([b, x, y])
    if [a, -x, -y] not in G[b]:
        G[b].append([a, -x, -y])
# print(G)

INF = 10**9
Person = [[INF, INF] for _ in range(N+1)]
Person[1] = [0, 0]
seen = [False] * (N+1)

stack = [1]
while stack:
    v = stack.pop()
    seen[v] = True
    for g in G[v]:
        p_next = g[0]
        x_dif = g[1]
        y_dif = g[2]
        if not seen[p_next]:
            Person[p_next] = [Person[v][0] + x_dif, Person[v][1] + y_dif]
            stack.append(p_next)

# def rec(v):
#     # print(Person)
#     seen[v] = True
#     for g in G[v]:
#         p_next = g[0]
#         x_dif = g[1]
#         y_dif = g[2]
#         if seen[p_next]:
#             continue
#         Person[p_next] = [Person[v][0] + x_dif, Person[v][1] + y_dif]
#         rec(p_next)
#     return


# # main
# rec(1)

# print(seen)
for p in range(1, N+1):
    if seen[p]:
        print(*Person[p])
    else:
        print("undecidable")

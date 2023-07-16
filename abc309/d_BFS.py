# Atcoder ABC309-D Add One Edge
# https://atcoder.jp/contests/abc309/tasks/abc309_d
#
# BFSを使った解答例

from collections import deque
import copy
import io
import sys

_INPUT = """\
3 4 6
1 2
2 3
4 5
4 6
1 3
6 7
"""
sys.stdin = io.StringIO(_INPUT)

# 入力
N1, N2, M = map(int, input().split())

graph = [[] for _ in range(N1 + N2)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

# 入力確認
# print(N1, N2, M)
# print(graph)

# 幅優先探索の関数


def bfs(u):
    # 変数の初期化
    queue = deque()
    distance = [-1] * (N1 + N2)

    # 頂点 u から幅優先探索
    queue.append(u)
    distance[u] = 0

    # 幅優先探索
    while queue:
        # 探索する頂点の取得
        v = queue.popleft()

        # 探索する頂点からつながっている頂点への探索
        for next_v in graph[v]:
            # 探索済みのとき
            if distance[next_v] != -1:
                continue

            # 次の頂点を追加
            queue.append(next_v)
            distance[next_v] = distance[v] + 1

    # 頂点 u からの最大距離を返す
    return max(distance)


# 頂点１からの最大距離
max_1 = bfs(1-1)

# 頂点N1＋N2からの最大距離
max_N1N2 = bfs(N1 + N2 - 1)

print(max_1 + max_N1N2 + 1)

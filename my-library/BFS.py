from collections import deque
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
print(N1, N2, M)
print(graph)

""" 出力結果
3 4 6
[[1, 2], [0, 2], [1, 0], [4, 5], [3], [3, 6], [5]]
"""

# 変数の初期化
queue = deque()
distance = [-1] * N

# 頂点0 から探索
queue.append(0)
distance[0] = 0

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

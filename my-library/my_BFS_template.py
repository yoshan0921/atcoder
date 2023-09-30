"""
Breadth First Search Template
"""

from collections import deque
import io
import sys

_INPUT = """\
6 7
0 1
0 5
1 3
1 5
2 3
3 4
4 5
"""
sys.stdin = io.StringIO(_INPUT)

# Input
N, M = map(int, input().split())

# グラフを表現する隣接リスト
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    # 頂点aから頂点bへの辺を隣接リストに入れる
    G[a].append(b)
    # 頂点bから頂点aへの辺を隣接リストに入れる
    G[b].append(a)

# グラフではなく座標問題の場合
# 四方向への移動を表すベクトル
# 0: 下、1: 右、2: 上、3: 左
# dxs = [1, 0, -1, 0]
# dys = [0, 1, 0, -1]

# 各頂点が何手目にチェックされたのか格納するリスト
checked = [-1] * N
checked[0] = 0

# 頂点0 から探索
queue = deque()
queue.append(0)

# キューが空になるまで継続する
while queue:
    # 探索する頂点をキューから取得する
    v = queue.popleft()

    # G[v]に含まれる頂点について確認する
    for v2 in G[v]:
        # v2がチェク済ならスキップする
        if checked[v2] != -1:
            continue

        # 次の頂点をキューに追加する
        queue.append(v2)
        checked[v2] = checked[v] + 1

    # グラフではなく座標問題の場合
    # マス (x, y) から 1 手で行けるマスを順に探索
    # for dx, dy in zip(dxs, dys):
    #     # 隣接マス
    #     x2, y2 = x + dx, y + dy

print(checked)

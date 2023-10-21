import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
5 47
.#..#..#####..#...#..#####..#...#...###...#####
.#.#...#.......#.#...#......##..#..#...#..#....
.##....#####....#....#####..#.#.#..#......#####
.#.#...#........#....#......#..##..#...#..#....
.#..#..#####....#....#####..#...#...###...#####
"""
sys.stdin = io.StringIO(_INPUT)

# Input
H, W = map(int, input().split())

G = []
for _ in range(H):
    G.append(list(input()))

# print(G)

# 四方向への移動を表すベクトル
# 0: 上、1: 右上、2: 右、3: 右下、4: 下、5: 左下、6: 左、7: 左上
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

# 各座標がチェックされたのか格納するリスト
checked = [[-1] * W for _ in range(H)]

queue = collections.deque()
count = 0

# キューが空になるまで継続する
for i in range(H):
    for j in range(W):
        if G[i][j] == "#":
            count += 1
            queue.append((i, j))
            G[i][j] = "."
            while queue:
                # 探索する頂点をキューから取得する
                x, y = queue.popleft()
                # print(x, y)
                # G[x][y] = "."

                # グラフではなく座標問題の場合
                # マス (x, y) から 1 手で行けるマスを順に探索
                for dx, dy in zip(dxs, dys):
                    # 隣接マス
                    x2, y2 = x + dx, y + dy

                    # 座標外ならスキップする
                    if x2 < 0 or x2 >= H or y2 < 0 or y2 >= W:
                        continue

                    # x2, y2がチェク済ならスキップする
                    # if checked[x2][y2] != -1:
                    if G[x2][y2] != "#":
                        continue

                    # 次の座標をキューに追加する
                    queue.append((x2, y2))
                    # checked[x2][y2] = 0
                    G[x2][y2] = "."

print(count)

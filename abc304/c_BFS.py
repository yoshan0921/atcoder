# Atcoder ABC304-C Virus
# https://atcoder.jp/contests/abc304/tasks/abc304_c
#
# BFSを使った解答例

import io
import queue
import sys
import math

_INPUT = """\
9 4
3 2
6 -1
1 6
6 5
-2 -3
5 3
2 -3
2 1
2 6
"""
sys.stdin = io.StringIO(_INPUT)

N, D = map(int, (input().split()))

# 各人の座標情報を読み込む
coordinate = [list(map(int, input().split())) for _ in range(N)]

# 各人の感染チェック結果
ans = ["No"] * N
# 人1は最初の感染者であるためYesとする。
ans[0] = "Yes"

q = queue.Queue()

# 最初の感染者である人1をキューに入れる。
q.put(0)
distance = 0
while not q.empty():
    idx = q.get()

    # キューから取り出した感染者idxを起点として、距離D以内に人がいないかチェックする。
    for i in range(N):
        # 人iが既に感染者であればスキップする。
        if ans[i] == "Yes":
            continue

        # 2点間の距離を計算
        dx = coordinate[idx][0]-coordinate[i][0]
        dy = coordinate[idx][1]-coordinate[i][1]
        distance = dx*dx+dy*dy

        # 2点間の距離がD以下である場合、人iを感染者とする。
        if distance <= D*D:
            ans[i] = "Yes"
            # 感染者iをキューに入れる。
            q.put(i)

for j in ans:
    print(j)

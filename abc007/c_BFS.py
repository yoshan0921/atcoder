# Atcoder ABC007-C Breadth-First Search
# https://atcoder.jp/contests/abc007/tasks/abc007_3
#
# BFSを使った解答例
import collections
import io
import sys

_INPUT = """\
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
"""
sys.stdin = io.StringIO(_INPUT)
H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

C = [list(input()) for _ in range(H)]

q = collections.deque()
q.append((sy-1, sx-1))

# 初期値は十分に大きい値にしておく
INF = 10**9

# 到達時点のステップ数を管理する配列
seen = [[INF] * W for _ in range(H)]
# スタート地点のステップ数を0にする
seen[sy-1][sx-1] = 0


while q:
    y, x = q.popleft()
    step = seen[y][x] + 1
    for yy, xx in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
        # 枠外を参照していたらスキップ
        if not (0 <= yy < H and 0 <= xx < W):
            continue
        # 空きマス、かつ、記録されているステップ数が現在のステップ数より大きい場合
        # ステップ数を現在のステップ数で更新し、キューに追加
        if C[yy][xx] == "." and seen[yy][xx] > step:
            seen[yy][xx] = step
            q.append((yy, xx))

print(seen[gy-1][gx-1])
for i in seen:
    for j in range(W):
        if i[j] == INF:
            i[j] = 0
    print(i)

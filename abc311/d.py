import collections
import io
import sys

_INPUT = """\
21 25
#########################
#..............###...####
#..............#..#...###
#........###...#...#...##
#........#..#..#........#
#...##...#..#..#...#....#
#..#..#..###...#..#.....#
#..#..#..#..#..###......#
#..####..#..#...........#
#..#..#..###............#
#..#..#.................#
#........##.............#
#.......#..#............#
#..........#....#.......#
#........###...##....#..#
#..........#..#.#...##..#
#.......#..#....#..#.#..#
##.......##.....#....#..#
###.............#....#..#
####.................#..#
#########################
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
# print(S)

q = collections.deque()

# 最初はマス(2, 2)からスタート
sy, sx = 2, 2
q.append((sy-1, sx-1))

# 到達マスを管理する配列
touch = [[False] * M for _ in range(N)]
# スタート地点をTrueにする
touch[sy-1][sx-1] = True
# print(touch)

# キューに追加したことがあるマスを管理する配列
checked = [[False] * M for _ in range(N)]
checked[sy-1][sx-1] = True

while q:
    y, x = q.popleft()
    # print(y, x)
    for yy, xx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        # 岩に当たるまで進む
        tmp_y = y
        tmp_x = x
        while True:
            tmp_y += yy
            tmp_x += xx
            # 氷だったらsenndをTrueにして次へ
            if S[tmp_y][tmp_x] == ".":
                touch[tmp_y][tmp_x] = True
            # 岩だったらマスのキューに追加してbreak
            elif S[tmp_y][tmp_x] == "#":
                if checked[tmp_y - yy][tmp_x - xx] == False:
                    q.append((tmp_y - yy, tmp_x - xx))
                    checked[tmp_y - yy][tmp_x - xx] = True
                break
ans = 0
for i in touch:
    # print(i)
    ans += i.count(True)
print(ans)

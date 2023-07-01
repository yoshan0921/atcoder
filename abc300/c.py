import io
import sys

_INPUT = """\
15 20
#.#..#.............#
.#....#....#.#....#.
#.#....#....#....#..
........#..#.#..#...
#.....#..#.....#....
.#...#....#...#..#.#
..#.#......#.#....#.
...#........#....#.#
..#.#......#.#......
.#...#....#...#.....
#.....#..#.....#....
........#.......#...
#.#....#....#.#..#..
.#....#......#....#.
#.#..#......#.#....#
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
ans = [0] * min(H, W)

for i in range(H):
    if i == 0 or i == H-1:
        continue
    for j in range(W):
        if j == 0 or j == W-1:
            continue
        if S[i][j] == '#':
            # バツ印の中心のかどうかをチェック
            if S[i-1][j-1] == '#' and S[i-1][j+1] == '#' and S[i+1][j-1] == '#' and S[i+1][j+1] == '#':
                # バツ印のサイズをチェック
                chk_distance = min(H-i, W-j)
                for k in range(chk_distance):
                    if S[i+k][j+k] != "#":
                        ans[k-2] += 1
                        break
                    if S[i+k][j+k] == "#" and k == chk_distance-1:
                        ans[k-1] += 1
                        break
print(*ans)

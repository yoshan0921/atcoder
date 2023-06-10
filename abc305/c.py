import io
import sys

_INPUT = """\
6 6
......
.#####
######
######
######
......
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
# print(H, W)

# itemlist = [list(map(int, input().split())) for _ in range(M)]
cookie_map = [list(input()) for _ in range(H)]
# print(cookie_map)


for i in range(H):
    flg1 = False
    flg2 = False
    d = 0
    for j in range(W):
        # print(cookie_map[i][j])
        if cookie_map[i][j] == ".":
            if j < W - 1 and cookie_map[i+1][j] == "#" and cookie_map[i][j+1] == "#":
                print(i+1, j+1)
                exit()
        if cookie_map[i][j] == "#":
            flg1 = True
            if cookie_map[i+1][j] == ".":
                print(i+2, j+1)
                exit()
        if cookie_map[i][j] == "." and flg1 == True:
            flg2 = True
            if cookie_map[i+1][j] == "#":
                print(i+1, j+1)
                exit()

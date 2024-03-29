import io
import sys

_INPUT = """\
18 18
######............
######............
######............
######............
######............
######............
..................
..................
..................
..................
..................
..................
............######
............######
............######
............######
............######
............######
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
ans = []

for i in range(N-8):
    for j in range(M-8):
        if S[i][j] == "#":
            # 左上部分の判定
            if S[i][j+1] == "#" and S[i][j+2] == "#" and S[i][j+3] == ".":
                if S[i+1][j] == "#" and S[i+1][j+1] == "#" and S[i+1][j+2] == "#" and S[i+1][j+3] == ".":
                    if S[i+2][j] == "#" and S[i+2][j+1] == "#" and S[i+2][j+2] == "#" and S[i+2][j+3] == ".":
                        if S[i+3][j] == "." and S[i+3][j+1] == "." and S[i+3][j+2] == "." and S[i+3][j+3] == ".":
                            # 右下部分の判定
                            if S[i+5][j+5] == "." and S[i+5][j+6] == "." and S[i+5][j+7] == "." and S[i+5][j+8] == ".":
                                if S[i+6][j+5] == "." and S[i+6][j+6] == "#" and S[i+6][j+7] == "#" and S[i+6][j+8] == "#":
                                    if S[i+7][j+5] == "." and S[i+7][j+6] == "#" and S[i+7][j+7] == "#" and S[i+7][j+8] == "#":
                                        if S[i+8][j+5] == "." and S[i+8][j+6] == "#" and S[i+8][j+7] == "#" and S[i+8][j+8] == "#":
                                            ans.append([i+1, j+1])

for count in ans:
    print(*count)

import io
import sys

_INPUT = """\
7 5
xssxx
xssxx
ekuns
xsskx
xsuxx
xnsxx
sxxxx
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
S = [input() for i in range(H)]

if H < 5 or W < 5:
    exit()

for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            # horizontal search #1
            if W - j >= 4:
                if S[i][j+1] == "n" and S[i][j+2] == "u" and S[i][j+3] == "k" and S[i][j+4] == "e":
                    print(i+1, j+1)
                    print(i+1, j+2)
                    print(i+1, j+3)
                    print(i+1, j+4)
                    print(i+1, j+5)
                    break
            # horizontal search #2
            if j >= 4:
                if S[i][j-1] == "n" and S[i][j-2] == "u" and S[i][j-3] == "k" and S[i][j-4] == "e":
                    print(i+1, j+1)
                    print(i+1, j+0)
                    print(i+1, j-1)
                    print(i+1, j-2)
                    print(i+1, j-3)
                    break
            # vertival search #1
            if H - i >= 4:
                if S[i+1][j] == "n" and S[i+2][j] == "u" and S[i+3][j] == "k" and S[i+4][j] == "e":
                    print(i+1, j+1)
                    print(i+2, j+1)
                    print(i+3, j+1)
                    print(i+4, j+1)
                    print(i+5, j+1)
                    break
            # vertival search #2
            if i >= 4:
                if S[i-1][j] == "n" and S[i-2][j] == "u" and S[i-3][j] == "k" and S[i-4][j] == "e":
                    print(i+1, j+1)
                    print(i+0, j+1)
                    print(i-1, j+1)
                    print(i-2, j+1)
                    print(i-3, j+1)
                    break
            # oblique search #1
            if W - j >= 4 and H - i >= 4:
                if S[i+1][j+1] == "n" and S[i+2][j+2] == "u" and S[i+3][j+3] == "k" and S[i+4][j+4] == "e":
                    print(i+1, j+1)
                    print(i+2, j+2)
                    print(i+3, j+3)
                    print(i+4, j+4)
                    print(i+5, j+5)
                    break
            # oblique search #2
            if j >= 4 and i >= 4:
                if S[i-1][j-1] == "n" and S[i-2][j-2] == "u" and S[i-3][j-3] == "k" and S[i-4][j-4] == "e":
                    print(i+1, j+1)
                    print(i+0, j+0)
                    print(i-1, j-1)
                    print(i-2, j-2)
                    print(i-3, j-3)
                    break
            # oblique search #3
            if W - j >= 4 and i >= 4:
                if S[i-1][j+1] == "n" and S[i-2][j+2] == "u" and S[i-3][j+3] == "k" and S[i-4][j+4] == "e":
                    print(i+1, j+1)
                    print(i+0, j+2)
                    print(i-1, j+3)
                    print(i-2, j+4)
                    print(i-3, j+5)
                    break
            # oblique search #4
            if j >= 4 and H - i >= 4:
                if S[i+1][j-1] == "n" and S[i+2][j-2] == "u" and S[i+3][j-3] == "k" and S[i+4][j-4] == "e":
                    print(i+1, j+1)
                    print(i+2, j+0)
                    print(i+3, j-1)
                    print(i+4, j-2)
                    print(i+5, j-3)
                    break
    else:
        continue
    break

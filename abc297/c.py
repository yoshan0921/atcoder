import io
import sys

_INPUT = """\
2 3
TTT
T.T
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W-1):
        if S[i][j] == ".":
            continue
        elif S[i][j] == "T" and S[i][j+1] == "T":
            S[i][j] = "P"
            S[i][j+1] = "C"

for k in S:
    print(*k, sep="")

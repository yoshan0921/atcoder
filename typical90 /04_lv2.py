import io
import sys
import itertools

_INPUT = """\
2 10
31 41 59 26 53 58 97 93 23 84
62 64 33 83 27 95 2 88 41 97
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
ans = [[0] * W for _ in range(H)]
row = [0] * H
col = [0] * W

for i in range(H):
    for j in range(W):
        row[i] += A[i][j]
        col[j] += A[i][j]

for a in range(H):
    for b in range(W):
        ans[a][b] = row[a] + col[b] - A[a][b]

for k in range(H):
    print(*ans[k])

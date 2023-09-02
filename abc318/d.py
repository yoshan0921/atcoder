import io
import sys

_INPUT = """\
4
1 5 4
7 8
6
"""
sys.stdin = io.StringIO(_INPUT)

# 1からNまでの番号がついた重み付き無効完全グラフ

N = int(input())
G = [[0] * N for _ in range(N)]
for i in range(N-1):
    score = list(map(int, input().split()))
    for j in range(i+1, N):
        G[i][j] = score[j-i-1]
        # G[j][i] = score[j-i-1]

print(G)

# 選べる辺の数
side = N // 2
print(side)

max_score = []
for g in G:
    max_score.append(max(g))

print(max_score)

for m in max_score:
    if m == 0:
        max_score.remove(m)

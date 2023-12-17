import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
4 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
1 3 2 5 4
11 13 12 15 14
6 8 7 10 9
16 18 17 20 19
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
print(A)
B = [list(map(int, input().split())) for _ in range(H)]
print(B)

# グリッドのサイズが小さいので、全探索できる。
# AとBの差分を抽出する。

g = collections.defaultdict(list)
for i in range(H):
    count = 0
    for j in range(H):
        for k in range(W):
            if A[i][k] == B[j][k]:
                count += 1
    if count <= W-2 and i != j:
        A[i], A[j] = A[j], A[i]

for i in range(W):
    count = 0
    for j in range(W):
        for k in range(H):
            if A[k][i] == B[k][j]:
                count += 1
    if count <= H-2 and i != j:
        for k in range(H):
            A[k][i], A[k][j] = A[k][j], A[k][i]

print(A)

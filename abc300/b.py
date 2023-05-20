import io
import sys

_INPUT = """\
4 3
..#
...
.#.
...
#..
...
.#.
...
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
# print(H, W)

A = [input() for i in range(H)]
B = [input() for i in range(H)]
# print(A[0])
# print(A[0][2])
# # print(B)

result = False
for sy in range(H):
    for sx in range(W):
        this_time = True
        for y in range(H):
            for x in range(W):
                if A[(y - sy) % H][(x - sx) % W] != B[y][x]:
                    this_time = False
                # print(A[(y - sy + H) % H][(x - sx + W) % W])
        if this_time:
            result = True

print("Yes" if result else "No")

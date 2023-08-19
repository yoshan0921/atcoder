import io
import sys

_INPUT = """\
4 3
aaa
aaa
abc
abd
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
cookie = [list(input()) for _ in range(H)]
mark = [[0] * W for _ in range(H)]

for c in cookie:
    print(c)
print("\n")

# 操作(1)
for i in range(H):
    for j in range(W):
        if cookie[i][0] != cookie[i][j]:
            break
    else:
        for k in range(W):
            mark[i][k] = 1

# 操作(2)
for j in range(W):
    for i in range(H):
        if cookie[0][j] != cookie[i][j]:
            break
    else:
        for k in range(H):
            mark[k][j] = 1

# 操作(3)
for i in range(H):
    for j in range(W):
        if mark[i][j] == 1:
            cookie[i][j] = "."


for c in cookie:
    print(c)
print("\n")

for m in mark:
    print(m)
print("\n")

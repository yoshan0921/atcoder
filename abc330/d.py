import math
import io
import sys
import bisect
import collections
import itertools
import math
sys.setrecursionlimit(10**9)

_INPUT = """\
15
xooxxooooxxxoox
oxxoxoxxxoxoxxo
oxxoxoxxxoxoxxx
ooooxooooxxoxxx
oxxoxoxxxoxoxxx
oxxoxoxxxoxoxxo
oxxoxooooxxxoox
xxxxxxxxxxxxxxx
xooxxxooxxxooox
oxxoxoxxoxoxxxo
xxxoxxxxoxoxxoo
xooxxxooxxoxoxo
xxxoxxxxoxooxxo
oxxoxoxxoxoxxxo
xooxxxooxxxooox
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = [input() for _ in range(N)]
row = [0] * N
col = [0] * N

for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            row[i] += 1
            col[j] += 1

ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            ans += (col[j]-1) * (row[i]-1)

print(ans)

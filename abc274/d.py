# Atcoder ABC274-D Robot Arms 2
# https://atcoder.jp/contests/abc274/tasks/abc274_d
#
# DPを使った解答例

import io
import sys

_INPUT = """\
3 -1 1
2 1 3
"""
sys.stdin = io.StringIO(_INPUT)

N, x, y = map(int, input().split())
A = list(map(int, input().split()))

dpx = [set() for _ in range(N + 1)]
dpy = [set() for _ in range(N + 1)]

# dpx[0].add(0)
dpx[1].add(A[0])
dpy[0].add(0)

for i in range(N):
    if i % 2 == 0:
        for j in dpx[i]:
            dpx[i + 1].add(j + A[i])
            dpx[i + 1].add(j - A[i])
        dpy[i + 1] = dpy[i]
    else:
        for j in dpy[i]:
            dpy[i + 1].add(j + A[i])
            dpy[i + 1].add(j - A[i])
        # dpx[i + 1].add(dpx[i])
        dpx[i + 1] = dpx[i]

if x in dpx[N] and y in dpy[N]:
    print("Yes")
else:
    print("No")

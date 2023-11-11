import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
30
73 8 55 26 97 48 37 47 35 55 5 17 62 2 60 23 99 73 34 75 7 46 82 84 29 41 32 31 52 32
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
D = list(map(int, input().split()))

ans = 0

for i in range(1, N+1):
    if i == 1:
        if D[i-1] >= 1:
            ans += 1
        if D[i-1] >= 11:
            ans += 1
    if i == 2:
        if D[i-1] >= 2:
            ans += 1
        if D[i-1] >= 22:
            ans += 1
    if i == 3:
        if D[i-1] >= 3:
            ans += 1
        if D[i-1] >= 33:
            ans += 1
    if i == 4:
        if D[i-1] >= 4:
            ans += 1
        if D[i-1] >= 44:
            ans += 1
    if i == 5:
        if D[i-1] >= 5:
            ans += 1
        if D[i-1] >= 55:
            ans += 1
    if i == 6:
        if D[i-1] >= 6:
            ans += 1
        if D[i-1] >= 66:
            ans += 1
    if i == 7:
        if D[i-1] >= 7:
            ans += 1
        if D[i-1] >= 77:
            ans += 1
    if i == 8:
        if D[i-1] >= 8:
            ans += 1
        if D[i-1] >= 88:
            ans += 1
    if i == 9:
        if D[i-1] >= 9:
            ans += 1
        if D[i-1] >= 99:
            ans += 1
    if i == 11:
        if D[i-1] >= 1:
            ans += 1
        if D[i-1] >= 11:
            ans += 1
    if i == 22:
        if D[i-1] >= 2:
            ans += 1
        if D[i-1] >= 22:
            ans += 1
    if i == 33:
        if D[i-1] >= 3:
            ans += 1
        if D[i-1] >= 33:
            ans += 1
    if i == 44:
        if D[i-1] >= 4:
            ans += 1
        if D[i-1] >= 44:
            ans += 1
    if i == 55:
        if D[i-1] >= 5:
            ans += 1
        if D[i-1] >= 55:
            ans += 1
    if i == 66:
        if D[i-1] >= 6:
            ans += 1
        if D[i-1] >= 66:
            ans += 1
    if i == 77:
        if D[i-1] >= 7:
            ans += 1
        if D[i-1] >= 77:
            ans += 1
    if i == 88:
        if D[i-1] >= 8:
            ans += 1
        if D[i-1] >= 88:
            ans += 1
    if i == 99:
        if D[i-1] >= 9:
            ans += 1
        if D[i-1] >= 99:
            ans += 1
print(ans)

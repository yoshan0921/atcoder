import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
3 10 10
11 10 9
"""
sys.stdin = io.StringIO(_INPUT)

N, L, R = map(int, input().split())
A = list(map(int, input().split()))

for a in A:
    if a <= L:
        print(L, end=" ")
    elif a >= R:
        print(R, end=" ")
    else:
        print(a, end=" ")

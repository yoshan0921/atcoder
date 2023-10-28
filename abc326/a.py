import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
5 2
"""
sys.stdin = io.StringIO(_INPUT)

X, Y = map(int, input().split())

if 0 < Y - X <= 2 or 0 < X - Y <= 3:
    print("Yes")
else:
    print("No")

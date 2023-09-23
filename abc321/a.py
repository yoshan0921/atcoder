import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
143513
"""
sys.stdin = io.StringIO(_INPUT)

N = input()

INF = 10**9
val = INF
for i in N:
    i = int(i)
    if i >= val:
        print("No")
        exit()
    val = i
print("Yes")

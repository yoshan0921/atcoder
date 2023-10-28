import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
100
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
for i in range(N, 920):
    if int(str(i)[0]) * int(str(i)[1]) == int(str(i)[2]):
        print(i)
        exit()

import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
10 50
31 41 59 26 53 58 97 93 23 84
"""
sys.stdin = io.StringIO(_INPUT)

N, L = map(int, input().split())
A = list(map(int, input().split()))
count = 0
for a in A:
    if a >= L:
        count += 1
print(count)

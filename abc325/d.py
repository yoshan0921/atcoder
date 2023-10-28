import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
5
1 1
1 1
2 1
1 2
1 4
"""
sys.stdin = io.StringIO(_INPUT)

# Input
N = int(input())
T1 = []
T2 = []
D = []
for _ in range(N):
    t, d = map(int, input().split())
    T1.append(t)
    T2.append(t+d)
    D.append(d)
print(T1, T2)

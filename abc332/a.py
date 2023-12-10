import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
2 2000 500
1000 1
1000 1
"""
sys.stdin = io.StringIO(_INPUT)

N, S, K = map(int, input().split())
fee = 0

for i in range(N):
    p, q = map(int, input().split())
    fee += p * q

if fee >= S:
    print(fee)
else:
    print(fee+K)

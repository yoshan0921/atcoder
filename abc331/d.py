import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
3 2
WWB
BBW
WBW
1 2 3 4
0 3 4 5
"""
sys.stdin = io.StringIO(_INPUT)

N, Q = map(int, input().split())
P = [[] for _ in range(N)]
for i in range(N):
    P[i] = list(input())
Query = [[] for _ in range(Q)]
for j in range(Q):
    Query[j] = list(map(int, input().split()))
print(Query)

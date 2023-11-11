import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
5 1
aaaaa
1 5
"""
sys.stdin = io.StringIO(_INPUT)

N, Q = map(int, input().split())
S = input()
C = [0] * N

count = 0
pre_c = ""
for i in range(len(S)):
    if S[i] == pre_c:
        count += 1
    pre_c = S[i]
    C[i] = count

# print(C)

for i in range(Q):
    l, r = map(int, input().split())
    print(C[r-1] - C[l-1])

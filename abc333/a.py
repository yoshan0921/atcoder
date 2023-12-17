import io
import sys
import bisect
import collections
import itertools
import math
sys.setrecursionlimit(10**9)

_INPUT = """\
9
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

ans = []
for i in range(N):
    ans.append(str(N))
print(''.join(ans))

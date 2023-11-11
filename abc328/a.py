import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
8 674
675 675 675 675 675 675 675 675
"""
sys.stdin = io.StringIO(_INPUT)

N, X = map(int, input().split())
S = list(map(int, input().split()))

ans = 0
for v in S:
    if v <= X:
        ans += v
print(ans)

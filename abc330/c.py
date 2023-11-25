import math
import io
import sys
import bisect
import collections
import itertools
import math
sys.setrecursionlimit(10**9)

_INPUT = """\
998244353
"""
sys.stdin = io.StringIO(_INPUT)

D = int(input())
X = int(math.sqrt(D))
min_value = D

for x in range(X, -1, -1):
    y = int(math.sqrt(D - x**2))
    if abs(x**2 + y**2 - D) < min_value:
        min_value = abs(x**2 + y**2 - D)
    if abs(x**2 + (y+1)**2 - D) < min_value:
        min_value = abs(x**2 + (y+1)**2 - D)
print(min_value)

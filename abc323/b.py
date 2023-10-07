import collections
import math
import io
import sys
import bisect

import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
3
oo-
o-x
oo-
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = []
ret = [0] * N

dict_int = collections.defaultdict(int)

for i in range(N):
    count = collections.Counter(list(input()))
    dict_int[i+1] = count['o']

# print(dict_int)

dict_sorted = dict(sorted(dict_int.items(), key=lambda x: (-x[1], x[0])))
# print(dict_sorted)

print(*list(dict_sorted))

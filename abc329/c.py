import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
1
x
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()

prev = S[0]
count = 0
dict = collections.defaultdict(int)

for i in range(N):
    if S[i] == prev:
        count += 1
        if i == N-1:
            dict[prev] = max(dict[prev], count)
    else:
        dict[prev] = max(dict[prev], count)
        count = 1
        prev = S[i]

ans = 0
for k, v in dict.items():
    ans += dict[k]
print(ans)

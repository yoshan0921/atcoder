import io
import sys
import bisect
import collections
import itertools
import math
sys.setrecursionlimit(10**9)

_INPUT = """\
19
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
ans = set()

val1 = "1"
val2 = "1"
val3 = "1"

for i in range(12):
    val1 = "1" * (i+1)
    for j in range(12):
        val2 = "1" * (j+1)
        for k in range(12):
            val3 = "1" * (k+1)
            # print(val1, val2, val3)
            ans.add(int(val1)+int(val2)+int(val3))

ans = list(ans)
ans.sort()
# print(ans)
print(ans[N-1])

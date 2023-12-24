import io
import sys
import bisect
import collections
import itertools
import math
sys.setrecursionlimit(10**9)

_INPUT = """\
8 5
1 2 4 7 8
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 1:
    print(0)
    exit(0)

# cumulative sum from the forward
A_cumsum_f = []
A_f = sorted(A)
# print(A_f)
for i in range(0, K-1, 2):
    if len(A_cumsum_f) == 0:
        A_cumsum_f.append(abs(A_f[i]-A_f[i+1]))
    else:
        A_cumsum_f.append(A_cumsum_f[-1] + abs(A_f[i]-A_f[i+1]))
# print(A_cumsum_f)


# cumulative sum from the backward
A_cumsum_b = []
A_b = sorted(A, reverse=True)
# print(A_b)
for i in range(0, K-1, 2):
    if len(A_cumsum_b) == 0:
        A_cumsum_b.append(abs(A_b[i]-A_b[i+1]))
    else:
        A_cumsum_b.append(A_cumsum_b[-1] + abs(A_b[i]-A_b[i+1]))
A_cumsum_b = A_cumsum_b[::-1]
# print(A_cumsum_b)


ans = 10**9

if K % 2 == 0:
    # In the case of an even number
    ans = A_cumsum_f[-1]
else:
    # In the case of an odd number
    for i in range(len(A_cumsum_f)+1):
        if i == 0:
            ans = min(ans, A_cumsum_b[i])
        elif i == len(A_cumsum_f):
            ans = min(ans, A_cumsum_f[i-1])
        else:
            ans = min(ans, A_cumsum_f[i-1] + A_cumsum_b[i])
print(ans)

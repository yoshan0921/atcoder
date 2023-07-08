import bisect
import itertools
import io
import sys

_INPUT = """\
2 3 2
3 10
2 5 15
"""
sys.stdin = io.StringIO(_INPUT)

N, M, D = map(int, input().split())
A = sorted(map(int, input().split()))
B = map(int, input().split())

# print(A)
# print(B)
Ans = -1

for b in B:
    ret = bisect.bisect_right(A, b+D) - 1
    if ret >= 0 and A[ret] >= b-D:
        Ans = max(Ans, A[ret]+b)

print(Ans)

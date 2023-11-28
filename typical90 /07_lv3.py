import io
import sys
import itertools
import bisect

_INPUT = """\
10
869120000 998244353 777777777 123456789 100100100 464646464 987654321 252525252 869120001 1000000000
10
4229
20210406
1
268435456
3582
536870912
1000000000
869120
99999999
869120001
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())

for i in range(Q):
    B = int(input())
    ret = bisect.bisect_left(A, B)
    if ret == 0:
        dissatisfaction = abs(A[ret]-B)
    elif ret == N:
        dissatisfaction = abs(A[ret-1]-B)
    else:
        dissatisfaction = min(abs(A[ret]-B), abs(A[ret-1]-B))
    print(dissatisfaction)

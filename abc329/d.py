import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
9 8
8 8 2 2 8 8 2 2
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = list(map(int, input().split()))

poll = [0] * (N+1)
top = 0
for i in range(M):
    poll[A[i]] += 1
    if i == 0:
        top = A[i]
    else:
        if poll[A[i]] > poll[top]:
            top = A[i]
        elif poll[A[i]] == poll[top]:
            if A[i] < top:
                top = A[i]
    # print(poll)
    # print(f'max(poll)= {max(poll)}')
    # print(f'A.index(max(poll))= {poll.index(max(poll))}')
    print(top)

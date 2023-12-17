"""
Bit Search Template
"""

import io
import sys

# Q1: Suppose there are N items, each with weight W and value V. Find the maximum value of the sum of their values, provided that the sum of their weights does not exceed M.
_INPUT1 = """\
5 10
1 4 2 1 5
7 4 5 9 1
"""
sys.stdin = io.StringIO(_INPUT1)

N, M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))

max_value = 0
for i in range(1 << N):
    weight = 0
    value = 0
    for j in range(N):
        # check if j-th bit of i is 1
        if i & (1 << j):
            weight += W[j]
            value += V[j]

    if weight <= M:
        max_value = max(max_value, value)

print(max_value)

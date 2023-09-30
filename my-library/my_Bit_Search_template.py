"""
Bit Search Template
"""

import io
import sys

_INPUT = """\
5 10
1 4 2 1 5
7 4 5 9 1
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))

max_value = 0
for i in range(1 << N):
    weight = 0
    value = 0
    for j in range(N):
        if i & (1 << j):
            weight += W[j]
            value += V[j]

    if weight <= M:
        max_value = max(max_value, value)

print(max_value)

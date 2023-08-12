import io
import sys

_INPUT = """\
4
4 7 3 7
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

num_sum = sum(A)

quotient = num_sum // N
reminder = num_sum % N

operation = 0

if reminder == 0:
    for i in range(N):
        if A[i] < quotient:
            operation += quotient - A[i]
else:
    ope1 = 0
    ope2 = 0
    for i in range(N):
        if A[i] < quotient:
            ope1 += quotient - A[i]
        elif A[i] > quotient + 1:
            ope2 += A[i] - (quotient + 1)
    operation = max(ope1, ope2)

print(operation)

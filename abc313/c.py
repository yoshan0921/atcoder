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
# print(quotient)
# print(reminder)
A.sort(reverse=True)
B = [quotient + reminder] * reminder + [quotient] * (N - reminder)
print(A)
print(B)

gap = 0
for a, b in zip(A, B):
    gap += abs(a - b)

print(gap // 2)

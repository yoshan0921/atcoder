import io
import sys

_INPUT = """\
123456789123456789 987654321
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())
# print(A, B)

q, r = A // B, A % B

if r > 0:
    q = q + 1

print(q)

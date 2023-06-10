import io
import sys

_INPUT = """\
21
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

q, r = N // 5, N % 5
# print(q, r)

if r >= 3:
    print(5*(q+1))
else:
    print(5*q)

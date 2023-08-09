import io
import sys

_INPUT = """\
2 0
141421356 17320508
"""
sys.stdin = io.StringIO(_INPUT)

N, X = map(int, input().split())
A = set(map(int, input().split()))
# print(A)

for i in A:
    if (i + X) in A:
        print("Yes")
        exit(0)
print("No")

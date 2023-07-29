import io
import sys

_INPUT = """\
3 8
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())
count = 0

while True:
    if A == B:
        print(count)
        exit(0)

    if A > B:
        q, r = A // B, A % B
        count += q
        A = r
        if A == 0:
            A += B
            count -= 1
    elif A < B:
        q, r = B // A, B % A
        count += q
        B = r
        if B == 0:
            B += A
            count -= 1

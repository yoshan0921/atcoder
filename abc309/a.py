import io
import sys

_INPUT = """\
3 4
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())

if abs(A-B) != 1:
    print("No")
    exit(0)
if B in (2, 5, 8, 3, 6, 9):
    print("Yes")
else:
    print("No")

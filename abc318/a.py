import io
import sys

_INPUT = """\
200000 314 318
"""
sys.stdin = io.StringIO(_INPUT)

N, M, P = map(int, input().split())
temp = N - M
print((temp // P) + 1)

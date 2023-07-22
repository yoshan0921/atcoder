import io
import sys

_INPUT = """\
4 500
100 600 1100 1600
"""
sys.stdin = io.StringIO(_INPUT)

N, D = map(int, input().split())
T = list(map(int, input().split()))

for i in range(N-1):
    if T[i+1] - T[i] <= D:
        print(T[i+1])
        exit(0)
print(-1)

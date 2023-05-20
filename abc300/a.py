import io
import sys

_INPUT = """\
3 125 175
200 300 400
"""
sys.stdin = io.StringIO(_INPUT)

N, A, B = map(int, input().split())
C = list(map(int, input().split()))

Answer = A + B

for i in range(N):
    if C[i] == Answer:
        print(i+1)

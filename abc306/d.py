import io
import sys

_INPUT = """\
5
1 100
1 300
0 -200
1 500
1 300
"""
sys.stdin = io.StringIO(_INPUT)
N = int(input())
X = []

for i in range(N):
    x, y = input().split()
    X.append([int(x), int(y)])

print(X)

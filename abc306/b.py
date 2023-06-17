import io
import sys

_INPUT = """\
1 0 1 0 1 0 0 0 0 1 0 0 1 1 0 1 1 1 1 0 0 0 1 0 0 1 1 1 1 1 1 0 0 0 0 1 0 1 0 1 0 1 1 1 1 0 0 1 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0
"""
sys.stdin = io.StringIO(_INPUT)

N = list(map(int, input().split()))

ans = 0
for i in range(len(N)):
    if N[i] == 1:
        ans += 2**i

print(ans)

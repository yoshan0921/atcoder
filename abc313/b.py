import collections
import io
import sys

_INPUT = """\
3 2
1 2
2 3
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

ans = set(range(1, N+1))

for i in A:
    ans.discard(i[1])

print(-1 if len(ans) != 1 else ans.pop())

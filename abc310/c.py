import io
import sys

_INPUT = """\
6
a
abc
de
cba
de
abc
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = []
for i in range(N):
    S.append(input())

ans = set()
for j in (S):
    ans.add(min(j, j[::-1]))

print(len(ans))

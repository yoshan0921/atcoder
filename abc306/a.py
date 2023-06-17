import io
import sys

_INPUT = """\
3
aaa
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()
ans = []

for i in range(N):
    ans.append(S[i])
    ans.append(S[i])

print(''.join(ans))

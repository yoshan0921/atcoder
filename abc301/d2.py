import io
import sys


_INPUT = """\
?0?10??0??0???0??0??0??0???0??0??0??0??
100
"""
sys.stdin = io.StringIO(_INPUT)

S, N = list(reversed(input())), int(input())
s = 0
for i in range(len(S)):
    s |= (S[i] == '1') << i
if s > N:
    print(-1)
else:
    for i in reversed(range(len(S))):
        if S[i] == '?' and (s | 1 << i) <= N:
            s |= 1 << i
    print(s)

import collections
import io
import sys

_INPUT = """\
8
a(b)(d)c
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()
Ans = ""

dque = collections.deque([])

for i in range(N):
    if S[i] != "(" and S[i] != ")":
        Ans += S[i]
    elif S[i] == "(":
        Ans += S[i]
        dque.append(len(Ans)-1)
    elif S[i] == ")":
        if dque:
            index = dque.pop()
            Ans = Ans[:index]
        else:
            Ans += S[i]
print(Ans)

import io
import sys

_INPUT = """\
ch@ku@ai
choku@@i
"""
sys.stdin = io.StringIO(_INPUT)

S = list(input())
T = list(input())
S2 = S.copy()
T2 = T.copy()

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            print("i=" + str(i))
            print("j=" + str(j))

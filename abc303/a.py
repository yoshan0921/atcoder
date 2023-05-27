import io
import sys

_INPUT = """\
4
nok0
n0ko
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()
T = input()
# print(N)
# print(S, T)

answer = "Yes"
for i in range(N):
    if S[i] == T[i]:
        continue
    elif S[i] == "0" and T[i] == "o":
        continue
    elif S[i] == "o" and T[i] == "0":
        continue
    elif S[i] == "1" and T[i] == "l":
        continue
    elif S[i] == "l" and T[i] == "1":
        continue
    else:
        answer = "No"

print(answer)

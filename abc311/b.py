import io
import sys

_INPUT = """\
5 15
oxooooooooooooo
oxooxooooooooox
oxoooooooooooox
oxxxooooooxooox
oxooooooooxooox
"""
sys.stdin = io.StringIO(_INPUT)

N, D = map(int, input().split())
S = [list(input()) for _ in range(N)]
# print(S)

ans = 0
ans_max = 0

for i in range(D):
    if S[0][i] == "x":
        cavation = False
        ans = 0
        continue
    else:
        vacation = True

    for j in range(N):
        if j == 0:
            continue
        if S[j][i] == "x":
            vacation = False
            break

    if vacation:
        ans += 1
        ans_max = max(ans, ans_max)
    else:
        ans = 0
print(ans_max)

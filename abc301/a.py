import io
import sys

_INPUT = """\
5
TTAAT
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
W = (N+2-1)//2
S = list(input())

win_t, win_a = 0, 0

for i in range(N):
    if (S[i] == "T"):
        win_t += 1
    else:
        win_a += 1

    if win_t >= W:
        print("T")
        break
    elif win_a >= W:
        print("A")
        break

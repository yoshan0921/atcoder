import io
import sys

_INPUT = """\
3
14159 26535 89793 23846 26433 83279 50288 41971 69399 37510 58209 74944 59230 78164 6286 20899 86280 34825 34211 70679 82148
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

W = 0
Ans = []

for i in range(N*7):
    W += A[i]
    if (i+1) % 7 == 0:
        Ans.append(W)
        W = 0

print(*Ans)

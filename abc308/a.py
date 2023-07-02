import io
import sys

_INPUT = """\
0 23 24 145 301 413 631 632
"""
sys.stdin = io.StringIO(_INPUT)

S = list(map(int, input().split()))

for i in range(len(S)):
    if i == 0:
        continue
    if S[i] < S[i-1]:
        print("No")
        exit(0)

for i in range(len(S)):
    if S[i] < 100 or S[i] > 675:
        print("No")
        exit(0)

for i in range(len(S)):
    if S[i] % 25 != 0:
        print("No")
        exit(0)

print("Yes")

import io
import sys

_INPUT = """\
BRKRBQNN
"""
sys.stdin = io.StringIO(_INPUT)

S = input()

B_flg = False
B1 = 0
B2 = 0

R_count = 0

for i in range(len(S)):
    if S[i] == "B" and not B_flg:
        B_flg = True
        B1 = i + 1
        continue
    elif S[i] == "B" and B_flg:
        B2 = i + 1
else:
    if (B1 + B2) % 2 == 0:
        print("No")
        exit(0)

for j in range(len(S)):
    if S[j] == "R":
        R_count += 1
    elif S[j] == "K" and R_count == 1:
        print("Yes")
        exit(0)
print("No")

import io
import sys

_INPUT = """\
5
-----
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = list(input())
# print(S)

flg_pass = False
for i in S:
    if i == "x":
        print("No")
        break
    if i == "o":
        flg_pass = True
else:
    if flg_pass:
        print("Yes")
    else:
        print("No")

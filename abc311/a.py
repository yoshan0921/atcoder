import io
import sys

_INPUT = """\
30
AABABBBABABBABABCABACAABCBACCA
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()

FlgA = False
FlgB = False
FlgC = False

for i in range(len(S)):
    if S[i] == "A":
        FlgA = True
    elif S[i] == "B":
        FlgB = True
    elif S[i] == "C":
        FlgC = True

    if FlgA and FlgB and FlgC:
        print(i+1)
        exit(0)

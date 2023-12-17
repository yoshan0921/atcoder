import io
import sys
import bisect
import collections
import itertools
import math
sys.setrecursionlimit(10**9)

_INPUT = """\
BD
BD
"""
sys.stdin = io.StringIO(_INPUT)

CHARS = "ABCDE"

S = input()
S1, S2 = S[0], S[1]
T = input()
T1, T2 = T[0], T[1]

flgS = False
flgT = False

if S1 == "A":
    if S2 == "B" or S2 == "E":
        flgS = True
elif S1 == "B":
    if S2 == "A" or S2 == "C":
        flgS = True
elif S1 == "C":
    if S2 == "B" or S2 == "D":
        flgS = True
elif S1 == "D":
    if S2 == "C" or S2 == "E":
        flgS = True
elif S1 == "E":
    if S2 == "A" or S2 == "D":
        flgS = True

if T1 == "A":
    if T2 == "B" or T2 == "E":
        flgT = True
elif T1 == "B":
    if T2 == "A" or T2 == "C":
        flgT = True
elif T1 == "C":
    if T2 == "B" or T2 == "D":
        flgT = True
elif T1 == "D":
    if T2 == "C" or T2 == "E":
        flgT = True
elif T1 == "E":
    if T2 == "A" or T2 == "D":
        flgT = True

if flgS == flgT:
    print("Yes")
else:
    print("No")

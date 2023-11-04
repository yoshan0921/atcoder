import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
7
atcoder
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()

flg = "No"

for i in range(N):
    if S[i] == "a":
        if i < N-1:
            if S[i+1] == "b":
                flg = "Yes"
        if i > 0:
            if S[i-1] == "b":
                flg = "Yes"
print(flg)

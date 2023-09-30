import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
20
BBAAABBACAACABCBABAB
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()
for c in range(N):
    if S[c] == "A":
        if c > N-3:
            print(-1)
            exit()
        if S[c+1] == "B":
            if S[c+2] == "C":
                print(c+1)
                exit()

print(-1)

import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
2 1
01
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
S = input()

muji = M
logo = 0
max_logo = 0

for i in range(N):
    # 洗濯
    if S[i] == "0":
        muji = M
        logo = 0
    # 食事
    elif S[i] == "1":
        if muji > 0:
            muji -= 1
        else:
            logo -= 1
            if abs(logo) > max_logo:
                max_logo = abs(logo)
    # 仕事
    elif S[i] == "2":
        logo -= 1
        if abs(logo) > max_logo:
            max_logo = abs(logo)

print(max_logo)

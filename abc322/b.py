import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
1 1
a
b
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
S = input()
T = input()

flg_head = False
flg_end = False

if T[:N] == S:
    flg_head = True

if T[-N:] == S:
    flg_end = True

if flg_head and flg_end:
    print(0)
elif flg_head:
    print(1)
elif flg_end:
    print(2)
else:
    print(3)

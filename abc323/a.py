import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
1000000000000000
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
for idx, val in enumerate(S):
    # idxが偶数の場合
    if (idx+1) % 2 == 0:
        if val == "0":
            continue
        else:
            print("No")
            exit(0)
print("Yes")

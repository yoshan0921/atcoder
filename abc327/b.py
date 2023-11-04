import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
10000000000
"""
sys.stdin = io.StringIO(_INPUT)


B = int(input())


def check_A(B):
    for A in range(1, int(math.log(B, 2)) + 2):
        if A ** A == B:
            return A
    return -1


print(check_A(B))

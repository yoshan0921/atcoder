import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
8
22 22 18 16 22 18 18 22
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(set(A), reverse=True)
print(sorted_A[1])

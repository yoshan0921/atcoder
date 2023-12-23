import io
import sys
import bisect
import collections
import itertools
import math
sys.setrecursionlimit(10**9)

_INPUT = """\
334 343
"""
sys.stdin = io.StringIO(_INPUT)

B, G = map(int, input().split())

if B > G:
    print("Bat")
else:
    print("Glove")

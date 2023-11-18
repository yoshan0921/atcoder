import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
OOXXOO
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
print(*S)

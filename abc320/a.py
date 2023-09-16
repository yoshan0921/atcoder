import math
import io
import sys
import bisect
import collections
import itertools

_INPUT = """\
9 9
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())
ret = A**B + B**A
print(ret)

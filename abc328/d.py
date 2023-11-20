import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

sys.setrecursionlimit(10**9)

_INPUT = """\
AAABCABCABCAABCABCBBBAABCBCCCAAABCBCBCC
"""
sys.stdin = io.StringIO(_INPUT)

S = input()

stack = []
for char in S:
    stack.append(char)
    if stack[-3:] == list('ABC'):
        # 高速化する上でここが重要だった。
        for _ in range(3):
            stack.pop()
        # del stack[-3:]

print(''.join(stack))

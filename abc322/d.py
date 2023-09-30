import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
....
###.
.#..
....
....
.###
.##.
....
..#.
.##.
.##.
.##.
"""
sys.stdin = io.StringIO(_INPUT)

P1 = []
P2 = []
P3 = []

for i in range(4):
    P1.append(list(input()))
for i in range(4):
    P2.append(list(input()))
for i in range(4):
    P3.append(list(input()))
print(P1)
print(P2)
print(P3)

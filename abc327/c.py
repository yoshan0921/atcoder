import numpy as np
import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)


_INPUT = """\
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
2 3 4 5 6 7 8 9 1
5 6 7 8 9 1 2 3 4
8 9 1 2 3 4 5 6 7
3 4 5 6 7 8 9 1 2
6 7 8 9 1 2 3 4 5
9 1 2 3 4 5 6 7 8
"""
sys.stdin = io.StringIO(_INPUT)

A = []
for i in range(9):
    A.append(list(map(int, input().split())))

for i in A:
    if len(set(i)) != 9:
        print("No")
        exit()

# Aを90度回転
A_rot = np.rot90(A)
# print(A_rot)

for i in A_rot:
    if len(set(i)) != 9:
        print("No")
        exit()


def check_subgrid(A):
    for i in range(0, 9, 3):
        print(i)
        for j in range(0, 9, 3):
            subgrid = [A[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if len(set(subgrid)) != 9:
                return False
    return True


if check_subgrid(A):
    print("Yes")
else:
    print("No")

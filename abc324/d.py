import math
import io
import sys
import bisect
import collections
import itertools
import time
sys.setrecursionlimit(10**6)

# START
start_time = time.perf_counter()

_INPUT = """\
13
8694027811503
"""
sys.stdin = io.StringIO(_INPUT)


def is_square(n):
    return n > 0 and int(n**0.5)**2 == n


N = int(input())
S = sorted(input())
MAX_A = round(10 ** (N/2))
count = 0

for a in range(MAX_A + 1):
    count += S == sorted("{:0{}}".format(a**2, N))

# data = list(itertools.permutations(S, N))
# data = list(itertools.product(S, repeat=N))
# data = set(data)
# for d in data:
#     if is_square(int("".join(d))):
#         print(d)
#         count += 1
print(count)

# END
# end_time = time.perf_counter()

# 経過時間を出力(秒)
# elapsed_time = end_time - start_time
# print(elapsed_time)

import io
import sys
import bisect
import collections
import itertools

_INPUT = """\
30 8
8 55 26 97 48 37 47 35 55 5 17 62 2 60 23 99 73 34 75 7 46 82 84 29 41 32 31 52 32 60
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
L = list(map(int, input().split()))
# print(L)
min_width = sum(L) // M
# print(min_width)

min_width2 = 0
L_sorted = sorted(L, reverse=True)
for i in range(len(L_sorted)-1):
    min_width2 = max(min_width2, L_sorted[i] + L_sorted[i+1])
print(min_width2)

count = []
for i in range(len(L)):
    if i == 0:
        count.append(L[i])
    else:
        count.append(count[i-1] + 1+L[i])
print(count)

for i in range(len(count)):
    if count[i] < min_width2:
        continue
    if count[i] >= min_width2:
        print(count[i])
        exit()

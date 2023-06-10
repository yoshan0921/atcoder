import io
import sys
import bisect

_INPUT = """\
21
0 20 62 192 284 310 323 324 352 374 409 452 486 512 523 594 677 814 838 946 1000
10
77 721
255 541
478 970
369 466
343 541
42 165
16 618
222 592
730 983
338 747
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

# fA[i] = How many hours did he sleep by A[i]
fA = [0 for _ in range(N)]
for i in range(1, N):
    if i % 2 == 0:
        fA[i] = fA[i-1] + A[i] - A[i-1]
    else:
        fA[i] = fA[i-1]

# How many hours did he sleep by the time


def calc_stime(time):
    index = bisect.bisect_left(A, time) - 1
    stime = fA[index] + (time - A[index]) * \
        ((fA[index+1] - fA[index]) / (A[index+1] - A[index]))
    return int(stime)


Q = int(input())
for i in range(Q):
    start, end = map(int, input().split())
    print(calc_stime(end) - calc_stime(start))

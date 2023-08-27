import io
import sys

_INPUT = """\
8
3 1 4 5 9 2 6 8
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A)
# print(sorted_A)

for i in range(1, N):
    # print(sorted_A[i], sorted_A[i-1])
    if sorted_A[i] - sorted_A[i-1] != 1:
        print(sorted_A[i]-1)
        exit(0)
else:
    print(sorted_A[i]+1)

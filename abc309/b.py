import copy
import io
import sys

_INPUT = """\
5
01010
01001
10110
00110
01010
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = [list(input()) for _ in range(N)]
B = copy.deepcopy(A)
# print(A)

for i in range(N):
    for j in range(N):
        if i == 0:
            if j == 0:
                B[i][j] = A[i+1][j]
            elif j >= 1 and j <= N-1:
                B[i][j] = A[i][j-1]
        elif i == N-1:
            if j == N-1:
                B[i][j] = A[i-1][j]
            elif j >= 0 and j <= N-1:
                B[i][j] = A[i][j+1]
        else:
            if j == 0:
                B[i][j] = A[i+1][j]
            elif j == N-1:
                B[i][j] = A[i-1][j]

for k in range(N):
    print("".join(B[k]))

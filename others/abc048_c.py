import io
import sys

_INPUT = """\
5 9
3 1 4 1 5
"""
sys.stdin = io.StringIO(_INPUT)

N, X = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    if A[i] > X:
        count += (A[i] - X)
        A[i] -= (A[i] - X)

for j in range(N-1):
    if A[j] + A[j+1] > X:
        count += (A[j] + A[j+1] - X)
        A[j+1] -= (A[j] + A[j+1] - X)

# print(A)
print(count)

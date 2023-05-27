import io
import sys

_INPUT = """\
10 10
4 10 7 2 8 3 9 1 6 5
3 6 2 9 1 8 10 7 4 5
9 3 4 5 7 10 1 8 2 6
7 3 1 8 4 9 5 6 2 10
5 2 1 4 10 7 9 8 3 6
5 8 1 6 9 3 2 4 7 10
8 10 3 4 5 7 2 9 6 1
3 10 2 7 8 5 1 4 9 6
10 6 1 5 4 2 3 8 9 7
4 5 9 1 8 2 7 6 3 10
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())

listdata = []
for i in range(M):
    listdata.append(input().split())
# print(listdata)

myset = set()

for j in listdata:
    for k in range(N-1):
        if j[k] < j[k+1]:
            myset.add((j[k], j[k+1]))
        else:
            myset.add((j[k+1], j[k]))

maxnum = N * (N-1) // 2
print(maxnum - len(myset))

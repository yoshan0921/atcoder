from collections import deque
import io
import sys

_INPUT = """\
8 3
apzbqrcs
1 2 3 1 2 2 1 2
"""
sys.stdin = io.StringIO(_INPUT)

# 長さNの文字列Sである
# 文字列Sの各文字の色はM色のうちのどれかである
# 文字列Sの各文字の色はC_iである

N, M = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))

group_by_color = [[] for _ in range(M)]

for i in range(N):
    group_by_color[C[i]-1].append(S[i])

for i in range(M):
    temp = deque(group_by_color[i])
    temp.rotate(1)
    group_by_color[i] = temp

result = []
for k in C:
    temp = group_by_color[k-1].popleft()
    result.append(temp)

for s in result:
    print(s, end="")

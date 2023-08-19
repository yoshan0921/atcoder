import io
import sys

_INPUT = """\
3
30 31 30
"""
sys.stdin = io.StringIO(_INPUT)
M = int(input())
D = list(map(int, input().split()))

cumlativeD = []
for i in range(M):
    if i == 0:
        cumlativeD.append(D[i])
    else:
        cumlativeD.append(D[i]+cumlativeD[i-1])

center_date = cumlativeD[-1]//2 + 1
# print(center_date)
# print(cumlativeD)

ans_M = 1
ans_D = 1
for j in range(M):
    if center_date == cumlativeD[j]:
        ans_M = j + 1
        ans_D = D[j]
        break

    if center_date < cumlativeD[j]:
        ans_M = j + 1
        if j == 0:
            ans_D = center_date
        else:
            ans_D = center_date - cumlativeD[j-1]
        break

print(ans_M, ans_D)

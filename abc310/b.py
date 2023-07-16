import io
import sys

_INPUT = """\
4 4
3 1 1
3 1 2
3 1 2
4 2 2 3
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
P = []
F = set()
for i in range(N):
    P.append(list(map(int, input().split())))

P_sorted = sorted(P)
# print(P_sorted)

for j in range(len(P_sorted)-1):
    if P_sorted[j][0] >= P_sorted[j+1][0]:
        tmp_1 = set()
        tmp_2 = set()
        for k in range(P_sorted[j][1]):
            tmp_1.add(P_sorted[j][k+2])
        for k in range(P_sorted[j+1][1]):
            tmp_2.add(P_sorted[j+1][k+2])
        if tmp_1 >= tmp_2:
            if P_sorted[j][0] > P_sorted[j+1][0] or len(tmp_1) > len(tmp_2):
                print("Yes")
                exit(0)
print("No")

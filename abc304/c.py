import io
import sys
import math
import numpy

_INPUT = """\
9 4
3 2
6 -1
1 6
6 5
-2 -3
5 3
2 -3
2 1
2 6
"""
sys.stdin = io.StringIO(_INPUT)

N, D = map(int, (input().split()))
print(N, D)
coordinate = [list(map(int, input().split())) for _ in range(N)]
# print(coordinate)

ret = ["No"] * N
ret[0] = "Yes"
print(ret)

# 各人から距離がD以内の人を整理する。
personWithinD = []

for i in range(len(coordinate)):
    temp_list = []
    for j in range(len(coordinate)):
        if i == j:
            continue
        a = numpy.array(coordinate[i])
        b = numpy.array(coordinate[j])
        distance = numpy.linalg.norm(b-a)
        # print(distance)
        if distance <= D:
            temp_list.append(j)
    else:
        personWithinD.append(temp_list)

print(personWithinD)

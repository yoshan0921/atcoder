import io
import queue
import sys
import math

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
# print(N, D)
coordinate = [list(map(int, input().split())) for _ in range(N)]
# print(coordinate)

ans = ["No"] * N
ans[0] = "Yes"
# print(ans)

q = queue.Queue()
q.put(0)
distance = 0
while not q.empty():
    idx = q.get()
    # print("idx=" + str(idx))
    # print(q.queue)
    for i in range(1, N):
        if ans[i] == "Yes":
            continue

        dx = coordinate[idx][0]-coordinate[i][0]
        dy = coordinate[idx][1]-coordinate[i][1]
        distance = dx*dx+dy*dy
        # print("distance=" + str(distance))

        if distance <= D*D:
            ans[i] = "Yes"
            q.put(i)

for j in ans:
    print(j)

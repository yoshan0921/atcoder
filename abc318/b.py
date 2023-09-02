import io
import sys

_INPUT = """\
3
0 1 0 1
0 3 0 5
5 10 0 10
"""
sys.stdin = io.StringIO(_INPUT)
N = int(input())

sheet = [[0] * 100 for _ in range(100)]

paper = []
for _ in range(N):
    x1, x2, y1, y2 = map(int, input().split())
    paper.append([x1, x2, y1, y2])
# print(paper)

for i in range(N):
    x1, x2, y1, y2 = paper[i]
    # print(x1, x2, y1, y2)
    for j in range(x1, x2):
        # print(j)
        for k in range(y1, y2):
            # print(k)
            sheet[j][k] = 1

ans = 0
for i in range(100):
    ans += sum(sheet[i])
print(ans)

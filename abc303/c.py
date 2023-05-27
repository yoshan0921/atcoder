import io
import sys

_INPUT = """\
5 2 1 5
LDRLD
0 0
-1 -1
"""
sys.stdin = io.StringIO(_INPUT)

N, M, H, K = list(map(int, input().split()))
S = list(input())

# itemlist = [list(map(int, input().split())) for _ in range(M)]
# itemlist = {map(int, input().split()) for _ in range(M)}
itemlist = set()
for i in range(M):
    u, v = map(int, input().split())
    itemlist.add((u, v))
print(itemlist)

x = 0
y = 0
answer = "Yes"

for i in S:
    if H <= 0:
        answer = "No"
        break

    if i == "R":
        x += 1
    elif i == "U":
        y += 1
    elif i == "D":
        y -= 1
    elif i == "L":
        x -= 1

    H -= 1

    # in <List型>は遅いため、in <Set型>に変更
    if H < K and (x, y) in itemlist:
        H = K
        itemlist.remove((x, y))

print(answer)

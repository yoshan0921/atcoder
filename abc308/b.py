import io
import sys

_INPUT = """\
3 2
code queen atcoder
king queen
10 1 1
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
D.insert(0, "other")

P = list(map(int, list(input().split())))

dict = {}

for i in range(len(D)):
    dict[D[i]] = P[i]

ans = 0
for j in range(len(C)):
    if C[j] in dict:
        ans += dict[C[j]]
    else:
        ans += dict["other"]
print(ans)

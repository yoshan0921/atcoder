import io
import sys
from collections import defaultdict

_INPUT = """\
ch@kud@i
akidu@ho
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
T = input()
Scnt = defaultdict(int)
Tcnt = defaultdict(int)
for c in S:
    Scnt[c] += 1
for c in T:
    Tcnt[c] += 1

print(Scnt)
print(Tcnt)

for c in "atcoder":
    M = max(Scnt[c], Tcnt[c])
    if Scnt['@'] < M-Scnt[c] or Tcnt['@'] < M-Tcnt[c]:
        print("No")
        exit()

    # print("M=" + str(M))
    # print(Scnt[c])
    # print(Tcnt[c])

    Scnt['@'] -= M-Scnt[c]
    Scnt[c] = M
    Tcnt['@'] -= M-Tcnt[c]
    Tcnt[c] = M

print(Scnt)
print(Tcnt)
print("Yes" if Scnt == Tcnt else "No")

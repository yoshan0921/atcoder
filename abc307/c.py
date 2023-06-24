import io
import sys

_INPUT = """\
3 5
#.#..
.....
.#...
2 2
#.
.#
5 3
...
#.#
.#.
.#.
...
"""
sys.stdin = io.StringIO(_INPUT)

HA, WA = map(int, input().split())
A = [input() for _ in range(HA)]
print(A)

HB, WB = map(int, input().split())
B = [input() for _ in range(HB)]
print(B)

HX, WX = map(int, input().split())
X = [input() for _ in range(HX)]
print(X)

for i in range(HX):
    for j in range(WX):
        print(X[i][j], end="")

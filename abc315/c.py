import io
import sys

_INPUT = """\
4
4 10
3 2
2 4
4 12
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
Ice = [list(map(int, input().split())) for _ in range(N)]
# print(Ice)

Ice_sorted = sorted(Ice, key=lambda x: -x[1])
# print(Ice_sorted)

max_val = 0
for i in range(N-1):
    if Ice_sorted[i][0] == Ice_sorted[i+1][0]:
        ret = Ice_sorted[0][1] + int(Ice_sorted[i+1][1] / 2)
    elif Ice_sorted[i][0] != Ice_sorted[i+1][0]:
        ret = Ice_sorted[0][1] + Ice_sorted[i+1][1]
    max_val = max(max_val, ret)

print(max_val)

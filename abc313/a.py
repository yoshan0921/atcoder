import io
import sys

_INPUT = """\
3
100 100 4
"""
sys.stdin = io.StringIO(_INPUT)
N = int(input())
P = list(map(int, input().split()))

if N == 1:
    print(0)
    exit(0)

dif = max(P) - P[0]
# 最大値がP0の場合
if dif == 0:
    sorted_P = sorted(P, reverse=True)
    # P0と同じ値が存在する場合
    if sorted_P[0] == sorted_P[1]:
        print(1)
    else:
        print(0)
# 最大値がP0以外の場合
else:
    print(dif + 1)

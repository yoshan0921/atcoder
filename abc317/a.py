import io
import sys

_INPUT = """\
10 500 999
38 420 490 585 613 614 760 926 945 999
"""
sys.stdin = io.StringIO(_INPUT)

# 薬の種類 N
# 現在の体力 H
# 実現したいモンスターの体力 X
N, H, X = map(int, input().split())
P = list(map(int, input().split()))

Gap = X - H
for i in range(N):
    if Gap <= P[i]:
        print(i+1)
        exit()

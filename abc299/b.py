import io
import sys

_INPUT = """\
2 1000000000
1000000000 1
1 1000000000
"""
sys.stdin = io.StringIO(_INPUT)

N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

t_max = -1
t_idx = -1

# 色がTであるカードのインデックスを取得
for i in range(N):
    if C[i] == T and R[i] > t_max:
        t_max = R[i]
        t_idx = i
if t_idx != -1:
    print(t_idx+1)
    exit(0)
else:
    for i in range(N):
        if C[i] == C[0] and R[i] > t_max:
            t_max = R[i]
            t_idx = i
    if t_idx != -1:
        print(t_idx+1)
        exit(0)

import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
7 8
500 500 500 500 500 500 500 500
xxxxxxxx
oxxxxxxx
ooxxxxxx
oooxxxxx
ooooxxxx
oooooxxx
ooooooxx
"""
sys.stdin = io.StringIO(_INPUT)

# N人のプレイヤー
# M問のクイズ
N, M = map(int, input().split())

# i番目のクイズはAi点(500-2500)
A = list(map(int, input().split()))
# A_sort = sorted(A, reverse=True)
# A_sort_a = list(itertools.accumulate(A_sort))
# print(A)
# print(A_sort)
# print(A_sort_a)

# 各プレイヤーの現時点の正解状況
Status = []
for i in range(N):
    Status.append(list(input()))
# print(Status)

# 各プレイヤーの現時点の得点
Score = [0] * N
for i in range(len(Status)):
    for j in range(len(Status[i])):
        if Status[i][j] == 'o':
            Score[i] += A[j]
    Score[i] += i+1

# print(Score)
for i in range(len(Score)):
    # print(max(Score) - s)
    if max(Score) - Score[i] == 0:
        print(0)
    else:
        A_remain = []
        for j in range(len(Status[i])):
            if Status[i][j] == 'x':
                A_remain.append(A[j])
        A_sort = sorted(A_remain, reverse=True)
        A_sort_a = list(itertools.accumulate(A_sort))
        # print(A_sort_a)
        for idx, val in enumerate(A_sort_a):
            if max(Score) - Score[i] < val:
                print(idx+1)
                break

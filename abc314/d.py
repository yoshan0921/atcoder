from collections import deque
import io
import sys

_INPUT = """\
7
AtCoder
5
1 4 i
3 0 a
1 5 b
2 0 a
1 4 Y
"""
sys.stdin = io.StringIO(_INPUT)

# 長さNの文字列Sが与えられる
# 文字列Sに対してQ回の操作を行う
# 操作は（t, x, c）で表される
# t =1 のとき、Sのx文字目をcに変更する
# t =2 のとき、Sに含まれる大文字を全て小文字に変更
# t =3 のとき、Sに含まれる小文字を全て大文字に変更

N = int(input())
S = list(input())
Q = int(input())
T = [[] for _ in range(Q)]

for i in range(Q):
    T[i] = list(input().split())

change_index = 0

for j in range(1, Q+1):
    if T[-j][0] != "1":
        change_index = Q - j
        break

for i in range(Q):
    if T[i][0] == "1":
        S[int(T[i][1])-1] = T[i][2]
    if T[i][0] == "2" and i == change_index:
        for s in range(N):
            S[s] = S[s].lower()
    if T[i][0] == "3" and i == change_index:
        for s in range(N):
            S[s] = S[s].upper()

for s in S:
    print(s, end="")

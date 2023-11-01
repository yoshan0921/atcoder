import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
1000000000 1000000000 10
1 1
10 10
100 100
1000 1000
10000 10000
100000 100000
1000000 1000000
10000000 10000000
100000000 100000000
1000000000 1000000000
"""
sys.stdin = io.StringIO(_INPUT)

H, W, N = map(int, input().split())
A, B = [], []

# 元々の座標を取得
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# 昇順にソート
SA = sorted(list(set(A)))
SB = sorted(list(set(B)))

# 辞書化（値：昇順）
Adict = {x: i+1 for i, x in enumerate(SA)}
Bdict = {y: i+1 for i, y in enumerate(SB)}

# 出力
for i in range(N):
    # 元々の座標について、縦横座標を昇順の数字で置き換え（座標圧縮）
    print(Adict[A[i]], Bdict[B[i]])

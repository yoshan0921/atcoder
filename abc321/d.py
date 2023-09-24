import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
2 2 7
3 5
6 1
"""
sys.stdin = io.StringIO(_INPUT)

# 主菜N種類、副菜M種類、価格min(s,P)
N, M, P = map(int, input().split())
# 主菜の価格
A = list(map(int, input().split()))
# 副菜の価格
B = list(map(int, input().split()))

# 価格を小さい順にソートする。
A.sort()
B.sort()
B_acc = [0] + list(itertools.accumulate(B))  # 累積和
# print(B_acc)

ans = 0
for a in A:
    # a + b >= P
    # b >= P - a
    # 副菜の価格がP-aより大きいかどうかを二分探索する。
    idx = bisect.bisect_left(B, P - a)
    # print(B)
    # print(P-a)
    # print(idx)
    # print("-----")

    # 副菜の価格がP-aより大きい場合、価格をPとする。
    ans += P * (M - idx)
    # 副菜の価格がP-aより小さい場合、価格をa+bとする。
    ans += (a * idx) + B_acc[idx]
print(ans)

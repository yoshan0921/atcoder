import io
import sys
import bisect
import collections
import itertools
import math
sys.setrecursionlimit(10**9)

_INPUT = """\
-177018739841739480 2436426 -80154573737296504 585335723211047198

"""
sys.stdin = io.StringIO(_INPUT)

A, M, L, R = map(int, input().split())

r_tree_num = 0
l_tree_num = 0
tree_num = 0

# AがLとRの間にある場合
if R >= A and L <= A:
    r_dif = R - A
    l_dif = A - L
    r_tree_num = (r_dif // M)
    l_tree_num = (l_dif // M)
    tree_num = r_tree_num + l_tree_num + 1
# AがRより右にある場合
elif R < A:
    r_dif = A - R
    l_dif = A - L
    r_tree_num = (r_dif // M)
    l_tree_num = (l_dif // M)
    tree_num = l_tree_num - r_tree_num
    # 地点RLがどちらもちょうど木がある場合は、上記の計算で1つ多く引きすぎてしまうため調整
    if (A-R) % M == 0 and (A-L) % M == 0:
        tree_num += 1
    # RとLが同じ地点で、その地点にちょうど木がある場合
    if R == L and (A-R) % M == 0:
        tree_num = 1
# AがLより左にある場合
elif L > A:
    r_dif = R - A
    l_dif = L - A
    r_tree_num = (r_dif // M)
    l_tree_num = (l_dif // M)
    tree_num = r_tree_num - l_tree_num
    # 地点RLがどちらもちょうど木がある場合は、上記の計算で1つ多く引きすぎてしまうため調整
    if (L-A) % M == 0 and (R-A) % M == 0:
        tree_num += 1
    # RとLが同じ地点で、その地点にちょうど木がある場合
    if R == L and (L-A) % M == 0:
        tree_num = 1

print(tree_num)

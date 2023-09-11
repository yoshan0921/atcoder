import math
import io
import sys
import bisect
import collections
import itertools

_INPUT = """\
3 1 9
2 5 6
2 7 1
"""
sys.stdin = io.StringIO(_INPUT)


c = [list(map(int, input().split())) for _ in range(3)]

# 縦横斜のライン
A = [(0, 4, 8), (2, 4, 6)]
for i in range(3):
    tpl = tuple(i * 3 + j for j in range(3))
    A.append(tpl)
for j in range(3):
    tpl = tuple(i * 3 + j for i in range(3))
    A.append(tpl)


def is_ok_tuple(tpl, perm):
    """
    がっかりする = はじめに知ったほうの2マスに書かれた数字が同じであり、
    最後に知ったマスに書かれた数字がそれと異なる場合。
    高橋くんががっかりしてしまうならFalseを返し、がっかりしないならTrueを返す。
    そのラインの中で最初に見た数と2番目に見た数が同じ時にFalseを返し、
    それ以外はすべてTrueを返す。
    """
    T = []
    for pos in tpl:
        i, j = divmod(pos, 3)
        T.append((perm[pos], c[i][j]))
    T.sort()
    return T[0][1] != T[1][1]


# tpl = (3, 4, 5)
# perm = (8, 7, 6, 5, 1, 4, 0, 2, 3)
# is_ok_tuple(tpl, perm)

ok_cnt = 0
# 順列を全て列挙する
for perm in itertools.permutations(range(9)):
    # print(perm)
    is_ok = True
    for tpl in A:
        if not is_ok_tuple(tpl, perm):
            is_ok = False
            break
    if is_ok:
        ok_cnt += 1

ans = ok_cnt / math.prod(range(1, 10))
print(ans)

import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
777
"""
sys.stdin = io.StringIO(_INPUT)

K = int(input())
ans = []

for flg in range(1 << 10):
    # 9から0までの数字を使うかどうかの2進10桁のフラグ
    # print(format(flg, 'b'))

    # 何もフラグが立っていない場合（使う数字がない）はスキップする。
    if flg == 0:
        continue

    # 0は正の整数に含まれないのでスキップする。（0のフラグだけ立っている場合）
    if flg == 1:
        continue

    num = 0
    for idx in range(9, -1, -1):
        # print(idx)
        # 9から0までフラグが立っているか順番に確認する。
        if flg & (1 << idx):
            # フラグが立っていたら、その数字を使う。
            # print(idx)
            # 数字を10倍して、次の桁にする。
            num *= 10
            # 1桁目に数字を足す。
            num += idx
    # 数字が完成したので、ansに追加する。
    ans.append(num)

# ansを小さい順にソートする。
ans.sort()
# K番目の数字を出力する。
print(ans[K-1])

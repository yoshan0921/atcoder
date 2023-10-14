import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
5 ababc
ababc
babc
abacbc
abdbc
abbac
"""
sys.stdin = io.StringIO(_INPUT)

N, M = input().split()
N = int(N)
S = [input() for _ in range(N)]

K = 0
Klist = []


for idx in range(len(S)):
    front_match = 0
    back_match = 0
    # print(M, S[idx])
    # 先頭から数えて一致する文字数
    for j in range(min(len(M), len(S[idx]))):
        if M[j] == S[idx][j]:
            front_match += 1
        else:
            break
    # 最後から数えて一致する文字数
    for j in range(min(len(M), len(S[idx]))):
        if M[-j-1] == S[idx][-j-1]:
            back_match += 1
        else:
            break
    # print(front_match, back_match, len(M))

    # 完全一致
    if front_match == back_match == len(M) == len(S[idx]):
        K += 1
        Klist.append(idx+1)
        # print("完全一致")
    # 1文字削除？
    elif front_match + back_match >= len(M) - 1 == len(S[idx]):
        K += 1
        Klist.append(idx+1)
        # print("一文字削除")
    # 1文字追加？
    elif front_match + back_match >= len(M) == len(S[idx]) - 1:
        K += 1
        Klist.append(idx+1)
        # print("一文字追加")
    # 1文字置換？
    elif front_match + back_match == len(M) - 1 == len(S[idx]) - 1:
        K += 1
        Klist.append(idx+1)
    # else:
    #     print("その他")

print(K)
print(*Klist)

import math
import io
import sys
import bisect
import collections
import itertools

_INPUT = """\
TOYOT
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
count1 = 0
for i in range(len(S)):
    for j in range(i, len(S)):
        if S[i:j+1] == S[i:j+1][::-1]:
            count1 = max(count1, j+1-i)
print(count1)

# リバースした文字列に含まれるかどうかで判定すると1件だけWAになる。
# 該当ケースがわからないので、とりあえずコメントアウトしておく。

# count2 = 0
# R = S[::-1]
# for i in range(len(S)):
#     for j in range(i, len(S)):
#         if S[i:j+1] in R:
#             count2 = max(count2, j+1-i)
# print(count2)

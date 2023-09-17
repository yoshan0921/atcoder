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
# R = S[::-1]

count1 = 0
for i in range(len(S)):
    for j in range(i, len(S)):
        # リバースした文字列に含まれるかどうかで判定すると1件だけWAになる。
        # WAになるケースが分からない・・・。
        # if S[i:j+1] in R:
        if S[i:j+1] == S[i:j+1][::-1]:
            count1 = max(count1, j+1-i)
print(count1)

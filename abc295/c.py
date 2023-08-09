import collections
import io
import sys

_INPUT = """\
10
295 2 29 295 29 2 29 295 2 29
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

dict = collections.defaultdict(int)
for i in A:
    dict[i] += 1

count = 0
for j in dict:
    # print(dict[j])
    count += dict[j] // 2

print(count)

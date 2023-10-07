import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
1
1000000000 1000000000
"""
sys.stdin = io.StringIO(_INPUT)

# N種類のサイズのスライム
N = int(input())

# 合体可能なスライム
deque = collections.deque([])

# サイズ別のスライムの数
Size = collections.defaultdict(int)
for _ in range(N):
    a, b = map(int, input().split())
    Size[a] = b
    if b >= 2:
        deque.append(a)

# 2つのスライムを選んで合体させる
while deque:
    # print(deque)
    size = deque.popleft()
    num = Size[size]
    # print(size)
    # print(Size)

    # 合体後の結果を反映
    new_size = size * 2
    new_num = num // 2
    remain_num = num % 2

    if new_num > 0:
        Size[size] = remain_num
        Size[new_size] += new_num
        if remain_num == 0:
            del Size[size]
        if Size[new_size] >= 2:
            deque.append(new_size)
    # print(Size)

ret = 0
for size, num in Size.items():
    ret += num
print(ret)

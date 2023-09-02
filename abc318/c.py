import io
import sys

_INPUT = """\
3 1 10
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)

# N日間の旅行
# 1日パスは、D枚セットでP円
N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)

# リストからn個ずつ取り出してリストにする関数


def split_list_func(mylist, n):
    for elem in range(0, len(mylist), n):
        yield mylist[elem:(elem + n)]


split_F = list(split_list_func(F, D))
# print(split_F)

ans = 0
for x in split_F:
    if sum(x) < P:
        ans += sum(x)
    else:
        ans += P
print(ans)

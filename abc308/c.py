import io
import sys

_INPUT = """\
4
999999999 1000000000
333333333 999999999
1000000000 999999997
999999998 1000000000
"""
sys.stdin = io.StringIO(_INPUT)

INF = 10 ** 20

N = int(input())
list = []
ans = []

for i in range(N):
    a, b = map(int, input().split())
    list.append([i+1, INF * a // (a+b)])

ans = sorted(list, key=lambda i: (i[1], -i[0]), reverse=True)

ans_print = []
for i in (ans):
    ans_print.append(i[0])
print(*ans_print)

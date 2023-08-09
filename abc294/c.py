import io
import sys

_INPUT = """\
4 3
3 14 15 92
6 53 58
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


C = sorted(A + B)
get_index = {c: i + 1 for i, c in enumerate(C)}
# print(get_index)

a = [get_index[a] for a in A]
b = [get_index[b] for b in B]

print(*a)
print(*b)

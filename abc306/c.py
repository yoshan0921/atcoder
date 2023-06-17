import io
import sys

_INPUT = """\
3
1 1 3 2 3 2 2 3 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
p_list = {key+1: 0 for key in range(N)}
c_list = {key+1: 0 for key in range(N)}

for i in range(len(A)):
    c_list[A[i]] = c_list[A[i]] + 1
    if c_list[A[i]] < 3:
        p_list[A[i]] = i + 1

ans = sorted(p_list.items(), key=lambda i: i[1])

for k in range(len(ans)):
    print(ans[k][0], end=' ')

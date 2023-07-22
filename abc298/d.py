from collections import deque
import io
import sys

_INPUT = """\
11
1 9
1 9
1 8
1 2
1 4
1 4
1 3
1 5
1 3
2
3
"""
sys.stdin = io.StringIO(_INPUT)

Q = int(input())
S = deque([1])
fix = 998244353
query = []
ans = 1

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        S.append(query[1])
        ans = (ans * 10 + query[1]) % fix
    elif query[0] == 2:
        x = S.popleft()
        ans = ans - x * pow(10, len(S), fix)
    elif query[0] == 3:
        print(ans % fix)

import io
import sys
import collections

_INPUT = """\
4 10
1
1
3
2 1
1
2 3
3
1
2 2
3
"""
sys.stdin = io.StringIO(_INPUT)

N, Q = map(int, input().split())

# 待っている人（受付に呼ばれていない）
que = 1
# 受付に呼ばれた人
call = collections.defaultdict(int)

for _ in range(Q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        call[que] = 1
        que += 1
    elif event[0] == 2:
        call.pop(event[1])
    elif event[0] == 3:
        print(next(iter(call)))

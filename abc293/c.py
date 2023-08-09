import itertools
import io
import sys

_INPUT = """\
2 2
3 2
2 2
"""
sys.stdin = io.StringIO(_INPUT)

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
# print(a)


def dfs(y, x, s: set) -> int:
    if (y, x) == (h-1, w-1):
        return 1
    count = 0

    if (x+1 <= w-1) and (y <= h-1) and (a[y][x+1] not in s):
        s.add(a[y][x+1])
        count += dfs(y, x+1, s)
        s.remove(a[y][x+1])
    if (x <= w-1) and (y+1 <= h-1) and (a[y+1][x] not in s):
        s.add(a[y+1][x])
        count += dfs(y+1, x, s)
        s.remove(a[y+1][x])
    return count


ans = dfs(0, 0, {a[0][0]})
print(ans)

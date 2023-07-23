import collections
import io
import sys

_INPUT = """\
2
2 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, ("0 " + input()).split()))

# 通って来たルートを記録する。
route = []

# 重複チェック
checked = set()

# 回答表示用のリスト
ans = []

now = 1
for c in range(N):
    now = A[now]
    if now in checked:
        ans = route[route.index(now):]
        break
    else:
        route.append(now)
        checked.add(now)

# 1周しても重複がない場合、前提条件として必ず閉路があるため以下となる。
if ans == []:
    ans = route

# print(route)
print(len(ans))
print(*ans)

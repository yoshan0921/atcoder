# Atcoder ABC284-C Count Connected Components
# DFSを使った解答例

import io
import sys

_INPUT = """\
5 3
1 2
1 3
4 5
"""
sys.stdin = io.StringIO(_INPUT)


def dfs(v):
    seen[v] = True
    for next_v in e[v]:
        if not seen[next_v]:
            dfs(next_v)


N, M = map(int, input().split())

# グラフ情報の読み込み
e = [[] for i in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)
# else:
#     print(e)


ans = 0

# 訪問済みチェックリスト
seen = [False] * (N + 1)

for i in range(1, N + 1):
    if not seen[i]:
        ans += 1
        # 一度dfsをコールすると、iから連結している全ての頂点に訪問済みチェックが入る。
        dfs(i)

print(ans)

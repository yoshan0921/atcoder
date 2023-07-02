# Atcoder ABC308-D Snuke Maze
# https://atcoder.jp/contests/abc308/tasks/abc308_d
#
# BFSを使った解答例

import collections
import io
import sys

_INPUT = """\
3 3
sns
nxx
uke
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

q = collections.deque()
q.append((0, 0))

# チェック済みのマスを管理する配列
seen = [[False] * W for _ in range(H)]
seen[0][0] = True

T = "snuke"


def check_next(i, j, ii, jj):
    if S[i][j] not in T or S[ii][jj] not in T:
        return False
    if (T.index(S[i][j]) + 1) % 5 == T.index(S[ii][jj]):
        return True
    else:
        return False


if S[0][0] not in T:
    print("No")
    exit(0)

while q:
    i, j = q.popleft()
    char = S[i][j]
    for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        # 枠外を参照していたらスキップ
        if not (0 <= ii < H and 0 <= jj < W):
            continue
        # 既に訪れていたらスキップ
        if seen[ii][jj]:
            continue
        # 次の文字が一致していたらキューに追加
        if check_next(i, j, ii, jj):
            seen[ii][jj] = True
            q.append((ii, jj))

if seen[H-1][W-1]:
    print("Yes")
else:
    print("No")

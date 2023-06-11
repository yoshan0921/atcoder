# Atcoder ABC287-C Path Graph?
# https://atcoder.jp/contests/abc287/tasks/abc287_c
# Union Findを使った解答例

from collections import defaultdict
import io
import sys

_INPUT = """\
4 3
1 3
4 2
3 2
"""
sys.stdin = io.StringIO(_INPUT)


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


N, M = map(int, input().split())

uf = UnionFind(N)

# 辺の数がN-1本であること
if M != N - 1:
    print("No")
    exit()

# グラフ情報の読み込み
graph = [[] for i in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    uf.unite(u-1, v-1)
# else:
#     print(graph)
#     print(uf.group_count())
#     print(uf.all_group_members())

if uf.group_count() != 1:
    print("No")
    exit()

for i in graph:
    if len(i) >= 3:
        print("No")
        exit()

print("Yes")
exit()

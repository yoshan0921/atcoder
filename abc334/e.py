import io
import sys
import bisect
import collections
import itertools
import math
sys.setrecursionlimit(10**9)

_INPUT = """\
3 4
#...
.#.#
..##
"""
sys.stdin = io.StringIO(_INPUT)


class UnionFind_v2:
    # Initialize
    def __init__(self, n):
        """
        Manage n elements by numbering them 0 ~ n - 1.
        """
        # List containing the number of the parent element of each element
        # If the element is the root, the value is -1
        self.parent = [-1] * n
        # Height of the rooted tree to which element x belongs
        self.rank = [0] * n
        # Size (number of elements) of the group to which element x belongs
        self.size = [1] * n

    # Seek root
    def root(self, x):
        if self.parent[x] == -1:
            return x  # x is the root
        else:
            self.parent[x] = self.root(self.parent[x])  # routing compression
            return self.parent[x]

    # Show all roots
    def roots(self):
        return [i for i, x in enumerate(self.parent) if x < 0]

    # Check if x and y belong to the same group
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # Merge the group containing x with the group containing y
    def unite(self, x, y):
        # Get the roots of both sides of x and y
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False  # Do nothing when already in the same group

        # Shorter rooted trees are merged under longer rooted trees
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx

        # If the height of the tree is the same, the depth increases by 1
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        # The size of the group is the sum of the sizes of the two groups
        self.size[rx] += self.size[ry]

        return True

    # Find the size of the rooted tree containing x
    def group_size(self, x):
        return self.size[self.root(x)]


if __name__ == "__main__":
    # Input
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    uf = UnionFind_v2(H*W)
    count = 0
    red = []

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                for next_i, next_j in [(i+1, j), (i, j+1)]:
                    if not (0 <= next_i < H and 0 <= next_j < W):
                        continue
                    if S[next_i][next_j] == "#":
                        uf.unite(i*W+j, next_i*W+next_j)
            else:
                red.append((i, j))

    # original number of connected cells groups
    org_num = len(uf.roots())-len(red)
    # Expected number of connected cellsn when each ret cell is changed to green
    ans = []

    dhs = [-1, 0, 1, 0]
    dws = [0, -1, 0, 1]
    for h, w in red:
        check_group = set()
        for dh, dw in zip(dhs, dws):
            next_h, next_w = h + dh, w + dw
            if not (0 <= next_h < H and 0 <= next_w < W):
                continue
            if S[next_h][next_w] == "#":
                check_group.add(uf.root(next_h*W+next_w))
        # print(check_group)
        ans.append(org_num - len(check_group) + 1)

    mod = 998244353
    m = (sum(ans) * pow(len(ans), mod-2, mod)) % mod
    # print(ans)
    print(m)

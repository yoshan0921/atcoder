from collections import defaultdict


class UnionFind_v1:
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
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


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

    # Find root
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

    # Find the members of the group containing x
    def group_members(self, x):
        root = self.root(x)
        return [i for i in range(len(self.size)) if self.root(i) == root]


if __name__ == "__main__":
    n = 5
    uf = UnionFind_v2(n)
    uf.unite(1, 2)
    uf.unite(4, 1)
    uf.unite(0, 1)
    print(uf.root(2))
    print(uf.issame(1, 3))
    print(uf.group_size(1))
    print(uf.roots())
    print(uf.group_members(1))
    print(uf.group_members(3))

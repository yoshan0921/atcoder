"""
Depth First Search Template
"""
import io
import sys
import time

sys.setrecursionlimit(10**6)

# Q1: Answer how many "clumps of black squares" there are in this grid.
_INPUT1 = """\
8 8
..#.....
.###.##.
.###..#.
####....
.#..###.
.....###
....##.#
.....##.
"""

# Q2: Answer if you can reach the goal(g) from the start(s).
_INPUT2 = """\
4 4
...s
....
....
.g..
"""


sys.stdin = io.StringIO(_INPUT2)


def dfs_stack_for_coordinate(coodinate, h_start, w_start):
    """DFS stack version"""
   # You can change the definition based on your needs.
    # dhs = [-1, -1, 0, 1, 1, 1, 0, -1]
    # dws = [0, 1, 1, 1, 0, -1, -1, -1]
    dhs = [-1, 0, 1, 0]
    dws = [0, -1, 0, 1]

    stack = [(h_start, w_start)]
    visited = set()
    visited.add((h_start, w_start))

    while stack:
        h, w = stack.pop()
        for dh, dw in zip(dhs, dws):
            h_next, w_next = h + dh, w + dw
            # Check if the next coordinate is already visited.
            if (h_next, w_next) in visited:
                continue
            # Check if the next coordinate is out of the grid.
            if not (0 <= h_next < H and 0 <= w_next < W):
                continue
            # Adding another condition here will change the behavior of the algorithm.
            if coodinate[h_next][w_next] == "#":
                continue
            visited.add((h_next, w_next))
            stack.append((h_next, w_next))

    return visited


def dfs_recursive_for_coordinate(coodinate, h_start, w_start, visited: set = None):
    """DFS recursive version"""

    if visited is None:
        visited = set()

    # you can change the definition based on your needs.
    # dhs = [-1, -1, 0, 1, 1, 1, 0, -1]
    # dws = [0, 1, 1, 1, 0, -1, -1, -1]
    dhs = [-1, 0, 1, 0]
    dws = [0, -1, 0, 1]

    visited.add((h_start, w_start))
    for dh, dw in zip(dhs, dws):
        h_next, w_next = h_start + dh, w_start + dw
        # Check if the next coordinate is already visited.
        if (h_next, w_next) in visited:
            continue
        # Check if the next coordinate is out of the grid.
        if not (0 <= h_next < H and 0 <= w_next < W):
            continue
        # Adding another condition here will change the behavior of the algorithm.
        if coodinate[h_next][w_next] == "#":
            continue
        dfs_recursive_for_coordinate(coodinate, h_next, w_next, visited)

    return visited


if __name__ == "__main__":
    H, W = map(int, input().split())

    C = [list(input()) for i in range(H)]
    print(C)

# Q1
    # # Stack version
    # time_start = time.time()
    # visited = set()
    # count = 0

    # for i in range(H):
    #     for j in range(W):
    #         if C[i][j] == "#" and not (i, j) in visited:
    #             count += 1
    #             visited.update(dfs_stack_for_coordinate(C, i, j))
    # print(count)
    # print(f"processing time={time.time() - time_start:06.5f}")

    # # Recursive version
    # time_start = time.time()
    # visited = set()
    # count = 0

    # for i in range(H):
    #     for j in range(W):
    #         if C[i][j] == "#" and not (i, j) in visited:
    #             count += 1
    #             visited.update(dfs_recursive_for_coordinate(C, i, j))
    # print(count)
    # print(f"processing time={time.time() - time_start:06.5f}")

# Q2
    # Stack version
    time_start = time.time()
    visited = set()

    for i in range(H):
        for j in range(W):
            if C[i][j] == "s":
                sh, sw = i, j  # start
            elif C[i][j] == "g":
                gh, gw = i, j  # goal

    visited.update(dfs_stack_for_coordinate(C, sh, sw))
    print(visited)
    if (gh, gw) in visited:
        print("Yes")
    else:
        print("No")

    # Recursive version
    time_start = time.time()
    visited = set()

    for i in range(H):
        for j in range(W):
            if C[i][j] == "s":
                sh, sw = i, j  # start
            elif C[i][j] == "g":
                gh, gw = i, j  # goal

    visited.update(dfs_recursive_for_coordinate(C, sh, sw))
    print(visited)
    if (gh, gw) in visited:
        print("Yes")
    else:
        print("No")

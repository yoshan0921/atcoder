import io
import sys

_INPUT = """\
5
RLURU
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()
coordinate_visited = set()
coordinate_visited.add((0, 0))

coordinate_now = [0, 0]

for i in S:
    if i == "R":
        coordinate_now[0] += 1
    elif i == "L":
        coordinate_now[0] -= 1
    elif i == "U":
        coordinate_now[1] += 1
    elif i == "D":
        coordinate_now[1] -= 1

    if tuple(coordinate_now) in coordinate_visited:
        print("Yes")
        exit(0)

    coordinate_visited.add(tuple(coordinate_now))

# print(coordinate_visited)
# print(coordinate_now)
print("No")

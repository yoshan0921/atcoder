import io
import sys

_INPUT = """\
7
0
1
0
"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())


def binary_search(N):
    left = 1
    right = N
    while right - left > 1:
        mid = (left + right) // 2
        print("?", mid)
        ans = int(input())
        if ans == 1:
            right = mid
        elif ans == 0:
            left = mid
    return left


if __name__ == "__main__":
    ret = binary_search(N)
    print("!", ret)

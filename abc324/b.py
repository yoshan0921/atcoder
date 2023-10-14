import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**6)

_INPUT = """\
37748736
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())


def is_power_of_two_and_three(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    return n == 1


if is_power_of_two_and_three(N):
    print("Yes")
else:
    print("No")

# if is_power_of_two(N):
#     print("Yes")
# elif is_power_of_three(N):
#     print("Yes")
# else:
#     print("No")

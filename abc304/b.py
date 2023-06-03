import io
import sys
import math

_INPUT = """\
123
"""
sys.stdin = io.StringIO(_INPUT)

N = input()
intN = int(N)
digit = len(N)
# print(digit)

if digit < 4:
    print(intN)
elif digit == 4:
    print(math.floor(intN / 10) * 10)
elif digit == 5:
    print(math.floor(intN / 100) * 100)
elif digit == 6:
    print(math.floor(intN / 1000) * 1000)
elif digit == 7:
    print(math.floor(intN / 10000) * 10000)
elif digit == 8:
    print(math.floor(intN / 100000) * 100000)
elif digit == 9:
    print(math.floor(intN / 1000000) * 1000000)

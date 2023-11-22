import io
import sys
import itertools

_INPUT = """\
4
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
for bits in itertools.product(["(", ")"], repeat=N):
    sum = 0
    for b in bits:
        if b == "(":
            sum += 1
        else:
            sum -= 1

        if sum < 0:
            break

    if sum == 0:
        print("".join(bits))

import io
import sys

_INPUT = """\
G B
"""
sys.stdin = io.StringIO(_INPUT)

distance = {"A": 0, "B": 3, "C": 4, "D": 8, "E": 9, "F": 14, "G": 23}

p, q = input().split()
val_p = distance[p]
val_q = distance[q]

print(abs(val_p-val_q))

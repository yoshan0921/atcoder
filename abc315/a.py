import io
import sys

_INPUT = """\
aaaabbbbcccc
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
targer = ["a", "e", "i", "o", "u"]

# print(S)
# print(targer)

for i in S:
    if i in targer:
        S = S.replace(i, "")

print(S)

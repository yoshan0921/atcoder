import io
import sys

_INPUT = """\
FAC
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
T = set(["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"])

if S in T:
    print("Yes")
else:
    print("No")

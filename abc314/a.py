import io
import sys

_INPUT = """\
32
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
pi = list(str(1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679))
print("3." + "".join(pi[:N]))

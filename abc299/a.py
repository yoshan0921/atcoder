import io
import sys

_INPUT = """\
10
.|..|.*...
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = list(input())

flg1 = False
flg2 = False
for i in S:
    if i == "|" and flg1 == False:
        flg1 = True
        continue
    if i == "|" and flg1 == True:
        flg2 = True
        continue
    if i == "*":
        if (flg1 == True and flg2 == True) or (flg1 == False and flg2 == False):
            # print(flg1, flg2)
            print("out")
            break
        else:
            # print(flg1, flg2)
            print("in")
            break

import io
import sys

_INPUT = """\
30
-o-o-oooo-oo-o-ooooooo--oooo-o
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()

flg = False
flg_bar = False
count_new = 0
count_old = 0

for i in S:
    if i == "-":
        flg_bar = True

    if i == "o" and flg == False:
        flg = True
        count_new += 1
    elif i == "o" and flg == True:
        count_new += 1
    elif i == "-" and flg == True:
        flg = False
        if count_new > count_old:
            count_old = count_new
        count_new = 0

if count_new == 0 and count_old == 0:
    print(-1)
elif flg_bar == False:
    print(-1)
elif count_new > count_old:
    print(count_new)
else:
    print(count_old)

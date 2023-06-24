import io
import sys

_INPUT = """\
2
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        str = ""
        str = S[i] + S[j]

        if len(str) % 2 == 0:
            for k in range(len(str)//2):
                if str[k] != str[len(str)-1-k]:
                    break
            else:
                print("Yes")
                exit()
        elif len(str) % 2 != 0:
            for k in range(len(str)//2+1):
                if str[k] != str[len(str)-1-k]:
                    break
            else:
                print("Yes")
                exit()

print("No")

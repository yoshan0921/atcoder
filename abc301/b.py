import io
import sys

_INPUT = """\
4
2 5 1 2
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = list(map(int, input().split()))
Answer = list()

for i in range(len(S)):
    if i == len(S)-1:
        Answer.append(S[i])
    elif S[i] < S[i+1]:
        Answer.append(S[i])
        for j in range(S[i+1]-S[i]-1):
            Answer.append(S[i]+j+1)
    elif S[i] > S[i+1]:
        Answer.append(S[i])
        for j in range(S[i]-S[i+1]-1):
            Answer.append(S[i]-j-1)

for v in Answer:
    print(v, end=" ")

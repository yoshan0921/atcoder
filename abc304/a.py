import io
import sys

_INPUT = """\
5
alice 31
bob 41
carol 5
dave 92
ellen 65
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
Name = []
Age = []
for i in range(N):
    S, A = input().split()
    Name.append(S)
    Age.append(int(A))

# print(Name)
# print(Age)

min_index = Age.index(min(Age))
# print(min_index)

for j in range(min_index, len(Age)):
    print(Name[j])
for k in range(min_index):
    print(Name[k])

import numpy as np
n = int(input())
a_ = [list(map(int, input().split())) for i in range(n)]
b_ = [list(map(int, input().split())) for i in range(n)]
# np.ndarrayに変換
a = np.array(a_)
b = np.array(b_)
# 高々4回まで回転させたケースを試せばよい
for i in range(4):
    if np.min(b - a) >= 0:
        print("Yes")
        exit(0)
    # aを回転する
    a = np.rot90(a)
print("No")

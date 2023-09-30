"""
Binary Search Template
"""

import random


def binary_search(data: list, value: int):
    """
    リスト dataの中に値valueがあれば、その index を返す (複数ある場合はどれか 1 つを返す)
    リスト dataの中に値valueがなければ、-1 を返す
    """
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_v2(data: list, value: int):
    """
    left は「常に」条件を満たさない
    right は「常に」条件を満たす
    right - left = 1 になるまで範囲を狭める (最後は right が条件を満たす最小)
    """
    # 「index = 0」が条件を満たすこともあるので、初期値は -1
    left = -1
    # 「index = data.size()-1」が条件を満たさないこともあるので、
    # 初期値は data.size()
    right = len(data)

    # どんな二分探索でもここの書き方を変えずに使える
    while right - left > 1:
        mid = (left + right) // 2

        if data[mid] >= value:
            right = mid
        else:
            left = mid
    # left は条件を満たさない最大の値、right は条件を満たす最小の値になっている
    return right


def isOK(data: list, mid: int, value: int):
    """
    mid(index)が条件を満たすかどうか
    """
    if data[mid] >= value:
        return True
    else:
        return False


def binary_search_v3(data: list, value: int):
    """
    left は「常に」条件を満たさない
    right は「常に」条件を満たす
    right - left = 1 になるまで範囲を狭める (最後は right が条件を満たす最小)
    """
    # 「index = 0」が条件を満たすこともあるので、初期値は -1
    left = -1
    # 「index = data.size()-1」が条件を満たさないこともあるので、
    # 初期値は data.size()
    right = len(data)

    # どんな二分探索でもここの書き方を変えずに使える
    while right - left > 1:
        mid = (left + right) // 2

        if isOK(data, mid, value):
            right = mid
        else:
            left = mid
    # left は条件を満たさない最大の値、right は条件を満たす最小の値になっている
    return right


if __name__ == "__main__":
    print("Please input the number of data.")
    num_data = int(input())
    data = [random.randint(0, 10000) for i in range(num_data)]
    data.sort()
    print(data)

    # print("Please select on of the numbers.")
    # value = int(input())
    # result = binary_search(data, value)
    # print(result)

    print("Please select on of the numbers.")
    value = int(input())
    result = binary_search_v3(data, value)
    print(result)

"""
Binary Search Template
"""
import io
import sys
import time

sys.setrecursionlimit(10**6)

# Q1: Answer how many "clumps of black squares" there are in this grid.
_INPUT1 = """\
1 2 2 3 4 5 5 5 6 7 8 9
5
"""
sys.stdin = io.StringIO(_INPUT1)


def isOK(data: list, mid: int, value: int):
    """
    Check if mid(index) meed the condition.
    """
    return True if data[mid] >= value else False


def binary_search_v3(data: list, target: int):
    """
    left always doesn't meet the condition.
    right always meets the condition.
    Keep narrowing the range until right - left = 1 (right is the minimum that meets the condition)
    """
    # Starting value is -1 because 0 might meet the condition.
    left = -1
    # Starting value is data.size because data.size - 1 might not meet the condition.
    right = len(data)

    # You need to change only isOK function.
    while right - left > 1:
        mid = (left + right) // 2

        if isOK(data, mid, target):
            right = mid
        else:
            left = mid

    return right


if __name__ == "__main__":
    print("Please input the number of data.")
    data = sorted(list(map(int, input().split())))
    print(data)

    target = int(input())
    result = binary_search_v3(data, target)
    print(result)

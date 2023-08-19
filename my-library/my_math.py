"""
数学関連の関数をまとめたライブラリ
"""


# 素数一覧を出力する関数
def get_prime_list(limit):
    prime = []
    for i in range(2, limit):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime


# 素数がどうかを判定する関数
def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True


# 約数一覧を出力する関数
def get_divisors_list(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if i**2 == num:
                continue
            divisors.append(int(num/i))
    return sorted(divisors)


if __name__ == "__main__":
    ret1 = get_prime_list(80)
    ret2 = is_prime(20)
    ret3 = get_divisors_list(20)

    print(ret1)
    print(ret2)
    print(ret3)

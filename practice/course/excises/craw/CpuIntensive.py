import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from util.Util import timesum


PRIMIES = [112272535095293] * 100


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


@timesum
def single_thread():
    for number in PRIMIES:
        # print(is_prime(number))
        is_prime(number)


@timesum
def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMIES)  # 多线程甚至拖慢了速度


@timesum
def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMIES)  # 提升了 6 倍


if __name__ == '__main__':
    single_thread()
    multi_thread()
    multi_process()

"""
>>开始计时!
<<耗时 23.292997 s
>>开始计时!
<<耗时 23.495053 s
>>开始计时!
<<耗时 4.086435 s
"""

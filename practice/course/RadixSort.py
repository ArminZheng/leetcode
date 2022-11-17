"""基数排序
是队列的一个应用
"""

from basic.LinearDS.queue import Queue


def radix_sort(s: list) -> list:
    main = Queue()
    for n in s:
        main.enqueue(n)
    d = len(str(max(s)))
    dstr = "%%0%dd" % d  # 前导零的模版, e.g. "%05d"
    # 准备10个队列
    nums = [Queue() for _ in range(10)]

    pass


if __name__ == '__main__':
    print(int("1111_1111", 2))
    print(hex(int("11111111", 2)).upper())
    print(oct(int("11111111", 2)).upper())
    print(bin(int("11111111", 2)))
    """
    书写大数使用下划线将其中的数字分组,Python不会打印其中的下划线

    存储这种数时,Python会忽略其中的下划线
    将数字分组时,即使不是将每三位分成一组,也不会影响最终的值
    在Python看来,1000和1_000没有什么不同,1_000和10_00也没什么不同
    表示法适用于整数和浮点数,但只有Python3.6+支持
    """
    test = hex(int("1111_1111", 2))
    a = test[2:]
    b = len(a)
    print("hello: %s %d" % (a.upper(), b))

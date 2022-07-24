from timeit import Timer

# 性能测试

def test1(): # 循环连接 (cat)
    l = []
    for i in range(1000):
        l = l + [i]

def test2(): # append()函数
    l = []
    for i in range(1000):
        l.append(i)

def test3(): # 列表推导式
    l = [i for i in range(1000)]

def test4(): # range()函数转列表
    l = list(range(1000))

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")
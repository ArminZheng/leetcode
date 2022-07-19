import random
from timeit import Timer
import datetime

def v1():
    s = "zhangsan"
    r = "lisi and %s" % s
    print(r)

def v2():
    # print(random.randrange(100) is 98)
    # is checks for identity - if the two variables point to the exact same object.
    # == checks for equality - if the two variables point at values are equal. That is, if they will act the same way in the same situations.
    print(random.randrange(100) == 98)
    print(random.randrange(100) in [98])

def v3():
    i = [1,3,4]
    i = i + [2,5,6]
    # O(n + k)
    print(i)

def v4():
    n = 7 / 2
    print(n)
    print(type(n))
    a = 7
    b = 2
    c = a / b
    print("c is ", type(c), "a is ", type(a), "b is ", type(b))
    a //= b
    print(a , "a is ", type(a))

def test1():
    global lst # 作用域, 本来py解释器有一套机制去找, 但下面38行是通过源代码字符串调用, 找机制就发挥不了作用
    lst.pop(0)
def v5():
    global lst
    lst = list(range(1000000))
    t1 = Timer("test1()", "from __main__ import test1") # 命名空间
    print(f"{t1.timeit(number=1000):.3f} seconds")
v5()

def v6():
    f = open("pi50.4.bin", "rb")
    dbuff = f.read()
    s = ("".join((f"d:02x" for d in dbuff))).encode()
    d1 = datetime.date(2022, 1, 1)
    found = 0
    for n in round(365):
        day = ((d1 + datetime.timedelta(days = n)).strftime("%Y%m%d")).encode()
        if day in s:
            found += 1

def v7():
    f = lambda : print(999)
    print(f())
    # f()

def v8():
    s = input("please wake up! ")
    print(s)

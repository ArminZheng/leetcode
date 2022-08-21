from math import sqrt


def primeNumber():
    # n = int(input())
    n = 9
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            print(f"{n} is Not a prime number.")
            break
    else:
        print(f"{n} is a prime number.")

    # a = [[0]*5]*3
    a = [[0 for i in range(5)] for j in range(3)]
    print(a)  # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    print(len(a))
    for obj in a:
        print("11")
        obj.append(3)
    print(a)


# 时间包
from datetime import datetime


def time():
    now: datetime = datetime.now()
    print(now)
    print(type(now))
    stamp = now.timestamp()
    print(stamp)
    print(datetime.fromtimestamp(stamp))


# base64包
import base64


def base64():
    var = base64.b64encode(b'12abca')
    new_var = base64.b64decode(var)
    print(var, new_var)
    base64.b64decode(var)


# haslib 摘要算法包
import hashlib


def hashmd5():
    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())


def loop():
    def func(a, b):
        def foo(b, a):
            print(b, a)
        return foo(a, b)  # 先执行函数调用
    a = func(4, 7)
    print(a)


def loopback():
    def func(a, b):
        c = 1024

        def foo(b, d):
            print(b, d, c, a)  # b、d 是内部方法参数, c、a 是借外部的
        return foo(a, b)  # 先执行函数调用
    a = func(4, 7)
    print(a)


from collections import defaultdict


def myDict():
    dict1 = defaultdict(int)
    dict2 = defaultdict(set)
    dict3 = defaultdict(str)
    dict4 = defaultdict(list)
    dict5 = defaultdict(lambda: [])
    dict1[2] = 'two'

    print(dict1[1])
    print(dict2[1])
    print(dict3[1])
    print(dict4[1])
    print(dict5[1])

# myDict()


def matchCase():
    x: int = 19
    # match x:
    # case 1:
    # print("hello")
    # case 19:
    # print("leetcode")
    # case 20:
    # print("GG")


from typing import Any, List, Mapping


def testDefaultDict():
    groups = defaultdict(List)
    x = Mapping[int, int]
    print(groups["gg"])
    print(type(groups["gg"]))
    for key, value in groups.items():
        print(key, value)
    return x
# testDefaultDict()


def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    source = defaultdict(list)
    for i, size in enumerate(groupSizes):
        source[size].append(i)
    ans = []
    for key, value in source.items():
        ans.extend(value[i: i + key] for i in range(0, len(value), key))
    return ans


def testEnumerate():
    arrys = [1, 2, 3, 4, 5]
    e = enumerate(arrys)
    print(type(e))
    print(type(arrys))


def exception():
    try:
        1 / 0
    except Exception as e:
        print(e)


def args():
    s1 = set([1, 2, 3, 3, 4, 1])
    print(s1)

    def user(*args):
        print(type(args), args)  # 不定长参数 + 位置传递: 元祖类型

    user(1, 2, 3)

    def user(**args):
        print(type(args), args)  # 不定长参数 + 关键字传递: 字典<标识符>类型

    user(a=1, b=2, c=3)


# args()
from typing import Optional


def foo_func(a: Optional[int] = None):
    print(a)  # Optional 也就是给个提示作用, 代表可以为 None


def func01():  # 0x1011233a0
    print("func01 is show")


def foo(func):  # func = func01 = 0x1011233a0
    func()  # 0x1011233a0


def test169_173():
    func02 = func01
    print(func01)
    print(func02)
    func02()
    foo(func01)  # input 0x1011233a0


def normalFunc(num1):
    def closure(num2):
        nonlocal num1
        num = num1 + num2
        # num1 += 10
        num1 += 10
        print("now value", num)
    return closure


def testNormalFunc():
    closureFunc = normalFunc(10)
    closureFunc(1)
    closureFunc(2)
    closureFunc(2)
    closureFunc(2)
    closureFunc(2)


def debug(func):
    def wrapper():  # 装饰器的本质是闭包
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper


def say_hello():
    print("hello!")


def testSayHello():
    global say_hello
    say_hello = debug(say_hello)  # 使用装饰器装饰函数
    say_hello()


from time import time as ti


def getTime(fn):
    def inner(*args, **kwargs):
        print(">>开始计时!")
        start = ti()
        result = fn(*args, **kwargs)
        print("<<耗时 %f %s" % (ti() - start, "s"))
        return result
    return inner


@getTime
def testGetTime():
    for i in range(100000):
        print(i)
    return "success"


def logging(fn):
    def inner(a, b):  # 内部函数应该和被装饰的函数参数一样多
        fn(a, b)  # 外部函数入参函数也应该和被装饰的函数一致
    return inner


def log(fn):
    def inner(*args, **kwargs):
        print(f">>>函数开始执行: 参数为: {args}, {kwargs}")
        result = fn(*args, **kwargs)
        print(f"<<<函数执行结束, 结果为: {result}")
        return result
    return inner


@getTime  # 外
@log  # 里
def testLog(a, b):
    return a + b


def logOperation(flag, sums):
    def decorator(fn):
        def inner(num1, num2):
            if flag == "+":
                print("addition", sums)
            elif flag == "-":
                print("subtraction", sums)
            result = fn(num1, num2)
            return result
        return inner
    return decorator


@logOperation("+", "arithmetic")
def add(a, b):
    return a + b

class Check(object):
    """使用__call__方法
    """
    def __call__(self, *args, **kwds):
        print("I'm call method")

class CheckI:
    def __init__(self, fn) -> None:
        self.__fn = fn
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("登陆")
        self.__fn()

@CheckI
def comment():
    print("发表评论")

if __name__ == '__main__':
    # testNormalFunc()
    # testSayHello()
    # print(testGetTime())
    # result = testLog(b=1, a=2)
    # add(1, 3)
    # c = Check()
    # c()
    comment()
    
    print("运行结束!")
    pass

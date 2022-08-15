from math import sqrt
from nis import match

def primeNumber():
    # n = int(input())
    n = 9
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            print(f"{n} is Not a prime number.")
            break
    else:
        print(f"{n} is a prime number.")

    # a = [[0]*5]*3
    a = [[0 for i in range(5)] for j in range(3)]
    print(a)        #[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
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
    def func(a,b):
        def foo(b,a):
            print(b,a)
        return foo(a,b) #先执行函数调用
    a = func(4,7)
    print(a)

def loopback():
    def func(a, b):
        c = 1024
        def foo(b, d):
            print(b, d, c, a) # b、d 是内部方法参数, c、a 是借外部的
        return foo(a, b) # 先执行函数调用
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

from typing import List, Mapping

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
    arrys = [1,2,3,4,5]
    e = enumerate(arrys)
    print(type(e))
    print(type(arrys))

def exception():
    try:
        1/0
    except Exception as e:
        print(e)
    
    
def args():
    s1 = set([1,2,3,3,4,1])
    print(s1)

    def user(*args):
        print(type(args), args) # 不定长参数 + 位置传递: 元祖类型
        
    user(1, 2, 3)

    def user(**args):
        print(type(args), args) # 不定长参数 + 关键字传递: 字典<标识符>类型

    user(a = 1, b = 2, c = 3)

# args()
from typing import Optional
def foo_func(a: Optional[int] = None):
    print(a) # Optional 也就是给个提示作用, 代表可以为 None

foo_func()

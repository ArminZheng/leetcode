from basic.LinearDS.simpleDeque import Stack as S1
from basic.LinearDS.simpleStack import Stack as S2
from timeit import Timer


def test1():
    s = S1()
    s.isEmpty()
    s.push(4)
    S1.push(s, 5)
    s.push('dog')
    s.peek()
    s.push(True)
    s.size()
    s.isEmpty()
    s.push(8.4)
    s.pop()
    s.pop()
    s.size()


def test2():
    s = S2()
    s.isEmpty()
    s.push(4)
    S1.push(s, 5)
    s.push('dog')
    s.peek()
    s.push(True)
    s.size()
    s.isEmpty()
    s.push(8.4)
    s.pop()
    s.pop()
    s.size()


t1 = Timer("test1()", "from __main__ import test1")
print("one ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("two ", t2.timeit(number=1000), "milliseconds")

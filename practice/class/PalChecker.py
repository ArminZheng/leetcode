from basic.LinearDS.deque import Deque


def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        if chardeque.removeFront() != chardeque.removeRear():
            stillEqual = False

    return stillEqual

# 是否回文词 回文词
print(palchecker("lsdfkj"))  # False
print(palchecker("radar"))  # True
print(palchecker)  # <function palchecker at 0x1006084c0>
print(Deque)  # <class 'basic.LinearDS.deque.Deque'>
print(Deque())  # <basic.LinearDS.deque.Deque object at 0x1004f8070>

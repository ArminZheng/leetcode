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
print(palchecker("lsdfkj"))
print(palchecker("radar"))

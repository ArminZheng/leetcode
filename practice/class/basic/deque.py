

class Deque:
    """双端队列

    应用: 回文词的判定, radar madam toot

    时间复杂度
    addFront/removeFront O(1)
    addRear/removeRear O(n)
    """

    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

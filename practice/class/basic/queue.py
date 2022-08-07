class Queue:
    """队列
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        """入队

        Args:
            item (any): 入队元素
        """
        self.items.insert(0, item)

    def dequeue(self):
        """出队
        """
        return self.items.pop()

    def size(self):
        return len(self.items)

class Queue:
    """队列
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        """_summary_

        Parameters
        ----------
        item : _type_
            _description_
        """
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

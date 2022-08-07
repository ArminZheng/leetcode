class Stack:
    """栈 (栈顶尾端版)
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """
        If the list is empty, return True. Otherwise, return False.
        :return: The function isEmpty() returns a boolean value.
        """
        return self.items == []

    def push(self, item):
        """
        Add an item to the end of the list.
        
        @param item The item to be pushed onto the stack.
        """
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

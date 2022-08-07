# 极简懒人 class Stack
class Stack(list):
    push = list.append
    peek = lambda self: self[-1]
    isEmpty = lambda self: len(self) == 0
    size = list.__len__

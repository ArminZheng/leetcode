class Queue(list):
    """简易版队列

    Args:
        list (list): 继承列表
    """
    isEmpty = lambda self: len(self) == 0
    enqueue = list.append
    dequeue = lambda l: l.pop(0)
    size = list.__len__

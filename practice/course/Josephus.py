# from basic.LinearDS.queue import Queue

class Queue(list):
    def isEmpty(self): return len(self) == 0
    enqueue = list.append
    def dequeue(l): return l.pop(0)
    size = list.__len__


def hotPotato(nameList, m):  # 约瑟夫环: Josephus problem
    simqueue = Queue()
    for name in nameList:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(m):
            simqueue.enqueue(simqueue.dequeue())
        print(simqueue.dequeue())
    return simqueue.dequeue()


print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))

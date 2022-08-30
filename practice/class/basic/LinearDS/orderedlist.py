"""有序表 OrderedList
链表实现的算法分析:(头插法)
- 相关方法是否需要遍历(强相关)
- 对于一个包含节点数为n的链表
1. isEmpty O(1) 只需检查head是否为None
2. size O(n) 除了便利到表尾没有其他方法
3. search/remove O(n)
4. 无序表 add O(1)
5. 有序表 add O(n)
"""

__all__ = ["OrderedList", "add", "remove",
           "search", "isEmpty", "size", "index", "pop"]


class Node:
    def __init__(self, initdata) -> None:
        self.__data = initdata
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, data):
        self.__next = data

    def __eq__(self, __o: object) -> bool:
        return True if type(__o) == type(self) and __o.data == self.data else False


class OrderedList:
    def __init__(self) -> None:
        self.head: Node = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):  # head -> 1 -> 10 -> 30 -> 110
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            # 小数直接停止
            if current.data > item:
                stop = True
            else:
                previous = current
                current = current.next
        # 原始加入
        temp = Node(item)
        # 加在首部. 如果循环立即就停了, previous 就为空
        if previous == None:
            temp.next = self.head  # 注意顺序, self.head 是一个别名. 如果先覆盖就遗失原来代表的Node
            self.head = temp
        # 放在表中. 放在大于的 item 的 previous 之后
        else:
            temp.next = current
            previous.next = temp

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next  # 后移
        if previous == None:
            self.head = current.next
        else:
            previous.next(current.next)  # 替换

    def size(self):
        current: Node = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current: Node = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.data == item:
                found = True
            else:
                if current.data > item:
                    stop = True
                else:
                    current = current.next
        return found

    def pop(self):
        result = self.head.data
        self.remove(result)
        return result


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    str1 = 'harry poter'
    print(node1 == node2)
    print(node1 != node2)
    print(node1 != str1)

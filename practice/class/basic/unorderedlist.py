"""无序列表
数据项只按照存放位置来索引 (相反: 按照物理上 相对位置 存放的数据集: 列表)

例子: 
    <ul>
        <li></li>
    </ul>
    <ol>
        <li></li>
    </ol>
    <dl>
        <dt>
            <dd></dd>
        </dt>
    </dl>

特点: 只有位置的索引

链表实现: 
    - 数据项项的存放位置并没有规则, 但如果在数据项之间建立链接指向, 就可以保持前后相对位置
    - 两个标记: 队首、队尾
    - 最基本元素是节点Node
        - 数据项本身
        - 引用 (next == None 代表没有下一个节点)

notes: 
    抽象设计时做一些假设, 能避免让例外处理来分散我们对于数据结构的实现的注意力
    而把注意力集中在它的本质, 具体实现逻辑上
"""
__all__ = ['Node', 'UnorderedList', 'add', 'remove', 'search',
           'isEmpty', 'size', 'append', 'index', 'insert', 'pop']


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


class UnorderedList:
    def __init__(self) -> None:
        self.head: Node = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

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
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def pop(self):
        result = self.head.data
        self.remove(result)
        return result

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


if __name__ == '__main__':
    temp = Node(11)
    print(temp.data)
    ul = UnorderedList()
    ul.add(2)
    ul.add(3)
    ul.add(4)
    ul.add(5)
    print(ul.search(3))  # True
    print(ul.search(1))  # False
    print(ul.pop())  # 5
    print(ul.search(5))  # False

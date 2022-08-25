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
__all__ = ['add', 'remove', 'search', 'isEmpty',
           'size', 'append', 'index', 'insert', 'pop' , 'Node', 'UnorderedList']


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


if __name__ == '__main__':
    temp = Node(11)
    print(temp.data)

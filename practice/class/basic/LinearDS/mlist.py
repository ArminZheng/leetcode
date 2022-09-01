"""多重链表
"""


class StudentMListNode(object):
    def __init__(self, data) -> None:
        self.data = data  # id name address zip
        self.nextById = None
        self.nextByName = None
        pass

# 二叉链表 == 二叉树

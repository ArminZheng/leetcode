#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit = tortoise = head
        while rabbit and rabbit.next:
            # rabbit = rabbit.next.next
            # tortoise = tortoise.next
            # 可以精简
            rabbit, tortoise = rabbit.next.next, tortoise.next
            if rabbit is tortoise:
                return True
        return False
# @lc code=end


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = a
    print(Solution().hasCycle(a))

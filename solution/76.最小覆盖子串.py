#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import defaultdict
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = defaultdict(int)
        window = defaultdict(int)
        for c in t:
            need[c] += 1

        left, right, valid = 0, 0, 0
        start, lenght = 0, sys.maxsize

        while right < len(s):
            c = s[right]  # c 是即将移入窗口的字符
            right += 1  # 右移窗口
            # ... 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while valid == len(need):
                if right - left < lenght:
                    start = left
                    lenght = right - left
                d = s[left]  # d 是即将移出窗口的字符
                left += 1  # 左移窗口
                # ... 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if lenght == sys.maxsize else s[start:start+lenght]
# @lc code=end

'''
window: [0, 1)
window: [0, 2)
window: [0, 3)
window: [0, 4)
window: [0, 5)
window: [0, 6)
window: [1, 7)
window: [1, 8)
window: [1, 9)
window: [1, 10)
window: [1, 11)
window: [6, 12)
window: [6, 13)
BANC
'''

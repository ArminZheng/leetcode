#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
from collections import defaultdict
import sys


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        NEED, window = defaultdict(int), defaultdict(int)
        for item in t:
            NEED[item] += 1

        left, right = 0, 0
        valid, point = 0, 0
        lenght = sys.maxsize

        while right < len(s):
            c = s[right]
            right += 1
            if c in NEED:
                window[c] += 1
                if window[c] == NEED[c]:
                    valid += 1

            while valid == len(NEED):
                if right - left < lenght:
                    point = left
                    lenght = right - left

                d = s[left]
                left += 1
                if d in NEED:
                    if window[d] == NEED[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if lenght == sys.maxsize else s[point:point+lenght]
# @lc code=end

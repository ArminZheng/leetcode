#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
from collections import defaultdict


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        NEED, window = defaultdict(int), defaultdict(int)
        valid = 0
        for item in s1:
            NEED[item] += 1

        left, right = 0, 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in NEED:
                window[c] += 1
                if window[c] == NEED[c]:
                    valid += 1

            while right - left >= len(s1):  # >
                if valid == len(NEED):  # len(s1)
                    return True

                d = s2[left]
                left += 1
                if d in NEED:
                    if window[d] == NEED[d]:
                        valid -= 1
                    window[d] -= 1
        return False
# @lc code=end

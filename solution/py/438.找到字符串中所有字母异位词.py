#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        NEED, window = defaultdict(int), defaultdict(int)
        for item in p:
            NEED[item] += 1
        left, right = 0, 0
        valid = 0
        res = list()
        while right < len(s):
            c = s[right]
            right += 1
            if c in NEED:
                window[c] += 1
                if window[c] == NEED[c]:
                    valid += 1

            while right - left >= len(p):
                if valid == len(NEED):
                    res.append(left)

                d = s[left]
                left += 1
                if d in NEED:
                    if window[d] == NEED[d]:
                        valid -= 1
                    window[d] -= 1
        return res
# @lc code=end

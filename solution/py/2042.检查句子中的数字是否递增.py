#
# @lc app=leetcode.cn id=2042 lang=python3
#
# [2042] 检查句子中的数字是否递增
#

# @lc code=start
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        pre, i = 0, 0
        while i < len(s):
            if s[i].isdigit():
                cur = 0
                while i < len(s) and s[i].isdigit():
                    cur = 10 * cur + int(s[i])
                    i += 1
                if cur <= pre:
                    return False
                pre = cur
            else:
                i += 1
        return True
# @lc code=end

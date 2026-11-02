#
# @lc app=leetcode.cn id=2027 lang=python3
#
# [2027] 转换字符串的最少操作次数
#

# @lc code=start
class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = i = 0
        while i < len(s):
            if s[i] == 'X':
                ans += 1
                i += 3
                continue
            i += 1
        return ans
# @lc code=end

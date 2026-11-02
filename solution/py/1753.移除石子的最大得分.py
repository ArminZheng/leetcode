#
# @lc app=leetcode.cn id=1753 lang=python3
#
# [1753] 移除石子的最大得分
#

# @lc code=start
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        m = max(a, b, c)
        ab = a + b + c - m
        if m > ab:
            return ab
        else:
            return (a + b + c) // 2
# @lc code=end

if __name__ == '__main__':
    print(Solution().maximumScore(4, 4, 6))
    print(bool(-1))


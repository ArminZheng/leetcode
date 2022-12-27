#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # sum = 0
        # while n:
        #     n = n & (n-1)
        #     sum += 1
        # return sum
        n = n - ((n >> 1) & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        n = (n + (n >> 4)) & 0x0f0f0f0f
        n = n + (n >> 8)
        n = n + (n >> 16)
        return n & 0x3f

# @lc code=end

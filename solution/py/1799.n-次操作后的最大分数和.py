#
# @lc app=leetcode.cn id=1799 lang=python3
#
# [1799] N 次操作后的最大分数和
#

# @lc code=start
from math import gcd
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m = len(nums)
        g = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                g[i][j] = gcd(nums[i], nums[j])
        f = [0] * (1 << m)
        for k in range(1 << m):
            if (cnt := k.bit_count()) % 2 == 0:
                for i in range(m):
                    if k >> i & 1:
                        for j in range(i + 1, m):
                            if k >> j & 1:
                                f[k] = max(f[k], f[k ^ (1 << i) ^ (1 << j)] + cnt // 2 * g[i][j])
        return f[-1]
    
    def gcd(self, num1: int, num2: int):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1 # num1 = num2
        
# @lc code=end

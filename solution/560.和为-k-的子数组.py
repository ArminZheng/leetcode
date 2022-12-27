#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = defaultdict(int)
        preSum[0] = 1

        ans, sum0_i = 0, 0
        for i in range(n):
            sum0_i += nums[i]
            sum0_j = sum0_i - k
            if sum0_j in preSum:
                ans += preSum[sum0_j]
            preSum[sum0_i] += 1
        return ans
        
    
    # Time Limit Exceeded
    def subarraySumTLE(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum = [0] * (n + 1)
        for i in range(n):
            sum[i+1] = sum[i] + nums[i]
        
        ans = 0
        for i in range(1, n + 1):
            for j in range(i):
                if sum[i] - sum[j] == k:
                    ans += 1
        return ans
# @lc code=end


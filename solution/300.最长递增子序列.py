#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
from ast import List
from turtle import right


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        top = [0] * len(nums)
        piles = 0
        for i in range(len(nums)):
            poker = nums[i]

            l, r = 0, piles
            while l < r:
                mid = (l + r) // 2
                if top[mid] > poker:
                    r = mid
                elif top[mid] < poker:
                    l = mid + 1
                else:
                    r = mid
            if l == piles:
                piles += 1
            top[l] = poker
        return piles

    def lengthOfLIS2(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# @lc code=end

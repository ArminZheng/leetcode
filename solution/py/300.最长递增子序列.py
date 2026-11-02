#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
from typing import List


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        top, piles = [0] * len(nums), 0
        for num in nums:
            left, right = 0, piles
            # piles 会大于实际右边界
            while left < right:
                mid = (left + right) // 2
                if top[mid] > num:
                    right = mid
                elif top[mid] < num:
                    left = mid + 1
                elif top[mid] == num:
                    right = mid
                ## 会因为left == right终结, 所以并不是精准搜索
            # 搜索到右边的极限后增加堆
            if left == piles:
                piles += 1
            # 左侧堆放入当前数字
            top[left] = num
        return piles

    def lengthOfLIS2(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                # 从前面找出比当前小的数组位置
                if nums[i] > nums[j]:
                    # 找出前面候选中最大的 (最小为1)
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# @lc code=end

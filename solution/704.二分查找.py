#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
from typing import List


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            if nums[mid] > target:
                right = mid
            if nums[mid] < target:
                left = mid + 1
        return left - 1 if left <= len(nums) and nums[left - 1] == target else -1
# @lc code=end

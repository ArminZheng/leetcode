#
# @lc app=leetcode.cn id=2012 lang=python3
#
# [2012] 数组美丽值求和
#

# @lc code=start
from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        l_max = nums[0]
        r_min = []
        temp_min = 10**5 + 1
        
        # 从 last 至 2
        for i in range(n-1, 1, -1):
            temp_min = min(nums[i], temp_min)
            # r_min[i-1] = temp_min
            r_min.append(temp_min)

        ans = 0
        for i in range(1, n-1):
            r = r_min.pop()
            if nums[i-1] < nums[i] < nums[i+1]:
                ans += 1
                # if l_max < nums[i] < r_min[i]:
                if l_max < nums[i] < r:
                    ans += 1
            # 更新左边最大值
            l_max = max(nums[i], l_max)

        return ans
# @lc code=end

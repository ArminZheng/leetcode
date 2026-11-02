#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#
from typing import List

# @lc code=start


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        c, m = 1, 1
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                c += 1
                if c > m:
                    m = c
            else:
                c = 1
        return m
# @lc code=end

if __name__ == '__main__':
    print(Solution().findLengthOfLCIS([1,3,5,4,7]))

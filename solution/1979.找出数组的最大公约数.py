#
# @lc app=leetcode.cn id=1979 lang=python3
#
# [1979] 找出数组的最大公约数
#

# @lc code=start
from typing import List


class Solution:
    # Greatest Common Divisor
    def findGCD(self, nums: List[int]) -> int:
        mx, mn = max(nums), min(nums)
        # 1997 ÷ 615 = 3 (a ÷ b = c)
        for i in range(1, mn):
            # 除数和余数反复做除法运算，当余数为 0 时，取当前算式除数b为最大公约数
            # gcd(a,b) = gcd(b,a mod b)
            ##    a % b = r
            ## 置 a←b, b←r
        #     mx, mn = mn, mx % mn
        # return mx
            r = mn // i
            if not mn % r and not mx % r:
                return r
        return 1 # return a
# @lc code=end

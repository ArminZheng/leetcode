#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#

# @lc code=start


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """
        高楼扔鸡蛋、编辑距离详解、最长回文子序列
        """
        memo = {}

        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    l, h = 1, n
                    while l + 1 < h:
                        x = (l + h) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)

                        if t1 < t2:
                            l = x
                        elif t1 > t2:
                            h = x
                        else:
                            l = h = x
                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))
                                  for x in (l, h))
                memo[k, n] = ans
            return memo[k, n]
        return dp(k, n)
# @lc code=end

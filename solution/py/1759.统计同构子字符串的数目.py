#
# @lc app=leetcode.cn id=1759 lang=python3
#
# [1759] 统计同构子字符串的数目
#

# @lc code=start
class Solution:
    def countHomogenous(self, s: str) -> int:
        # 连续字符数 aabbbc [2, 3, 1]
        ans = []
        cur = 1
        let = s[0]
        for i in range(1, len(s)):
            if s[i] != let:
                ans.append(cur)
                cur = 1
                let = s[i]
            else:
                cur += 1
        ans.append(cur)
        return sum(i * (i+1)//2 for i in ans) % (10**9+7)

# @lc code=end


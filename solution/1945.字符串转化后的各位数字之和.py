#
# @lc app=leetcode.cn id=1945 lang=python3
#
# [1945] 字符串转化后的各位数字之和
#

# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result = "".join(str(ord(item) - ord('a') + 1) for item in s)
        
        for _ in range(k):
            if len(result) <= 1:
                break
            total = sum(int(ch) for ch in result)
            result = str(total)
        return int(result)
# @lc code=end


if __name__ == '__main__':
    Solution().getLucky("abc", 1)

"""
longestPalindrome1
最长回文子串
"""

def longestPalindrome1(s: str) -> str:
    """动态规划"""
    n = len(s)
    if n < 2:
        return s

    max_lens, begin = 1, 0
    dp = [[False] * n for _ in range(n)]
    # for i in range(n):
    #     dp[i][i] = True

    for L in range(2, n + 1):
        for i in range(n):
            j = L + i - 1 # 右边界
            if j >= n:
                break
            if s[i] != s[j]:
                dp[i][j] = False
            else:
                # 0 1 2 (len=3 and s[i]==s[j])
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            if dp[i][j] and (j-i+1) > max_lens:  # num vs length
                # mark
                max_lens = j - i + 1
                begin = i
    # print(dp)
    return s[begin:begin + max_lens]


def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left+1, right-1


def longestPalindrome2(s: str) -> str:
    """中心扩散"""
    start, end = 0, 0
    for i in range(len(s)):
        left1, right1 = expandAroundCenter(s, i, i)
        left2, right2 = expandAroundCenter(s, i, i + 1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    return s[start: end+1]


def longestPalindrome3(s: str) -> str:
    """奇偶处理+中心扩散"""
    s = '#' + '#'.join(list(s)) + '#'
    start, end = 0, 0
    for i in range(len(s)):
        left1, right1 = expandAroundCenter(s, i, i)
        if right1 - left1 > end - start:
            start, end = left1, right1
    return s[start+1: end+1:2]


def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return (right - left - 2) // 2  # 多走了一步, 需要回退, then 返回半径


def longestPalindrome4(s: str) -> str:
    """Manacher算法"""
    start, end = 0, -1
    s = '#' + '#'.join(list(s)) + '#'
    arm_len = []
    right = -1
    j = -1
    for i in range(len(s)):
        if right >= i:
            # 镜像点
            mirror = 2 * j - i
            min_arm_len = min(arm_len[mirror], right - i)
            cur_arm_len = expand(s, i-min_arm_len, i+min_arm_len)
        else:
            cur_arm_len = expand(s, i, i)
        arm_len.append(cur_arm_len)
        if i + cur_arm_len > right:
            j = i
            right = i + cur_arm_len
        if 2 * cur_arm_len + 1 > end - start:
            start = i - cur_arm_len
            end = i + cur_arm_len
    return s[start+1:end+1:2]


if __name__ == '__main__':
    # print(longestPalindrome1("ebabababe"))
    # print(longestPalindrome2("ebabababe"))
    # print(longestPalindrome3("babad"))
    # print(longestPalindrome4("ebabababe"))
    for i in range(40):
        print(i & 1)


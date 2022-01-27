/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
class Solution {

  public int lengthOfLongestSubstring(String s) {
    int[] last = new int[]{-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};

    int res = 0;
    int start = 0;
    // 窗口开始位置
    for (int i = 0; i < s.length(); i++) {
      int index = s.charAt(i);
      // System.out.println("current Index = "+index);
      start = Math.max(start, last[index] + 1);
      // System.out.println("start = " +start);
      res = Math.max(res, i - start + 1);
      // System.out.println("ret = " +res);
      last[index] = i;
    }

    return res;
  }
  //   // 滑动窗口
  //   int pre = 0, post = 0, max = 0;
  //   Set<Character> set = new HashSet<>();

  //   while (post < s.length()) {
  //     if (!set.contains(s.charAt(post))) {
  //       set.add(s.charAt(post++));
  //       max = Math.max(max, set.size());
  //     } else {

  //       set.remove(s.charAt(pre++));
  //     }
  //   }
  //   return max;
  // }
}
// @lc code=end

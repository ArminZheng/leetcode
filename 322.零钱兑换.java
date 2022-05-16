/*
 * @lc app=leetcode.cn id=322 lang=java
 *
 * [322] 零钱兑换
 */
import java.util.Arrays;

// @lc code=start
class Solution {

  int[] dp;

  public int coinChange(int[] coins, int amount) {
    dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;
    for (int cash = 1; cash < dp.length; cash++) {
      for (int coin : coins) {
        if (cash < coin) continue;
        dp[cash] = Math.min(dp[cash], dp[cash - coin] + 1); // 复用
      }
    }
    return dp[amount] == amount + 1 ? -1 : dp[amount];
  }

  public static void main(String[] args) {
    int[] a = new int[] { 1, 2, 5 };
    Solution s = new Solution();
    int result = s.coinChange(a, 11);
    System.out.println("result = " + result);
  }
}
// @lc code=end

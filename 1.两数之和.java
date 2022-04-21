/*
 * @lc app=leetcode.cn id=1 lang=java
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {

  public int[] twoSum(int[] numbers, int target) {
    Map<Integer, Integer> hash = new HashMap<>();
    for (int i = 0; i < numbers.length; i++) {
      Integer diff = (Integer) (target - numbers[i]);
      if (hash.containsKey(diff)) {
        int toReturn[] = { hash.get(diff), i };
        return toReturn;
      }
      hash.put(numbers[i], i);
    }
    return new int[] {};
  }
}
// @lc code=end

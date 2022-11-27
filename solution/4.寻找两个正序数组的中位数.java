/*
 * @lc app=leetcode.cn id=4 lang=java
 *
 * [4] 寻找两个正序数组的中位数
 */

// @lc code=start
class Solution {

  /**
   * Find the median by traversing.
   * Time complexity: O(m+n).
   * Although the running time is similar,
   * it is worse than the required O(log (m+n)).
   * Space complexity: O(1).
   * @param nums1 the first sorted arrays
   * @param nums2 the second sorted arrays
   * @return the median of the two sorted arrays
   */
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int index1 = 0;
    int index2 = 0;
    int med1 = 0;
    int med2 = 0;
    for (int i = 0; i <= (nums1.length + nums2.length) / 2; i++) {
      med1 = med2;
      if (index1 == nums1.length) {
        med2 = nums2[index2];
        index2++;
      } else if (index2 == nums2.length) {
        med2 = nums1[index1];
        index1++;
      } else if (nums1[index1] < nums2[index2]) {
        med2 = nums1[index1];
        index1++;
      } else {
        med2 = nums2[index2];
        index2++;
      }
    }

    // the median is the average of two numbers
    if ((nums1.length + nums2.length) % 2 == 0) {
      return (float) (med1 + med2) / 2;
    }

    return med2;
  }
}
// @lc code=end

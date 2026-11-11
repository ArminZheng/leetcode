/*
 * @lc app=leetcode id=4 lang=java
 *
 * [4] Median of Two Sorted Arrays
 *
 * https://leetcode.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (47.93%)
 * Likes:    32987
 * Dislikes: 3642
 * Total Accepted:    4.7M
 * Total Submissions: 9.8M
 * Testcase Example:  '[1,3]\n[2]'
 *
 * Given two sorted arrays nums1 and nums2 of size m and n respectively, return
 * the median of the two sorted arrays.
 * 
 * The overall run time complexity should be O(log (m+n)).
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums1 = [1,3], nums2 = [2]
 * Output: 2.00000
 * Explanation: merged array = [1,2,3] and median is 2.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums1 = [1,2], nums2 = [3,4]
 * Output: 2.50000
 * Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -10^6 <= nums1[i], nums2[i] <= 10^6
 * 
 * 
 */

// @lc code=start
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // 保证 nums1 是较短的数组，对它做二分，复杂度 O(log(min(m,n)))
        if (nums1.length > nums2.length) {
            int[] tmp = nums1; nums1 = nums2; nums2 = tmp;
        }
        int m = nums1.length, n = nums2.length;
        // 左半部分元素总数：(m+n+1)/2，这样总数为奇数时中位数落在左半边
        int halfLen = (m + n + 1) / 2;

        int lo = 0, hi = m; // nums1 的切分点 i 取值范围 [0, m]
        while (lo <= hi) {
            int i = (lo + hi) / 2;       // nums1 左边取 i 个
            int j = halfLen - i;          // nums2 左边取 j 个，保证左半边总数为 halfLen

            // 用 ±∞ 处理边界（i=0 / i=m / j=0 / j=n 的情况）
            int nums1Left  = (i == 0) ? Integer.MIN_VALUE : nums1[i - 1];
            int nums1Right = (i == m) ? Integer.MAX_VALUE : nums1[i];
            int nums2Left  = (j == 0) ? Integer.MIN_VALUE : nums2[j - 1];
            int nums2Right = (j == n) ? Integer.MAX_VALUE : nums2[j];

            if (nums1Left <= nums2Right && nums2Left <= nums1Right) {
                // 找到正确切分
                if (((m + n) & 1) == 1) {
                    // 奇数：中位数是左半边最大值
                    return Math.max(nums1Left, nums2Left);
                } else {
                    // 偶数：中位数是左半边最大值与右半边最小值的平均
                    return (Math.max(nums1Left, nums2Left)
                            + Math.min(nums1Right, nums2Right)) / 2.0;
                }
            } else if (nums1Left > nums2Right) {
                // nums1 切多了，i 要往左移
                hi = i - 1;
            } else {
                // nums2Left > nums1Right，nums1 切少了，i 要往右移
                lo = i + 1;
            }
        }
        // 理论上不会走到这里
        return 0.0;
    }
}
// @lc code=end


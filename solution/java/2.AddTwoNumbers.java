/*
 * @lc app=leetcode id=2 lang=java
 *
 * [2] Add Two Numbers
 *
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (49.62%)
 * Likes:    37832
 * Dislikes: 7376
 * Total Accepted:    7.7M
 * Total Submissions: 15.5M
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order, and each of their nodes
 * contains a single digit. Add the two numbers and return the sum as a linked
 * list.
 *
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 *
 *
 * Example 1:
 *
 *
 * Input: l1 = [2,4,3], l2 = [5,6,4]
 * Output: [7,0,8]
 * Explanation: 342 + 465 = 807.
 *
 *
 * Example 2:
 *
 *
 * Input: l1 = [0], l2 = [0]
 * Output: [0]
 *
 *
 * Example 3:
 *
 *
 * Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
 * Output: [8,9,9,9,0,0,0,1]
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in each linked list is in the range [1, 100].
 * 0 <= Node.val <= 9
 * It is guaranteed that the list represents a number that does not have
 * leading zeros.
 *
 *
 */

// @lc code=start
/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode next; ListNode() {}
 * ListNode(int val) { this.val = val; } ListNode(int val, ListNode next) { this.val = val;
 * this.next = next; } }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        var result = new ListNode();
        boolean overflow = false;
        var a1 = l1 != null ? l1.val : 0;
        var a2 = l2 != null ? l2.val : 0;
        var sum = a1 + a2;
        var val = sum % 10;
        overflow = (sum / 10) != 0;
        result.val = val;
        var head = result;
        l1 = l1 != null ? l1.next : null;
        l2 = l2 != null ? l2.next : null;
        for (; l1 != null || l2 != null; ) {
            var c1 = l1 != null ? l1.val : 0;
            var c2 = l2 != null ? l2.val : 0;
            sum = c1 + c2;
            if (overflow) sum++;
            val = sum % 10;
            overflow = (sum / 10) != 0;
            var node = new ListNode(val);
            result.next = node;
            result = result.next;
            l1 = l1 != null ? l1.next : null;
            l2 = l2 != null ? l2.next : null;
        }
        if (overflow) {
            var node = new ListNode(1);
            result.next = node;
        }
        return head;
    }
}
// @lc code=end

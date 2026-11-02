package solution

import "sort"

/*
 * @lc app=leetcode.cn id=15 lang=golang
 *
 * [15] 三数之和
 */

// @lc code=start
func threeSum(nums []int) [][]int {
	var result [][]int
	sort.Ints(nums) // quick fix: cmd + .
	for i := 0; i < len(nums)-2; i++ {
		if i >= 1 && nums[i] == nums[i-1] {
			continue
		}
		second, third := i+1, len(nums)-1
		for second < third {
			sum := nums[i] + nums[second] + nums[third]
			if sum == 0 {
				result = append(result, []int{nums[i], nums[second], nums[third]})
				second++
				third--
				for second < third && nums[second] == nums[second-1] {
					second++
				}
				for second < third && nums[third] == nums[third+1] {
					third--
				}
			} else if sum > 0 {
				third--
			} else {
				second++
			}
		}
	}
	return result
}

// @lc code=end

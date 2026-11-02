package solution

import "sort"

/*
 * @lc app=leetcode.cn id=16 lang=golang
 *
 * [16] 最接近的三数之和
 */

// @lc code=start
func threeSumClosest(nums []int, target int) int {
	var closest int = 1 << 31
	sort.Ints(nums)
	for first := 0; first < len(nums)-2; first++ {
		second, third := first+1, len(nums)-1
		for second < third {
			diff := target - nums[first] - nums[second] - nums[third]
			if diff == 0 {
				return target
			}
			if abs(closest) > abs(diff) {
				closest = diff
			}
			if diff > 0 { 
				// diff > 0 (i.e. target > sum)  means sum is smaller
				second++
			} else {
				third--
			}
		}
	}
	return target - closest
}

func abs(i int) int {
	if i < 0 {
		return -i
	}
	return i
}

// @lc code=end

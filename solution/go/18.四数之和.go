package solution

import "sort"

/*
 * @lc app=leetcode.cn id=18 lang=golang
 *
 * [18] 四数之和
 */

// @lc code=start
func fourSum(nums []int, target int) [][]int {
	sort.Ints(nums)
	var res [][]int
	for i := 0; i < len(nums)-3; i++ {
		if i != 0 && nums[i] == nums[i-1] {
			continue
		}
		threeSumAddtion(&res, nums[i], nums[i+1:], target-nums[i])
	}
	return res
}

func threeSumAddtion(res *[][]int, first int, nums []int, target int) {
	sort.Ints(nums) // quick fix: cmd + .
	for i := 0; i < len(nums)-2; i++ {
		if i >= 1 && nums[i] == nums[i-1] {
			continue
		}
		second, third := i+1, len(nums)-1
		for second < third {
			sum := nums[i] + nums[second] + nums[third]
			if sum == target {
				*res = append(*res, []int{first, nums[i], nums[second], nums[third]})
				second++
				third--
				for second < third && nums[second] == nums[second-1] {
					second++
				}
				for second < third && nums[third] == nums[third+1] {
					third--
				}
			} else if sum > target {
				third--
			} else {
				second++
			}
		}
	}
}

// @lc code=end

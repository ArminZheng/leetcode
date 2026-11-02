package solution

/*
 * @lc app=leetcode.cn id=11 lang=golang
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
func maxArea(height []int) int {

	max, start, end := 0, 0, len(height)-1
	for start < end {
		width := end - start // 宽度固定
		high := 0            // 高度需要再次确定
		if height[start] < height[end] {
			high = height[start]
			start++
		} else {
			high = height[end]
			end--
		}

		temp := width * high
		if temp > max {
			max = temp // 有更大的值就替换
		}
	}
	return max
}

// @lc code=end

package solution

/*
 * @lc app=leetcode.cn id=1190 lang=golang
 *
 * [1190] 反转每对括号间的子串
 */

// @lc code=start
func reverseParentheses(s string) string {
	var stack [][]byte
	var top []byte
	stack = append(stack, []byte{}) // Initial segment in case we have any before the first parentheses
	for i := 0; i < len(s); i++ {
		if s[i] == '(' { // start the next segment
			stack = append(stack, []byte{})
		} else if s[i] == ')' { // end of a segment; pop it, reverse it, and append it to the previous segment
			top, stack = stack[len(stack)-1], stack[:len(stack)-1]
			rev(top)
			stack[len(stack)-1] = append(stack[len(stack)-1], top...)
		} else { // append to current segment
			stack[len(stack)-1] = append(stack[len(stack)-1], s[i])
		}
	}
	return string(stack[0])
}

func rev(seg []byte) {
	i, j := 0, len(seg)-1
	for i < j {
		seg[i], seg[j] = seg[j], seg[i]
		i++
		j--
	}
}

// @lc code=end

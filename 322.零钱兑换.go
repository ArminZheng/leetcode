package main

import (
	"fmt"
)

func coinChange(coins []int, amount int) int {
	var dp = make([]int, amount+1)
	for i := range dp {
		dp[i] = amount + 1
	}
	dp[0] = 0
	for i := 1; i < len(dp); i++ {
		for _, coin := range coins {
			if i < coin {
				continue
			}
			dp[i] = min(dp[i], dp[i-coin]+1)
		}
	}
	if dp[amount] == amount+1 {
		return -1
	}
	return dp[amount]
}

func min(a int, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}

func main() {
	list := []int{1, 2, 5}
	result := coinChange(list, 11)
	fmt.Println(result)
}

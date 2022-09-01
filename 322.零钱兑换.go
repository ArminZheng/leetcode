package main

import (
	"errors"
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

var ErrDivideByZero = errors.New("divide by zero")

func Divide(a, b int) (int, error) {
	if b == 0 {
		return 0, ErrDivideByZero
	}
	return a / b, nil
}

func testErr() {
	a, b := 10, 0
	result, err := Divide(a, b)
	if err != nil {
		switch {
		case errors.Is(err, ErrDivideByZero):
			fmt.Println("divide by zero error")
		default:
			fmt.Printf("unexpected division error: %s\n", err)
		}
		return
	} else {
		print("hello: ")
		print(err)
	}

	fmt.Printf("%d / %d = %d\n", a, b, result)
}

func testMap() {
	mapx := make(map[int]*int)
	t := []int{1, 2, 3}
	for k, v := range t {
		fmt.Println(v)
		fmt.Println(&v)
		fmt.Println(&k)
		mapx[v] = &v
	}
	for i, val := range mapx {
		fmt.Printf("%d %d \n", i, *val)
	}
	fmt.Println(mapx[1])
	fmt.Println(mapx[2])
	fmt.Println(mapx[3])
}

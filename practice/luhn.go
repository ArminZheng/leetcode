package main

import (
	"fmt"
)

/**
 * luhn 算法 (为防误输入设计)
 */
func main() {
	// 6258 520 9988 8888
	// 6258 58 20 99 88 8888
	// 6258 5800 58 00 8888
	for i := 0; i < 10000; i++ {
		checkBankCardNum(fmt.Sprintf("625858%04d888888", i))
	}
	fmt.Println(gg)
	// fmt.Println(checkBankCardNum("6258585399888888"))
	fmt.Println(checkBankCardNum("6258580020238888"))
}

var gg int = 0

func checkBankCardNum(n string) bool {
	total := 0
	for i := len(n) - 1; i >= 0; i-- {
		t := int(n[i]) - int('0')
		if i%2 == 0 {
			t *= 2
			if t > 9 {
				total += t - 9
			} else {
				total += t
			}
		} else {
			total += t
		}
	}

	if total%10 == 0 {
		fmt.Print(n + "\t")
		gg++
		if gg%9 == 0 {
			fmt.Println()
		}
	}
	return total%10 == 0
}

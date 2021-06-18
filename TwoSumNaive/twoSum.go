package main

import "fmt"

func twoSum(ls []int, target int) []int {

	for i := 0; i < len(ls); i++ {
		for j := i + 1; j < len(ls)-i; j++ {
			if (ls[i] + ls[j]) == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}

func main() {

	var ls = []int{2, 7, 11, 15}
	var target int = 18
	var result = twoSum(ls, target)
	fmt.Println("result is: ", result)
}

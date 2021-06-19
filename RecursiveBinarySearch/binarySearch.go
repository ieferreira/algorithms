package main

import "fmt"

func binarySearch(ls []int, low int, high int, target int) int {

	if high >= low {
		var mid int = (high + low) //2
		if ls[mid] == target {
			return mid
		} else if ls[mid] > target {
			return binarySearch(ls, low, mid-1, target)
		} else if ls[mid] < target {
			return binarySearch(ls, mid+1, high, target)
		}
	}

	return -1
}

func main() {
	var ls = []int{2, 3, 4, 10, 14, 21, 25, 29, 32, 220, 980, 1001, 1200, 1230}
	var target int = 1001
	var result = binarySearch(ls, 0, len(ls)-1, target)
	if result == -1 {
		fmt.Println("Result not found")
	} else {
		fmt.Println("target is located at index: ", result)
	}
}

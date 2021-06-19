package main

import "fmt"

func main() {
	var n int
	var k int
	fmt.Print("n: ")
	fmt.Scan(&n)
	fmt.Print("k:")
	fmt.Scan(&k)
	for i := 0; i < k; i++ {
		if n%10 == 0 {
			n = n / 10
		} else {
			n -= 1
		}
	}
	fmt.Print(n)

}

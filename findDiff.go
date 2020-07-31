package main

import "fmt"

func main() {
	N := []int{5, 20, 3, 2, 50, 80}
	target := 78
	fmt.Println(findNumber(N, target))
}

func findNumber(N []int, target int) []int {
	m := make(map[int]int)

	for i := 0; i < len(N); i++ {
		diff := N[i] - target
		if _, exists := m[diff]; exists {
			return []int{N[i], diff}
		}
		m[N[i]] = i
	}
	return nil
}

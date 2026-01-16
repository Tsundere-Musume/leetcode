package main

import "fmt"

func checkInclusion(s1 string, s2 string) bool {
	if len(s1) > len(s2) {
		return false
	}
	counter1 := [26]int{}
	counter2 := [26]int{}

	for i := range len(s1) {
		counter1[s1[i] - 'a'] += 1
		counter2[s2[i] - 'a'] += 1
	}

	matches := 0
	for i := range 26 {
		if counter1[i] == counter2[i] {
			matches ++ 
		}
	}

	l := 0
	for r := len(s1); r < len(s2); r++ {
		if matches == 26 {
			return true
		}
		idx := s2[r] - 'a'
		if counter2[idx] == counter1[idx] {
			matches--
		}
		counter2[idx]++
		if counter2[idx] == counter1[idx] {
			matches++
		}

		idx = s2[l] - 'a'
		if counter2[idx] == counter1[idx] {
			matches--
		}
		counter2[idx]--
		if counter2[idx] == counter1[idx] {
			matches++
		}
		l++
	}
	return matches == 26
}

func main() {
	s1 := "adc"
	s2 := "dcda"
	fmt.Println(checkInclusion(s1, s2))

	s1 = "ab"
	s2 = "lecabee"
	fmt.Println(checkInclusion(s1, s2))
}

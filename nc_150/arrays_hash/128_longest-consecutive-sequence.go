package main

func longestConsecutive(nums []int) int {
	values := make(map[int]struct{})
    for _, v := range  nums{
        values[v] = struct{}{}
    }
	longestChain := 0	
	for k := range values{
		if _, ok := values[k - 1]; ok{
			continue
		}

		chain := 0
		for {
			_, ok := values[k + chain]
			if !ok {
				break
			}
			chain++

		}

		if chain > longestChain{
			longestChain = chain
		}

	}
	return longestChain
}



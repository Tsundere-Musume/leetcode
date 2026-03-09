package leetcode

func rightSideView(root *TreeNode) []int {
	result := []int{}
	q := []*TreeNode{root}
	for len(q) > 0 {
		size := len(q)
		level := len(result)
		for range size {
			node := q[0]
			q = q[1:]

			if node == nil {
				continue
			}

			if l := len(result); l == level {
				result = append(result, node.Val)
			} else {
				result[l-1] = node.Val
			}

			q = append(q, node.Left)
			q = append(q, node.Right)

		}

	}
	return result
}

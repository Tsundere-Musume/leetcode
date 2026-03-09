package leetcode

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	result := make([][]int, 0)
	q := []*TreeNode{root}

	for len(q) > 0 {
		size := len(q)
		levelResult := []int{}
		for range size {
			node := q[0]
			q = q[1:]

			if node == nil {
				continue
			}

			levelResult = append(levelResult, node.Val)
			q = append(q, node.Left)
			q = append(q, node.Right)
		}

		if len(levelResult) > 0 {
			result = append(result, levelResult)
		}
	}
	return result

}

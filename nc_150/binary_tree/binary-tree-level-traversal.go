package leetcode

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	result := make([][]int, 0)

	if root == nil {
		return result
	}

	type LevelNode struct {
		Level int
		Node  *TreeNode
	}
	q := []LevelNode{{0, root}}
	for len(q) > 0 {
		top := q[0]
		q = q[1:]

		if len(result) <= top.Level {
			result = append(result, []int{})
		}
		result[top.Level] = append(result[top.Level], top.Node.Val)
		if top.Node.Left != nil {
			q = append(q, LevelNode{top.Level + 1, top.Node.Left})
		}
		if top.Node.Right != nil {
			q = append(q, LevelNode{top.Level + 1, top.Node.Right})
		}
	}

	return result

}

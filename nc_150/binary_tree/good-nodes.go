package leetcode

func goodNodes(root *TreeNode) int {
	var dfs func(*TreeNode, int) int
	dfs = func(node *TreeNode, max int) int {
		if node == nil {
			return 0
		}

		result := 0
		if max <= node.Val {
			result = 1
		}
		if (node.Val > max) {
			max = node.Val
		}
		result += dfs(node.Left, max)
		result += dfs(node.Right, max)
		return result
	}

	return dfs(root, root.Val)
}

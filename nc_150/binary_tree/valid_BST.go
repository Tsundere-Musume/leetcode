package leetcode
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isValidBST(root *TreeNode) bool {
	result := true
	var dfs func(*TreeNode, int) int
	dfs = func (node *TreeNode, last int) int {
		if (node == nil) {
			return last
		}

		last = dfs(node.Left, last)
		result = result && (last < node.Val)
		last = dfs(node.Right, last)
		return last
	}
	dfs(root, -10001)
	return result
}


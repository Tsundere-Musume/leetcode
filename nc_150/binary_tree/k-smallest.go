package leetcode
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func kthSmallest(root *TreeNode, k int) int {
	count, res := k, 0

	var dfs func(*TreeNode)
	dfs = func (node *TreeNode) {
		if (node == nil) {
			return 
		}

		dfs(node.Left)
		count--
		if (count == 0) {
			res = node.Val
			return
		}
		dfs(node.Right)
	}
	dfs(root)
	return res
}


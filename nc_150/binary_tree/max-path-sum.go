package leetcode

import "math"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func maxPathSum(root *TreeNode) int {
	result := math.MinInt
	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}

		l := dfs(node.Left)
		r := dfs(node.Right)
		result = max(result, l, r, l+node.Val+r)
		return node.Val + max(l, r)
	}

	dfs(root)
	return result
}

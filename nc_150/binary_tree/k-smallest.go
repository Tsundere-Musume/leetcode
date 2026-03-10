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
	result := -1  
	dfs(root, k, 0, &result)
	return result
}

func dfs(node *TreeNode, k int, count int, result *int) int  {
	if (node == nil || count > k) {
		return count
	}
	count = dfs(node.Left, k, count, result)
	count++
	if (count == k) {
		*result = node.Val
		return count
	}
	count = dfs(node.Right, k, count, result)
	return count
}


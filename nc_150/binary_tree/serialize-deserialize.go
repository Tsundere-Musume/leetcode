package leetcode

import (
	"strconv"
	"strings"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	if root == nil {
		return ""
	}

	var sb strings.Builder

	var dfs func(*TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			sb.WriteString("nil,")
			return
		}

		sb.WriteString(strconv.Itoa(node.Val))
		sb.WriteString(",")
		dfs(node.Left)
		dfs(node.Right)
	}

	dfs(root)
	return sb.String()

}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	if data == "" {
		return nil
	}

	parts := strings.Split(data, ",")
	curr := 0
	var dfs func() *TreeNode
	dfs = func() *TreeNode {
		if curr == len(parts)-1 || parts[curr] == "nil" {
			return nil
		}

		val, _ := strconv.Atoi(parts[curr])
		node := TreeNode{Val: val}
		curr++
		node.Left = dfs()
		curr++
		node.Right = dfs()
		return &node
	}
	return dfs()
}

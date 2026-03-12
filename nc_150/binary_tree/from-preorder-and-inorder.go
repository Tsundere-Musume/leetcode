package leetcode


func buildTree(preorder []int, inorder []int) *TreeNode {
	idxMap := make(map[int]int)
	for idx , v := range inorder {
		idxMap[v] = idx
	}

	currPos := 0
	var dfs func(l, r int)  *TreeNode
	dfs = func(l, r int) *TreeNode{
		if l > r{
			return nil
		}
		currVal := preorder[currPos]
		currPos++

		node := TreeNode{ Val: currVal }
		node.Left = dfs(l, idxMap[currVal] - 1)
		node.Right = dfs(idxMap[currVal] + 1, r)
		return &node
	}

	return dfs(0, len(inorder) - 1)
}

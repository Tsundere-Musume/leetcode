# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, result) -> int: 
            if not node:
                return 0
            left = dfs(node.left, result)
            right = dfs(node.right, result)
            result[0] = max(left + right, result[0])
            return 1 + max(left, right)

        result = [0]
        dfs(root, result)
        return result[0]

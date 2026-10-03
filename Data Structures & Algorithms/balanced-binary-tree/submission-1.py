# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]                  # assume balanced until a node proves otherwise

        def dfs(node):                     # returns the HEIGHT, same as maxDepth
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:      # sides too uneven at this node?
                balanced[0] = False
            return 1 + max(left, right)

        dfs(root)
        return balanced[0]
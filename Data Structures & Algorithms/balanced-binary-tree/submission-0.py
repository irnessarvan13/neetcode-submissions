# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0 
            left = height(node.left)              # get left height
            right = height(node.right)            # get right height
    
            if abs(left - right) > 1:            # difference more than 1 — not balanced
                return -1
            if right == -1 or left == -1:
                return -1
    
            return 1 + max(left, right)           # return height of this node
        return height(root) != -1   # if height is -1 it means unbalanced
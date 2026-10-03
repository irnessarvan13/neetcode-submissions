# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:       # both empty → same
            return True
        if not p or not q:        # only one empty → different shape
            return False
        if p.val != q.val:        # different values → different
            return False

        # this spot matches → both sides must match too
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
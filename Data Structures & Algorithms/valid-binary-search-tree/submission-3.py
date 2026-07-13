# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root, ivl: Tuple) -> bool:
        if not root:
            return True
        if root.val >= ivl[1] or root.val <= ivl[0]:
            return False
        return self.recurse(root.left, (ivl[0], root.val)) and self.recurse(root.right, (root.val, ivl[1]))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recurse(root, (-math.inf, math.inf))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasNode(self, root, node) -> bool:
        if root is None:
            return False
        if root.val == node.val:
            return True
        return self.hasNode(root.left, node) or self.hasNode(root.right, node)
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        leftValid = self.hasNode(root.left, p) and self.hasNode(root.left, q)
        rightValid = self.hasNode(root.right, p) and self.hasNode(root.right, q)
        if not leftValid and not rightValid:
            return root
        if leftValid:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        
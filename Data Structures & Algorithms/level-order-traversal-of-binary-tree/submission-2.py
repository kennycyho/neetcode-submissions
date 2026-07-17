# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []

        q = [root]
        while len(q) > 0:
            level = []
            for i in range(len(q)):
                first = q.pop(0)
                level.append(first.val)
                if first.left:
                    q.append(first.left)
                if first.right:
                    q.append(first.right)
            res.append(level)

        return res



"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    nodeMap = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        if node in self.nodeMap:
            return self.nodeMap[node]
        #clone node
        clone = Node(node.val)
        self.nodeMap[node] = clone
        #traverse neighbors
        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor))
        return clone
        
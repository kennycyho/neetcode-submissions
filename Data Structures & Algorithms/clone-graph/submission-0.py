"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneNode(self, node, node_copy, seen):
        seen[node_copy.val] = node_copy
        for n in node.neighbors:
            if n.val not in seen:
                n_copy = Node(n.val, [])
                self.cloneNode(n, n_copy, seen)
            else:
                n_copy = seen[n.val]
            node_copy.neighbors.append(n_copy)

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_copy = Node(node.val, [])
        self.cloneNode(node, node_copy, {})
        return node_copy
        
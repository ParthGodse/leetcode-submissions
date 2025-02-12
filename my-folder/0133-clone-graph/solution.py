"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}

        def dfs(node):

            if node in seen:
                return seen[node]

            copy = Node(node.val)
            seen[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy
        return dfs(node) if node else None

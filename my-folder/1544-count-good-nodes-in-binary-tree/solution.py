# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]

        if not root:
            return None
        
        good = 0

        while stack:
            node, max_value = stack.pop()

            if node.val >= max_value:
                good += 1
            
            max_value = max(max_value, node.val)

            if node.right:
                stack.append((node.right, max_value))
            if node.left:
                stack.append((node.left, max_value))

        return good

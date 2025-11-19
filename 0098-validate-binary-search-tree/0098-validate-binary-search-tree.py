# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        lower = float('-inf')
        upper = float('inf')

        stack = [(root, lower, upper)]

        while stack:
            node, less, great = stack.pop()

            if node.val <= less or node.val >= great:
                return False

            if node.right:
                stack.append((node.right, node.val, great))
            if node.left:
                stack.append((node.left, less, node.val))

        return True
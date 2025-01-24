# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node:
                return 0

            left_d = depth(node.left)
            right_d = depth(node.right)

            if left_d == -1 or right_d == -1:
                return - 1

            if abs(left_d - right_d) > 1:
                return - 1

            return 1 + max(left_d, right_d)

        return depth(root) != -1

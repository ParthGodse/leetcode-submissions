# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0 

        def diameter(node):
            if not node:
                return 0

            left_d = diameter(node.left)
            right_d = diameter(node.right)

            add = left_d + right_d
            self.max_diameter = max(self.max_diameter, add)

            return 1 + max(left_d, right_d)
        
        diameter(root)
        return self.max_diameter

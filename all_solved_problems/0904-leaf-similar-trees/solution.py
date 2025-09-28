# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root):
            if not root:
                return []

            stack = [root]
            leaves = []

            while stack:
                node = stack.pop()

                if not node.left and not node.right:
                    leaves.append(node.val)
                else:
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
            return leaves

        l1 = leaves(root1)
        l2 = leaves(root2)

        if l1 != l2:
            return False
        else:
            return True

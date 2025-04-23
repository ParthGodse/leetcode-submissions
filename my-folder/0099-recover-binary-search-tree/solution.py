# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        small = big = prev = None

        def inorder(root):
            nonlocal small, big, prev
            if not root:
                return
            inorder(root.left)
            if prev and prev.val > root.val:
                small = root
                if not big:
                    big = prev
            prev = root
            inorder(root.right)

        inorder(root)

        small.val, big.val = big.val, small.val

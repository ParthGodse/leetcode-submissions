# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # if root is None:
        #     return 0

        # stack = [root]
        # count = 0

        # while stack:
        #     node = stack.pop()
        #     count += 1
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)

        # return count
        if not root:
            return 0

        left, right = root, root
        heightl, heightr = 0, 0
        while left:
            heightl += 1
            left = left.left
        while right:
            heightr += 1
            right = right.right

        if heightl == heightr:
            return pow(2, heightl) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

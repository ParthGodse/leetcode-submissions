# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        stack = [(root, root.val, [root.val])]
        result = []

        while stack:
            node, total, path = stack.pop()

            if not node.left and not node.right:
                if total == targetSum:
                    result.append(path)

            if node.right:
                stack.append((node.right, total + node.right.val, path + [node.right.val]))
            if node.left:
                stack.append((node.left, total + node.left.val, path + [node.left.val]))

        return result

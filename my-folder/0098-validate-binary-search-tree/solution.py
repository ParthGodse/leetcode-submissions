# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # stack = [(root, float('-inf'), float('inf'))]

        # if not root:
        #     return True

        # while stack:

        #     node, lower, upper = stack.pop()

        #     if node.val <= lower or node.val >= upper:
        #         return False

        #     if node.right:
        #         stack.append((node.right, node.val, upper))
        #     if node.left:
        #         stack.append((node.left, lower, node.val))

        # return True
        
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True

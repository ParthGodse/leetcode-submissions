# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # q = deque()
        # if root:
        #     q.append(root)

        # lvl = 0
        # while q:
        #     for i in range(len(q)):
        #         node =q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     lvl += 1
        # return lvl
        if not root:
            return 0
        left_d = self.maxDepth(root.left)
        right_d = self.maxDepth(root.right)
        return 1 + max(left_d, right_d)

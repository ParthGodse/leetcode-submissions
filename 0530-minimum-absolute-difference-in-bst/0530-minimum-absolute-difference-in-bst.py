# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []

        def inorder(root):
            if not root:
                return 0

            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        
        inorder(root)
        l = 0
        r = 1
        minn = float('inf') 
        while r < len(arr):
            total = abs(arr[r] - arr[l])
            if total < minn:
                minn = total
            l += 1
            r += 1
        return minn
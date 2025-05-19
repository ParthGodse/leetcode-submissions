# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # hmap = {value: idx for idx, value in enumerate(inorder)}

        # def dfs(preorder, l, r):
        #     if not preorder or l > r:
        #         return None
            
        #     root_value = preorder.pop(0)
        #     root = TreeNode(root_value)

        #     root_index = hmap[root_value]

        #     root.left = dfs(preorder, l, root_index - 1)
        #     root.right = dfs(preorder, root_index + 1, r)

        #     return root
        # return dfs(preorder, 0, len(inorder) - 1)
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_map = {value: idx for idx, value in enumerate(inorder)}
        # self.post_index = len(postorder) - 1
        def dfs(l, r):
            if l > r:
                return None
            
            root_value = postorder.pop()
            # self.post_index -= 1
            root = TreeNode(root_value)
            
            index = in_map[root_value]  # Find in postorder

            # Recursively build left and right subtrees
            root.right = dfs(index + 1, r) 
            root.left = dfs(l, index - 1)   

            return root
        
        return dfs(0, len(inorder) - 1)

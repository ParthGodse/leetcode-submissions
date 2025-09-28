# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # hmap = {value: idx for idx, value in enumerate(postorder)}

        # def dfs(preorder, l, r):
        #     if not preorder or l > r:
        #         return None
            
        #     root_value = preorder.pop(0)
        #     root = TreeNode(root_value)
        #     root_index = hmap[root_value]

        #     root.left = dfs(preorder, l, root_index - 1)
        #     root.right = dfs(preorder, root_index + 1, r)

        #     return root
        # return dfs(preorder, 0, len(postorder) - 1)
        post_map = {value: idx for idx, value in enumerate(postorder)}
        self.pre_idx = 0  # Track index in preorder

        def dfs(l, r):
            if self.pre_idx >= len(preorder) or l > r:
                return None
            
            root_value = preorder[self.pre_idx]
            root = TreeNode(root_value)
            self.pre_idx += 1  # Move to the next preorder element

            if l == r:  # Leaf node, return immediately
                return root
            
            left_value = preorder[self.pre_idx]  # Next value in preorder is left child
            left_index = post_map[left_value]  # Find in postorder

            # Recursively build left and right subtrees
            root.left = dfs(l, left_index)  
            root.right = dfs(left_index + 1, r - 1)  

            return root
        
        return dfs(0, len(postorder) - 1)

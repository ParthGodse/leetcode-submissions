# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node, val):
            if not node:
                return None
            if val < node.val:
                node.left = delete(node.left, val)
            elif val > node.val:
                node.right = delete(node.right, val)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                min_larger_node = _find_min(node.right)
                node.val = min_larger_node.val
                node.right = delete(node.right, min_larger_node.val)

            return node

        def _find_min(node):
            while node.left:
                node = node.left
            return node

        return delete(root, key)

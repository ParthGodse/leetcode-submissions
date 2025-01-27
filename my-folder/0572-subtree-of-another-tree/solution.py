# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        stack = [root]

        while stack:
            node = stack.pop()

            if node and node.val == subRoot.val:  
                if self.isSameTree(node, subRoot):  
                    return True  

            if node:  
                if node.right:
                    stack.append(node.right)  
                if node.left:
                    stack.append(node.left)  

        return False  

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        st = [(p, q)]

        while st:
            node1, node2 = st.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            st.append((node1.right, node2.right))
            st.append((node1.left, node2.left))

        return True

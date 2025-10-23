# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("N")

        return ",".join(map(str,res))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "N":
            return None

        data = data.split(",")
        root = TreeNode(data[0])
        q = deque([root])
        i = 1

        while q and i < len(data):
            curr = q.popleft()

            if i < len(data) and data[i] != "N":
                curr.left = TreeNode(data[i])
                q.append(curr.left)
            i += 1

            if i < len(data) and data[i] != "N":
                curr.right = TreeNode(data[i])
                q.append(curr.right)
            i += 1

        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
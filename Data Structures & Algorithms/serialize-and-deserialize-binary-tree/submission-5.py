# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if not node:
                res.append("N")
                continue
            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(",")
        if preorder[0] == "N":
            return None
        root = TreeNode(int(preorder[0]))

        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if preorder[i] != "N":
                node.left = TreeNode(int(preorder[i]))
                q.append(node.left)
            i += 1
            if preorder[i] != "N":
                node.right = TreeNode(int(preorder[i]))
                q.append(node.right)
            i += 1
        return root




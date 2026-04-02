# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def maxnode(node):
            while node.right:
                node = node.right
            return node.val
        def minnode(node):
            while node.left:
                node = node.left
            return node.val
        if not root:
            return True
        elif root.left and maxnode(root.left) >= root.val:
            return False
        elif root.right and minnode(root.right) <= root.val:
            return False
        else:
            return self.isValidBST(root.left) and self.isValidBST(root.right)

            
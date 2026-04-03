# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        elif root and subRoot and subRoot.val == root.val:
            return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, tree1, tree2):
        if tree1 and tree2:
            return tree1.val == tree2.val and self.isSameTree(tree1.left, tree2.left) and self.isSameTree(tree1.right, tree2.right)
        elif (tree1 and not tree2) or (not tree1 and tree2):
            return False
        return True
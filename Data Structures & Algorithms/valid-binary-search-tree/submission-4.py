# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def iot(node): 
            nonlocal arr
            if not node:
                return
            if node.left:
                iot(node.left)
            arr.append(node.val)
            if node.right:
                iot(node.right)
        iot(root)
        print(arr)
        return arr == sorted(arr)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def balance(root):
            if root is None:
                return 0
            lheight = balance(root.left)
            rheight = balance(root.right)

            if lheight == -1 or rheight == -1 or abs(lheight - rheight) > 1:
                return -1
            return max(lheight, rheight) + 1
        
        return balance(root) >= 0
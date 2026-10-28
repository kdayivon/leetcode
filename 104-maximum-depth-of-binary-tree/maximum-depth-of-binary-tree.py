# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def height(root):
            if root is None:
                return -1
            left_height = height(root.left)
            right_height = height(root.right)
            return max(left_height, right_height) + 1
        return height(root) + 1
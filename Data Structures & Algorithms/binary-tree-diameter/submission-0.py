# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(current):
            nonlocal diameter

            if not current:
                return 0

            left_depth = dfs(current.left)
            right_depth = dfs(current.right)

            diameter = max(diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)
        
        dfs(current=root)
        
        return diameter
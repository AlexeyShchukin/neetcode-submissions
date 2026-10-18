# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]

            height_left = dfs(node.left)
            height_right = dfs(node.right)
            
            is_balanced = height_left[0] and height_right[0] and abs(height_left[1] - height_right[1]) <= 1

            return [is_balanced, 1 + max(height_left[1], height_right[1])]
        
        return dfs(root)[0]
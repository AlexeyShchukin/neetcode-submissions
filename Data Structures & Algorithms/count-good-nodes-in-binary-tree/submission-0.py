# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = collections.deque()
        q.append((root, root.val))
        count = 0

        while q:
            for _ in range(len(q)):
                node, max_val = q.popleft()
                if node.val >= max_val:
                    count += 1

                if node.left:
                    q.append((node.left, max(node.left.val, max_val)))
                if node.right:
                    q.append((node.right, max(node.right.val, max_val)))
        return count

        
            

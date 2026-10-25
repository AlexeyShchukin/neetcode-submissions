# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"

        q = collections.deque()
        q.append(root)
        res = []

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    res.append("null")
                else:
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
        
        return ", ".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data == "null":
            return None

        arr = data.split(", ")
        root = TreeNode(int(arr[0]))
        
        q = collections.deque()
        q.append(root)
        idx = 1
        
        while q:
            node = q.popleft()
            if arr[idx] != "null":
                node.left = TreeNode(int(arr[idx]))
                q.append(node.left)
            idx += 1
            if arr[idx] != "null":
                node.right = TreeNode(int(arr[idx]))
                q.append(node.right)
            idx += 1
        
        return root

            


        
            



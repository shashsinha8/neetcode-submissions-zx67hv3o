# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        if not root: 
            return 0 

        q = collections.deque()
        q.append(root)
        levels = 0

        while q:
            
            level_nodes = len(q)

            for _ in range(level_nodes):
                
                curr = q.popleft()

                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)

            levels += 1

        return levels



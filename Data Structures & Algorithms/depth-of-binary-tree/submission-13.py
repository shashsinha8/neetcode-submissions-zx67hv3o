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
        def dfs(node, depth):
            stack = deque()
            stack.append((root, depth))
            maxd = 0
            while stack: 
                curr, depth = stack.pop()
                
                # process                
                maxd = max(maxd, depth)

                # add to stack
                if curr.left: stack.append((curr.left, depth + 1))
                if curr.right: stack.append((curr.right, depth + 1))
                
            return maxd
    
        return dfs(root, 1)
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

        def dfs(root):
            res = 0
            q = deque()
            q.append((root, 1))

            while q: 
                # pop
                curr, depth = q.pop()
                
                # process
                if curr:

                    res = max(res, depth)
                    # update q
                    q.append((curr.left, depth+1))
                    q.append((curr.right, depth+1))

            return res
        return dfs(root)
        

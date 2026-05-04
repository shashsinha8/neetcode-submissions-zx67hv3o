# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.ctr = 0
        self.ans = 0
        def dfs(root):
            if not root:
                return
    
            # in order dfs
            
            # left
            dfs(root.left)
            # process
            self.ctr += 1
            if self.ctr == k: 
                self.ans = root
            # right
            dfs(root.right)
        
        dfs(root)
        return (self.ans.val)

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.answer = None
        
        def dfs(root):
            
            #base if end what to do
            if not root: 
                return False

            left = dfs(root.left)
            right = dfs(root.right)
            mid = (root.val == p.val or root.val == q.val)


            if mid + left + right >= 2:
                self.answer = root
            
            return mid or left or right
        
        dfs(root)
        return self.answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0
        def dfs(root):

            # base case return when None
            if not root: 
                return 0
            
            # calculate go left then right
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            # max diameter
            self.diameter = max(self.diameter, left_depth + right_depth)

            # return
            return 1 + max(left_depth, right_depth)
        
        dfs(root)
        return self.diameter

            



        
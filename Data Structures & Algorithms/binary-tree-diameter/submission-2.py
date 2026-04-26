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
            if not root:
                return 0
            
            left_d = dfs(root.left)
            right_d = dfs(root.right)

            local_d = left_d + right_d

            self.diameter = max(self.diameter, local_d)

            return 1 + max(left_d, right_d)
        
        dfs(root)
        return self.diameter
            



        
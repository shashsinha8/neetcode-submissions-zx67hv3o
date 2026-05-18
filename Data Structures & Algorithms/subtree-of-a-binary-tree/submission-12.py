# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        
        def isSame(s, t): 
            if not s and not t: 
                return True
            elif not s or not t: 
                return False
            elif s.val != t.val: 
                return False
            
            left = isSame(s.left, t.left)
            right = isSame(s.right, t.right)

            return left and right

        if not t: 
            return True
        elif not s: 
            return False
        elif isSame(s, t):
            return True
        
        left = self.isSubtree(s.left, t)
        right = self.isSubtree(s.right, t)

        return left or right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:

        def same(s, t):
            if not s and not t: 
                return True
            elif not s or not t: 
                return False
            elif s.val != t.val:
                return False
            
            return same(s.left, t.left) and same(s.right, t.right)
        
        if not s and not t: 
            return True
        elif not s or not t: 
            return False
        elif same(s, t): 
            return True

        return self.isSubtree(s.left, t)  or self.isSubtree(s.right, t) 

        



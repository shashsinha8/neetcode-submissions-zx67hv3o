# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root: 
            return False
        
        def isSame(root, sub):
            if not root and not sub: 
                return True
            elif not root or not sub:
                return False
            elif root.val != sub.val:
                return False
            
            return isSame(root.left, sub.left) and isSame(root.right, sub.right)
            
        if isSame(root, subRoot): return True
        
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    


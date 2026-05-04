# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    
        def dfs(node, p, q): 
            if not node: 
                print(f"{p.val},{q.val}")
                return
            elif p.val < node.val and q.val < node.val:
                print(f"{p.val},{q.val} < {node.val}")
                return dfs(node.left, p, q)
            elif p.val > node.val and q.val > node.val:
                print(f"{p.val},{q.val} > {node.val}")
                return dfs(node.right, p, q)
            else: 
                return node
        return dfs(root, p, q)
        # curr = root
        # while curr: 
        #     if p.val < curr.val and q.val < curr.val:
        #         curr = curr.left
        #     elif p.val > curr.val and q.val > curr.val: 
        #         curr = curr.right
        #     else: 
        #         return curr 

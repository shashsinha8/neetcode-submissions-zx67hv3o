# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: 
            return

        q = collections.deque()
        q.append(root)

        while q:
            
            # current node: pop q element
            curr = q.popleft()
            # process nodes: 
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            # add next node into the stack
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        
        return root

            


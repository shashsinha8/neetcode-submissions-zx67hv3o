# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True

        def bfs(node):

            q = collections.deque()
            q.append(node)
            levels = 0
            if not node:
                return 0

            while q: 
                # number of nodes in level
                num_nodes = len(q)

                for _ in range(num_nodes):
                    # popleft()
                    curr = q.popleft()

                    # update pointers
                    if curr.left: q.append(curr.left)
                    if curr.right: q.append(curr.right)
                
                levels += 1
            return levels
        
        diff = abs(bfs(root.left) - bfs(root.right))

        

        if diff <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else: 
            return False



        
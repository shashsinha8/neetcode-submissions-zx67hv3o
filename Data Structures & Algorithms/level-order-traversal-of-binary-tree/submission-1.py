# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: 
            return []
        self.answer = []
        def bfs(root):

            q = deque()
            q.append(root)
            
            while q: 
                level = len(q)
                local = []
                for _ in range(level):
                    curr = q.popleft()
                    local.append(curr.val)
                    
                    # update
                    if curr.left: q.append(curr.left)
                    if curr.right: q.append(curr.right)
                self.answer.append(local)
            return self.answer
        return bfs(root)


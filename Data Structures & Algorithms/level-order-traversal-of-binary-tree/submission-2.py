# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
            
        def bfs(node):

            q = deque([node])
            ans = []


            while q:
                level_nodes = len(q)
                local = []

                for _ in range(level_nodes):
                    curr = q.popleft()
                    local.append(curr.val)
                    if curr.left: q.append(curr.left)
                    if curr.right: q.append(curr.right)
                ans.append(local)
            return ans
        
        return bfs(root) if root is not None else []


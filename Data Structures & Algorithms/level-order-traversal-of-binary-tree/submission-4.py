# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        def bfs(root):

            q = deque()
            q.append(root)
            ans = []
            while q:
                # track number of nodes in each level
                num_nodes = len(q)
                local_level = []

                for _ in range(num_nodes):
                    # popleft
                    curr = q.popleft()
                    # process
                    local_level.append(curr.val)
                    
                    # append neighbors to q
                    q.append(curr.left) if curr.left else None
                    q.append(curr.right) if curr.right else None
                
                ans.append(local_level)
            return ans
        if not root: 
            return []
        return (bfs(root))

            


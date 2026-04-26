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
        
        self.ans = []

        def bfs(root): 
            
            # define q: 
            q = collections.deque()

            # add root to q: 
            q.append(root)

            # start while loop
            while q:

                # number of nodes in level = len of q
                num_nodes = len(q)
                this_level= []
                curr = None

                # for loop #nodes in level times
                for _ in range(num_nodes):
                
                    # popleft()]
                    curr = q.popleft()

                    # append to level array
                    this_level.append(curr.val)
                    
                    # Add next level to q
                    if curr.left: q.append(curr.left)
                    if curr.right: q.append(curr.right)

                # add to answer array
                self.ans.append(this_level)
                


        bfs(root)
        return self.ans



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: 
            return 0

        q = collections.deque()
        q.append((root,1))
        max_d = 0

        while q: 

            # pop()
            curr, depth = q.pop()

            # process
            max_d = max(max_d, depth)

            # visit next
            if curr.left: q.append((curr.left, depth + 1))
            if curr.right: q.append((curr.right, depth + 1))

        return max_d
            
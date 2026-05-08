# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # build index map from inorder list
        ind = {v: i for i, v in enumerate(inorder)}


        # init preorder index pointer
        self.pre_ind = 0

        #dfs function
        def dfs(l, r):
            # base case for left and right pointer 
            if l > r: 
                return None


            # root value is first preorder value
            root_val = preorder[self.pre_ind]
            # increment to next preorder ind
            self.pre_ind += 1

            # create node
            root= TreeNode(root_val)
            mid = ind[root_val]   # position of local root in inorder list is middle

            root.left = dfs(l, mid - 1) # recursively pass l and mid - 1(immediate left and lower limit)
            root.right = dfs(mid + 1, r) # recursively pass mid + 1(immediate right and upper limit)

            return root
        
        return dfs(0, len(inorder) - 1)


    
                    
            
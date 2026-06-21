class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        def dfs(): 
            stack = [0]
            visited = {0}
            
            while stack: 
                curr = stack.pop()
                for add in range(1, nums[curr] + 1): 
                    i = curr+add
                    if i >= len(nums) - 1:
                        return True
                    elif i not in visited:
                        stack.append(i)
                        visited.add(i)
            return False

        return dfs()
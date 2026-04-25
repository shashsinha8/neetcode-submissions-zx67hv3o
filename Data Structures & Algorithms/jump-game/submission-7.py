class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: 
            return True
        curr = nums[0]

        if curr >= len(nums) - 1:
            return True
        elif curr == 0 and len(nums) >= 1:
            return False

        path = False
        while curr:
            if len(nums) > 1:
                temp = self.canJump(nums[curr:])
                path = path or temp
                if path: 
                    break
                curr -= 1

        return path


"""
nums = [1,2,0,1,0]
curr = 1



"""
        

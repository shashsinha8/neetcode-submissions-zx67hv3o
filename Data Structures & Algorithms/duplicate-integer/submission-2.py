class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #nested for loops
        # for i in range(len(nums)): 
        #     for j in range(i+1, len(nums)): 
        #         if nums[i] == nums[j]: 
        #             return True
        # return False
        
        temp = []
        
        for i in range(len(nums)): 
            if nums[i] in temp: 
                return True
            else: 
                temp.append(nums[i])
        return False

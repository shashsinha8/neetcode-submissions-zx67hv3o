class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #nested for loops
        # for i in range(len(nums)): 
        #     for j in range(i+1, len(nums)): 
        #         if nums[i] == nums[j]: 
        #             return True
        # return False
        
        #sorting: 
        # newNums = sorted(nums)
        # for i in range(len(newNums)-1): 
        #     if newNums[i] == newNums[i+1]:
        #         return True
        # return False


        # Best answer: 
        # temp = []
        # for i in range(len(nums)): 
        #     if nums[i] in temp: 
        #         return True
        #     else: 
        #         temp.append(nums[i])
        # return False
        
        n = set()
        for i in range(len(nums)):
            if nums[i] in n:
                return True
            n.add(nums[i])
        return False
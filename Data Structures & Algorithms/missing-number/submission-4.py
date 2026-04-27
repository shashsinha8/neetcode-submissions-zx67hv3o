class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        add = len(nums)
        for i in range(len(nums)):
            add = add + i - nums[i]
        return add
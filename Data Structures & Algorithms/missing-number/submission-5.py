class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        add = 0
        for i in range(len(nums) + 1):
            add += i
        
        return abs(add - sum(nums))
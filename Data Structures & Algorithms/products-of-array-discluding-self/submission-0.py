class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if j != i: 
                    num *= nums[j]
            res.append(num)
        return res

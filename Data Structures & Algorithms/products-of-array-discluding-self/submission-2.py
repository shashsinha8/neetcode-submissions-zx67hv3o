class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # output = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j != i:
        #             output[i] = output[i] * nums[j]
        # return output

        # Hashmap solution
        output = [1] * len(nums)
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            for n in temp: 
                output[i] = output[i] * n
        
        return output




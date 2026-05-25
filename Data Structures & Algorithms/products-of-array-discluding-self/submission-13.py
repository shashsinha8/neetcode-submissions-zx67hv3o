class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        pre = 1
        for i in range(len(nums)):
            prefix.append(pre)
            pre *= nums[i]



        post = 1
        postfix = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = post
            post *= nums[i]
        
        # print(f"{nums}\n{prefix}\n{postfix}")
        for i in range(len(nums)): 
            postfix[i] *= prefix[i]
        
        return postfix
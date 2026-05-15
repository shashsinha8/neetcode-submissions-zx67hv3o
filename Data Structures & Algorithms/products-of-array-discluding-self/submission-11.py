class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            
        '''
        [1,1,2,8] # pre
        [48,24,6,1] # post
        '''

        prefix = []
        preval = 1
        for n in nums:
            prefix.append(preval)
            preval = preval * n
        print(prefix)

        postfix = [0] * len(nums) 
        postval = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = postval
            postval = postval * nums[i]
        print(postfix)


        for i in range(len(nums)): 
            postfix[i] *= prefix[i]

        return postfix
        
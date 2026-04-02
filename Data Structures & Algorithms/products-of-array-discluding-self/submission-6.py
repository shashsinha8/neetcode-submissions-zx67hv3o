class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:         

        # ans = []
        # for i in range(len(nums)):
        #     sum = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             sum *= nums[j]
        #     ans.append(sum)

        # print(ans)
        # return ans

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        pre = 1
        for i in range(len(nums)): 
            prefix[i] = prefix[i] * pre
            pre = pre * nums[i]
        print(prefix)

        post = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i] *= post
            post *= nums[i]
        print(postfix)


        ans = []
        for i in range(len(nums)):
            ans.append(postfix[i]*prefix[i])
        return ans
            

        print(prefix) 

        
        """
        [1 2 3 4]

        [1 1 2 6]
        [24 12 4 1]

        [1 2 3 4] = [24 12 8 6]


        [1 2 6 24]
        [X 2 3 4] = 24
        [1 X 3 4] = 12
        [1 2 X 4] = 8
        [1 2 3 X] = 6

        """

        # product = math.prod(nums)
        # print(product)

        # copy = nums.copy()
        # temp = 0
        # for i in range(len(nums)):
        #     # copy[i] = product/nums[i]
        #     # 120/10 = 120 - 12 * 9






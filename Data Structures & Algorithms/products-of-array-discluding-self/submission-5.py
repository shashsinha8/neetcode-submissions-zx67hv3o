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

        matrix = [[] for i in range(len(nums))]


        for i in range(len(nums)):
            copy = nums.copy()
            copy[i] = 1
            matrix[i] = copy
        
        result = []
        for i in range(len(nums)):
            result.append(math.prod(matrix[i]))
        
        return result
        
        """     
        [1 2 3 4] = [24 12 8 6]

        [X 2 3 4] = 24
        [1 X 3 4] = 12
        [1 2 X 4] = 8
        [1 2 3 X] = 6

        """






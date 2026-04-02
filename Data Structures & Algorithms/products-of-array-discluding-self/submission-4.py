class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # ds = [[] for in range(len(nums))]            

        ans = []
        for i in range(len(nums)):
            sum = 1
            for j in range(len(nums)):
                if i != j:
                    sum *= nums[j]
            ans.append(sum)

        print(ans)
        return ans





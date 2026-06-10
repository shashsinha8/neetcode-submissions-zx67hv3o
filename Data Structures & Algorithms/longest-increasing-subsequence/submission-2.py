class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums)):
            sub = []
            for j in range(i):
                if nums[j] < nums[i]:
                    sub.append(LIS[j])
            LIS[i] = 1 + max(sub, default=0)
        
        return max(LIS)
            


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        numset = set(nums)
        ans = 0
        for n in nums:
            num = n
            counter = 0
            while num in numset: 
                counter += 1
                num += 1
            ans = max(ans, counter)
        
        return ans
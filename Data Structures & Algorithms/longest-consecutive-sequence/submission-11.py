class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        ans = 0
        for n in nums:
            local = 0
            curr = n
            while curr in set(nums):
                curr += 1
                local += 1
            ans = max(ans, local)
        
        return ans
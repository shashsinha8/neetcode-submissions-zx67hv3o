class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        ans = 0
        for n in nums: 
            curr = n
            local = 0
            while curr in numset: 
                local += 1
                curr = curr + 1
            ans = max(ans, local)
        
        return ans

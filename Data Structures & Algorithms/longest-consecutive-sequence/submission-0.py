class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0

        for n in nums: 
            
            streak = 0
            curr = n

            while curr in nums: 
                streak += 1
                curr += 1
            res = max(res, streak)

        return res


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        res = 0

        for n in nums: 

            streak = 0
            curr = n
            while curr in nums:
                curr += 1
                streak += 1
            if streak > res: res = streak 

        return res
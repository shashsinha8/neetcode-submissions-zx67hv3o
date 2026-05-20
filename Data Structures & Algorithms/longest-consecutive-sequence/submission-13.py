class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        numset = set(nums)
        longest = 0
        for n in nums:
            curr = n
            local = 0
            while curr in numset:  
                curr = curr + 1
                local += 1
            longest = max(longest, local)

        return longest


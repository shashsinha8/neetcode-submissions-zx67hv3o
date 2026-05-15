class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        ans = 0
        for n in nums: 
            curr = n
            counter = 0
            while curr in numset: 
                curr = curr + 1
                counter += 1
            ans = max(ans, counter)
        return ans
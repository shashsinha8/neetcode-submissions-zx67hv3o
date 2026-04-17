class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        answer = 1
        for n in nums:

            length = 1
            curr = n
            while (curr + length) in nums_set:
                length += 1
                answer = max(answer, length)

        return answer

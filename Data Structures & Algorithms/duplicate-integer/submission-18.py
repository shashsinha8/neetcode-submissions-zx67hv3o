class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # true if any value appears more than once
        # false if no duplicate

        answer = []

        for n in nums: 
            if n in answer:
                return True
            answer.append(n)

        return False
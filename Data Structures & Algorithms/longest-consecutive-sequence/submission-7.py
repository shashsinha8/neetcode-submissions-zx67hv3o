class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nset = set(nums)
        answer = 0
        

        i = 0
        while i < len(nums):
            curr = nums[i]
            if (curr-1) in nset:
                i += 1
                continue
            else:
                count = 1
                while (curr+1) in nset:
                    count += 1
                    curr += 1
            answer = max(answer, count)
            i+=1


        return answer



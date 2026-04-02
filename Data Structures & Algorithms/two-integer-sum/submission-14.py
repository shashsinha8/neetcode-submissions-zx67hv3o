class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # GIVEN
        # nums = array of ints
        # target = target value
        
        # OUTPUT
        # return indices
        # nums[i] + nums[j] == target

        # BRAINSTORM:
        # nums = [3,4,5,6], target = 7
        # 3 + 4 = 7
        # [0, 1]

        answer = {}

        for i in range(len(nums)):
            
            diff = target - nums[i]
            if diff in answer:
                return [answer[diff], i]
            answer[nums[i]] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Given:
        # target
        # nums array
        
        # Return:
        # indices i, j
        hashmap = {}

        for i in range(len(nums)):

            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i


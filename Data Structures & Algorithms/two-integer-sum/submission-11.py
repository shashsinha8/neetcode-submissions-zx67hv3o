class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Given: 
            nums -> int array 
            target -> int value
        
        Goal:
            Return indices: i and j:
            nums[i] + nums[j] == target
            i != j
            
            (return smaller index first)

        Example: 
            nums = [3,4,5,6]    target = 7

            output = [0,1]
        '''
        
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i


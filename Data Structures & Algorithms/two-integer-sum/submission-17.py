class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Given:
        # target
        # nums array

        hash = {}


        for i, n in enumerate(nums): 
            diff = target - n
            if diff in hash:
                return [hash[diff], i]
            else: 
                hash[n] = i
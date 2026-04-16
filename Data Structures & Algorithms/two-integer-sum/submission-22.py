class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i, n in enumerate(nums):
        #     for j, m in enumerate(nums):
        #         if n + m == target and i !=j:
        #             return [i, j]

        sum_map = {}

        for i, n in enumerate(nums): 
            diff = target - n
            if diff in sum_map:
                return [sum_map[diff], i]
            else: 
                sum_map[n] = i
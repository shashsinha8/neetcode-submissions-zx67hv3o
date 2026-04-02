class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}

        for i in range(len(nums)):
            
            temp = target - nums[i]
            if temp in nmap: 
                return (nmap[temp], i)

            nmap[nums[i]] = i
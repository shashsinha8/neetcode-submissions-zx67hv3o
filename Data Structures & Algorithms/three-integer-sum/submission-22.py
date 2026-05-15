class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):
            l, r = i + 1 , len(nums) - 1
            if nums[i] > 0 : 
                break
            elif nums[r] < 0:
                break
            elif i>0 and nums[i] == nums[i-1]:
                continue
            while l < r: 
                summation = nums[i] + nums[l] + nums[r]

                if summation < 0: 
                    l += 1
                elif summation > 0: 
                    r -= 1
                elif summation == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return ans
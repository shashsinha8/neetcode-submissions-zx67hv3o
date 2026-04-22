class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        answer = []

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:break
            while l < r:
                
                res = nums[i] + nums[l] + nums[r]
                if nums[r] < 0:break
                elif res > 0:
                    r -= 1  
                elif res < 0:
                    l += 1
                elif res == 0:
                    answer.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

                
        return answer

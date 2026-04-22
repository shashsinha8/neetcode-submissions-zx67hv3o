class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        answer = []
        check = set()

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                if res > 0:
                    r -= 1
                elif res < 0:
                    l += 1
                else:
                    if (nums[i], nums[l], nums[r]) not in check:
                        check.add((nums[i], nums[l], nums[r]))
                        answer.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                
        return answer

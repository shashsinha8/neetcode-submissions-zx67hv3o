class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # 1. Identify if the LEFT half is the properly sorted half
            if nums[l] <= nums[mid]:
                # Is the target inside this properly sorted left half?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Target is here, search left
                else:
                    l = mid + 1  # Target is not here, search right
                    
            # 2. If the left isn't sorted, the RIGHT half MUST be the sorted half
            else:
                # Is the target inside this properly sorted right half?
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Target is here, search right
                else:
                    r = mid - 1  # Target is not here, search left

        return -1
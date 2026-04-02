class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums_hash = []

        for n in nums: 
            if n in nums_hash: 
                return True
            else:
                nums_hash.append(n)
        return False
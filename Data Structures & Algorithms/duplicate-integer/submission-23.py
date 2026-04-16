class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        DuplicateHash = set()

        for n in nums: 
            if n in DuplicateHash:
                return True
            else: 
                DuplicateHash.add(n)
        
        return False

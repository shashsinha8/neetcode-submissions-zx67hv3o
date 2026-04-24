class Solution:
    def findMin(self, nums: List[int]) -> int:
    
        smallest = 10**18 

        for n in nums: 
            smallest = min(smallest, n)
        
        return smallest

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counter = 0
        while n:
            counter += 1 if n & 1 else 0
            n = n >> 1

        return counter
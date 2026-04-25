class Solution:
    def hammingWeight(self, n: int) -> int:
        

        # m = n
        # ans = 0

        # while m: 
        #     bit = m % 2 
        #     m = m // 2
        #     if bit == 1: 
        #         ans += 1
        
        ans = 0
        while n:
            ans += n & 1
            n = n >> 1
        return ans

    

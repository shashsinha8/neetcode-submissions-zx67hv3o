class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans = []
        # for number in range(n+1): 
        #     count = 0
        #     while number:
        #         count = count + (number & 1)
        #         number = number >> 1
        #     ans.append(count)
        # return ans

        ans = [0]* (n+1)

        for i in range(1, n+1):
            
            ans[i] = ans[i>>1] + (i & 1)
        
        return ans
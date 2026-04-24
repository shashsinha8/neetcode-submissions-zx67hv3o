class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for number in range(n+1): 
            count = 0
            while number:
                count = count + (number & 1)
                number = number >> 1
            ans.append(count)
        return ans